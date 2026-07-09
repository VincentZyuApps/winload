#!/usr/bin/env python3
"""Generate Shields.io badge Markdown with a base64-embedded local logo."""

from __future__ import annotations

import argparse
import base64
import textwrap
from io import BytesIO
from pathlib import Path
from urllib.parse import quote, urlencode

from PIL import Image


WHITE = (255, 255, 255, 255)
TRANSPARENT = (255, 255, 255, 0)


def png_data_uri(png_bytes: bytes) -> str:
    encoded = base64.b64encode(png_bytes).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def image_to_png_bytes(image: Image.Image) -> bytes:
    buffer = BytesIO()
    image.save(buffer, format="PNG", optimize=True)
    return buffer.getvalue()


def load_png(image_path: Path) -> Image.Image:
    with Image.open(image_path) as image:
        return image.convert("RGBA")


def remove_white_background(
    image: Image.Image,
    *,
    white_threshold: int,
    soft_threshold: int,
) -> Image.Image:
    """Turn white and near-white background pixels transparent."""
    if not 0 <= soft_threshold <= white_threshold <= 255:
        raise ValueError("--soft-threshold must be <= --white-threshold, both in 0..255")

    result = image.convert("RGBA")
    pixels = result.load()

    for y in range(result.height):
        for x in range(result.width):
            red, green, blue, alpha = pixels[x, y]
            minimum = min(red, green, blue)

            if minimum >= white_threshold:
                pixels[x, y] = (red, green, blue, 0)
                continue

            if minimum >= soft_threshold:
                fade = (white_threshold - minimum) / max(1, white_threshold - soft_threshold)
                pixels[x, y] = (red, green, blue, int(alpha * fade))

    return result


def content_bbox_by_color(image: Image.Image, *, white_threshold: int) -> tuple[int, int, int, int]:
    """Find the non-white content bounding box."""
    left = image.width
    top = image.height
    right = 0
    bottom = 0
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            red, green, blue, alpha = pixels[x, y]
            if alpha > 0 and min(red, green, blue) < white_threshold:
                left = min(left, x)
                top = min(top, y)
                right = max(right, x + 1)
                bottom = max(bottom, y + 1)

    if left >= right or top >= bottom:
        return (0, 0, image.width, image.height)
    return (left, top, right, bottom)


def crop_and_pad(
    image: Image.Image,
    *,
    bbox: tuple[int, int, int, int],
    padding_ratio: float,
    background: tuple[int, int, int, int],
) -> Image.Image:
    """Crop around content, then place it on a square canvas with a small padding."""
    if padding_ratio < 0:
        raise ValueError("--padding-ratio must be >= 0")

    cropped = image.crop(bbox)
    content_size = max(cropped.width, cropped.height)
    padding = round(content_size * padding_ratio)
    canvas_size = content_size + padding * 2
    canvas = Image.new("RGBA", (canvas_size, canvas_size), background)
    offset = (
        (canvas_size - cropped.width) // 2,
        (canvas_size - cropped.height) // 2,
    )
    canvas.alpha_composite(cropped, offset)
    return canvas


def scale_from_center(
    image: Image.Image,
    *,
    scale: float,
    background: tuple[int, int, int, int],
) -> Image.Image:
    """Scale the logo around its center and crop/pad back to the original canvas size."""
    if scale <= 0:
        raise ValueError("--scale must be > 0")
    if scale == 1:
        return image

    target_size = image.size
    scaled_size = (
        max(1, round(image.width * scale)),
        max(1, round(image.height * scale)),
    )
    scaled = image.resize(scaled_size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", target_size, background)
    offset = (
        (target_size[0] - scaled_size[0]) // 2,
        (target_size[1] - scaled_size[1]) // 2,
    )
    canvas.alpha_composite(scaled, offset)
    return canvas


def make_with_background_logo(
    source_image: Image.Image,
    *,
    white_threshold: int,
    padding_ratio: float,
    scale: float,
) -> Image.Image:
    bbox = content_bbox_by_color(source_image, white_threshold=white_threshold)
    logo = crop_and_pad(source_image, bbox=bbox, padding_ratio=padding_ratio, background=WHITE)
    return scale_from_center(logo, scale=scale, background=WHITE)


def make_transparent_logo(
    source_image: Image.Image,
    *,
    white_threshold: int,
    soft_threshold: int,
    padding_ratio: float,
    scale: float,
) -> Image.Image:
    transparent = remove_white_background(
        source_image,
        white_threshold=white_threshold,
        soft_threshold=soft_threshold,
    )
    bbox = transparent.getbbox() or (0, 0, transparent.width, transparent.height)
    logo = crop_and_pad(transparent, bbox=bbox, padding_ratio=padding_ratio, background=TRANSPARENT)
    return scale_from_center(logo, scale=scale, background=TRANSPARENT)


def shields_url(
    *,
    label: str,
    message: str,
    color: str,
    style: str,
    logo_data_uri: str,
    label_color: str | None = None,
) -> str:
    params = {
        "label": label,
        "message": message,
        "color": color,
        "style": style,
        "logo": logo_data_uri,
    }
    if label_color:
        params["labelColor"] = label_color
    return "https://img.shields.io/static/v1?" + urlencode(params, quote_via=quote)


def markdown_badge(url: str, alt: str, link: str | None) -> str:
    image = f"![{alt}]({url})"
    if link:
        return f"[{image}]({link})"
    return image


def build_badge(args: argparse.Namespace, logo_png_bytes: bytes) -> tuple[str, str]:
    url = shields_url(
        label=args.label,
        message=args.message,
        color=args.color,
        style=args.style,
        logo_data_uri=png_data_uri(logo_png_bytes),
        label_color=args.label_color,
    )
    return url, markdown_badge(url, args.alt, args.link)


def build_markdown(
    image_path: Path,
    image: Image.Image,
    *,
    with_bg_bytes: bytes,
    transparent_bytes: bytes,
    with_bg_md: str,
    transparent_md: str,
    scale: float,
) -> str:
    return textwrap.dedent(
        f"""\
        # Shields.io Homebrew Logo Badge Test

        Source image: `{image_path.name}` ({image_path.stat().st_size} bytes, {image.width}x{image.height})

        ## Notes

        This script uses Pillow to generate two base64-logo Shields.io badges from the local PNG:

        - one badge keeps the original white background
        - one badge removes white / near-white pixels and keeps transparent background
        - both badge logos crop away outer whitespace and re-pad the content so the beer icon is larger
        - both badge logos are scaled from the center by `{scale:g}x`

        ## With White Background

        {with_bg_md}

        ## Transparent Background

        {transparent_md}

        ## README Snippets

        With white background:

        ```md
        {with_bg_md}
        ```

        Transparent background:

        ```md
        {transparent_md}
        ```

        ## Size

        - Original-background PNG payload: {len(with_bg_bytes)} bytes.
        - Transparent PNG payload: {len(transparent_bytes)} bytes.
        """
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate Shields.io badge Markdown with a local base64 logo."
    )
    parser.add_argument("--image", default="logo.homebrew.png", help="Local logo image path")
    parser.add_argument("--output", default="test-shield-io.md", help="Markdown output path")
    parser.add_argument("--white-threshold", type=int, default=245, help="Pixels with all RGB channels >= this become fully transparent")
    parser.add_argument("--soft-threshold", type=int, default=225, help="Pixels with all RGB channels >= this fade toward transparent")
    parser.add_argument("--padding-ratio", type=float, default=0.0, help="Padding around cropped logo content; smaller makes the logo larger")
    parser.add_argument("--scale", type=float, default=1.0, help="Center-scale the final logo canvas; keep 1.0 for compact base64")
    parser.add_argument("--label", default="Homebrew", help="Badge label")
    parser.add_argument("--message", default="tap", help="Badge message")
    parser.add_argument("--color", default="FBB040", help="Badge color")
    parser.add_argument("--label-color", default=None, help="Optional badge label color")
    parser.add_argument("--style", default="for-the-badge", help="Shields.io badge style")
    parser.add_argument("--alt", default="Homebrew", help="Markdown image alt text")
    parser.add_argument("--link", default="https://brew.sh/", help="Optional Markdown badge link")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    image_path = Path(args.image)
    if not image_path.is_absolute():
        image_path = script_dir / image_path

    if not image_path.exists():
        raise FileNotFoundError(image_path)

    source_image = load_png(image_path)
    with_bg_image = make_with_background_logo(
        source_image,
        white_threshold=args.white_threshold,
        padding_ratio=args.padding_ratio,
        scale=args.scale,
    )
    with_bg_bytes = image_to_png_bytes(with_bg_image)
    transparent_image = make_transparent_logo(
        source_image,
        white_threshold=args.white_threshold,
        soft_threshold=args.soft_threshold,
        padding_ratio=args.padding_ratio,
        scale=args.scale,
    )
    transparent_bytes = image_to_png_bytes(transparent_image)

    with_bg_url, with_bg_md = build_badge(args, with_bg_bytes)
    transparent_url, transparent_md = build_badge(args, transparent_bytes)

    markdown = build_markdown(
        image_path,
        source_image,
        with_bg_bytes=with_bg_bytes,
        transparent_bytes=transparent_bytes,
        with_bg_md=with_bg_md,
        transparent_md=transparent_md,
        scale=args.scale,
    )

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = script_dir / output_path
    output_path.write_text(markdown, encoding="utf-8", newline="\n")
    print(markdown)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
