![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> Linux의 `nload`에서 영감을 받은, 네트워크 대역폭 및 트래픽을 실시간으로 모니터링하는 경량 CLI 도구입니다.

> **[📖 English](readme.md)**
> **[📖 简体中文(大陆)](readme.zh-cn.md)**
> **[📖 繁體中文(台灣)](readme.zh-tw.md)**
> **[📖 文言文](readme.lzh.md)**
> **[📖 日本語](readme.jp.md)**
> **[📖 한국어](readme.ko.md)**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VincentZyuApps/winload)
[![Gitee](https://img.shields.io/badge/Gitee-C71D23?style=for-the-badge&logo=gitee&logoColor=white)](https://gitee.com/vincent-zyu/winload)

[![Windows x64 | ARM64](https://img.shields.io/static/v1?label=Windows&message=x64%20%7C%20ARM64&color=0078D4&style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTAgMGgxMS4zNzd2MTEuMzcySDB6TTEyLjYyMyAwSDI0djExLjM3MkgxMi42MjN6TTAgMTIuNjIzaDExLjM3N1YyNEgweiBNMTIuNjIzIDEyLjYyM0gyNFYyNEgxMi42MjN6IiBmaWxsPSIjZmZmIi8+PC9zdmc+)](https://github.com/VincentZyuApps/winload/releases)
[![Linux x64 | ARM64](https://img.shields.io/badge/Linux-x64_|_ARM64-FCC624?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![macOS x64 | ARM64](https://img.shields.io/badge/macOS-x64_|_ARM64-000000?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Android x64 | ARM64](https://img.shields.io/badge/Android-x64_|_ARM64-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)

[![PyPI](https://img.shields.io/badge/PyPI-3776AB?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/winload/)
[![Python Versions](https://img.shields.io/pypi/pyversions/winload.svg?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/winload/)

[![Crates.io](https://img.shields.io/badge/Crates.io-000000?style=for-the-badge&logo=rust&logoColor=white)](https://crates.io/crates/winload)

[![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/package/@vincentzyuapps/winload)

[![Scoop.sh](https://img.shields.io/badge/Scoop.sh-7B4AE2?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjeD0iMTIiIGN5PSI4IiByPSI1IiBmaWxsPSIjRUM3MEExIi8+PGNpcmNsZSBjeD0iOCIgY3k9IjEyIiByPSI0LjUiIGZpbGw9IiNFQkYzQTEiLz48Y2lyY2xlIGN4PSIxNiIgY3k9IjEyIiByPSI0LjUiIGZpbGw9IiM4RTZFQzgiLz48cGF0aCBkPSJNMTYuNSA0bC0xLjUtMS41TDExLjUgNmwxLjUgMS41eiIgZmlsbD0iI2ZmZmZmZiIvPjxwYXRoIGQ9Ik0zIDEzaDE4YzAgNC40LTMuNiA4LTggOGgtNGMtNC40IDAtOC0zLjYtOC04eiIgZmlsbD0iIzRGNEI1MyIvPjwvc3ZnPg==)](https://scoop.sh/#/apps?q=%22https%3A%2F%2Fgithub.com%2FVincentZyuApps%2Fscoop-bucket%22&o=false)
[![AUR](https://img.shields.io/badge/AUR-1793D1?style=for-the-badge&logo=archlinux&logoColor=white)](https://aur.archlinux.org/packages/winload-rust-bin)
[![APT](https://img.shields.io/badge/APT-E95420?style=for-the-badge&logo=debian&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![RPM](https://img.shields.io/badge/RPM-CB1626?style=for-the-badge&logo=redhat&logoColor=white)](https://github.com/VincentZyuApps/winload/releases)
[![Homebrew](https://img.shields.io/static/v1?label=Homebrew&message=tap&color=FBB040&style=for-the-badge&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAAJQAAACUCAYAAAB1PADUAAAYyUlEQVR42u1dfViT57n%2FRdoQIEWQxiGEDiEIA6GeZrZdLKvIeg3X8zo7r0lDZ6lcs%2BBOVziTGefV8gf90NS4q85ejXZrJt1ZkK472Ug17LQ29rhgrXKqoiBfgiUSBho%2BDBKi%2BJw%2F6PuaQICAURJ4ftf1XNebl5f3I%2B8v930%2F93N%2F8Agh8Gf09PTI%2F9V9RZu0JIEHihnHPH9%2FgHXr1mmXSx9BUVERqa6uJvSVzjAIIX476hsaCQCXIZVKicFgIP78XP48%2FFpCXag7P2ZfTU0NVq9ejRdeeIFcaGyiEouqPM%2FR0tLCbZtMJpSWlkIsFgMAysrK8J3EJdi9ezfp6emR01dNCTUprl%2B%2Fzm1HRUXhp9nPoqKiAgqFgttfXFyM3NxcbVtbG5VWlFBTg8PhgDB0PgoKCmAwGMAwDABAr9dj8eLFqKqqoqSihBofwcHB3Ha%2FbcBlOzYuHq%2B%2FuQOFhYXc%2FtWrV2OqM8Hq6mqqMucKoeLj47ntDnM7%2BHy%2Bi7QCgKKiIqjVam7%2FihUrPCZVQUEBWbFiBRYsWKAtLy%2Bn0m22EyopOYXbPn%2F%2BvNtj%2Bm0DWLkq04VUmzZtwmQzwG3btpH9%2B%2Fdzn3NyckBJNdsJ5eQdr62tndC2ysrKgkqlAgDU1dVha%2FGWCcmkVCoBAAzDQCQSUVLNFaOctZEOHz6Mtost4x7XbxvA08wa7ni9Xu%2BWHOXl5S5k2rZtG9577z1IJBKOVNS%2FNYsJlffzTQCA7u5unDx5EqHCkAklVd7PNyE5ORkA8Prrr6Ozs7OS%2FfuFxiaSk5PjLKmw4EER4iQJiImJ4fYf%2FewIZc5sJVTa0hRednY2AKCkpMRltucOfD4fxcXFnOozGAwM%2B7dfFORzx2m1Wix4cETVbc5%2FEUajkZNaBQUFdCF6NvuhXn755dtE%2BK8%2Fucz23Ekp6fJHkZGRwZEQAP72t78RljSFhYX4N%2Bl3AQAHNO%2BjuroaAJCbm4vKykpKpgnA8%2FfwFRarVq3iCKHT6ZCUnMK5DtxJqaOfHcHmzZsBAAaDAW%2B99RYnhc7UnhtzjFQqxalTpyiZ5gqhzp47T1Z873HYbDYkJyejvOLDCY%2B39fchOzsbZrMZEokEzc3NAAC1Wo2VqzLhcDjAnk8ikeCTTz5BbGwsJdRcWXpJW5rC27VrF2cb%2FVa1a0LVFxUVhYSEBADgyCSTySB7Ip1TnTabDQCwa9cuSqa5uJZXUFDAY9fvysrKcEDz%2FrizPrvjBmdHsUhPT0eoMATWK93Q6%2FUAAIlEgrVr11IyzUVCAcB7772nZ4miVCrxpz%2BNb6Snpqa6fF6zZg3sjhtoaGhAXV0dAGDv3r2UJXOZUJGRkWs0Gg33uaSkBH%2BpODhGUjkcDixcuJD7LBKJIAydDwH%2Ffuh0Ok4FLlu2TE9pMocJBQCxsbG81tZWzoFZUlKCffv2uT2WPeZHP%2FoR%2BHw%2B%2Bm0DnLpLT09HZGTkGkoTz3HfbHugs%2BfOkw5zOwAgLy%2BPc2IqlUr09vai6FdbXKIRvv76awC3IxfY%2FwWAxMTECa%2FV1tZGOjo60N%2FfP2Loi2MQEx2VEx4eXg6apOCf40ztOaLRaIhYLB6TsOBuJCcnE51OR%2BobGonJZOL2q1QqUt%2FQSDQaDbfvTO05l2QHq9UqN5lMJDc3d8JriEQiolarSWtr65xLlvDbGzcYDJO%2B2PGGUCgkKpXKhVAsAdRqNbfParXK2etptVrCMMyUr6NQKIjFYqmcK4TyO8dmdXU12bRpEzcLY8EwDOLi4vDwww9j0aJFI64Bux0tLS1oamrCqVOnUFNTM%2B55S0tLsWHDBvz1r3%2Fl1KRWq8WZM2fARh%2BwkEgkWLFiBVJTUxEfHw%2BBQAAAsFgs3AyRtcNYqFQqbNmyhUdtKB%2FCH%2F%2F4R5KXl%2BeyT6FQYOXKlYgSx7h1D7BBeNYr3bh06RL%2B%2Fve%2Fo6KiYsxxly9fHrPPOfIAAIRCIbZu3YrMzExu4dhlMhAXj%2B%2BteGIkqiEvDwcPHuSuVVxcjM8%2F%2F5yUlZXNahvLLyRUT0%2BPPDc3V%2Bv8qy8tLcWPn%2FkJQoUhk0YYwGkNT8C%2FH%2F22AdSc%2FBInTpxAY2Mj2tvbsX37dnxvxRO4UHcezzzzDPc%2FUqkUS5cuxeOPP46VqzJdDHpPrnX69Gn87ne%2F49YJxWIxKioqIJPJeJRQPkAmqVSKV155ZcLFX0%2FJxUouABCGzuf%2BdrG5CQAgEAgQGhrKSaPpXI%2FP58PhcODdd%2FaCDSkWiUT433%2BaMBvrMfg8odasWUNYMjEMg7dUu6f9cqdDBG%2Be75C%2BkrPPxGIxPjny2awjlU87Nl977TUXMr3%2B5o57Qqa7cQ2Hw4GnmTVcXLvZbMa6Z9ZST%2Fm9QlVVFWGD3zIyMu6ZZLrbJH2aWcNlNtfV1WH37t2Eqry7jM7OzsrMzEymrq4OEokEe%2FfuRWxcvF%2BTabT6W%2FfMWtTV1UEoFMJ0%2FAukLU3hUQl1l%2FD73%2F%2BeYf1M27dvn1VkYrF794jEtdlseGX7b6jKu5vSiVV1DMNAuvzRWUcmh8OB2Lh45OfncyldsyU1y%2BcItXPnTi4LJS8vb8KoS3%2FH888%2Fz20f0LxPJZS30dbWRg4dOsRJpzv1Nfm6lIqKiuKiRo8dO%2BaSI0gJ5QUYjUYuvnv0EouzQes8%2FBl2xw1s2LABAFBdXY2LFy8yoGt53gMbKSmVShEnSeCkE%2BtktPX34dKlS%2Bjo6AAAhISEIDY29o692TMppRITE7msmyNHjkAmk1FCecsYZ52YP%2FjBDzjp43A4cPSzI%2Fjwww%2B59bDREIvFeO6557By5UokJSV5vLbnbVeAgH%2B%2Fi%2FTxhODC0PmQSqVobm7G3r178eqrr1JCeQOnT59m2BX9hx9%2BGADwVc0plJSUcGoQTuEjANDX14fu7m6YzWYolUoolUooFArk%2FGyD15dOJlqe6TC34%2Fz582hvb0dvby%2FCwsIQExOD%2BPh4LFy4cELpyefzERkZCWCkPgNVeV7C0aNHAQCRkZFISU3DXyoOcmniwEjsd3FxMRITE7kXZL3Sja6uLlRVVXELr0qlEnV1dXj9zR13jVSs9Dykr8ShQ4fGlZzsfT%2F11FNYv349Fjwocns%2FzoU42traiD%2FnAPqMp5xdBM7IyMD69eu5FHCRSIQ9e%2FZALpfzJoslf%2FP117j4I%2Be1P2%2BT6auaU9i9e7dLwJ5IJEJCQgIiIiJw9epVdHV1uUhWkUiEX%2F7yl%2Fhp9rMupOLz%2BS4hMyaTya9DW3xGQrFZuk1NTXjjjTe4%2FZ9%2BZvRoWSJtaQrv4MGDEAgEpKysDHq9HnFxcSgqKvKaTcXn83Hc9E%2BXGahYLMZbb72FlNQ0LHwwQh8YGFg%2BNDQk7%2B2%2FxrRdbMG7774LvV6P7u5ulJSUYGBgADk%2F2%2BByXjbiEwC6urqoyoMXYp6GhoYAjKzCw6n2%2BFTXuA4cOMCz2%2B2koqICe%2FbsGTHUR%2Fmz3NXidJ4EeFJgAwA0Gg02btzo7v7KIyMjkbQkAVlZWaiuriYvv%2FwyampqXLJvHA4HHA4HQkNDnb8LSqi7gdLS0mmL%2Fp07d3Kqr6qqigsDZmdiHR0dOH78ONrb22G32zkpkZSUhLS0NERFRcHuuOFCNuuVbhcy6XQ6j1PUZTIZ76OPPiJ5eXkwGo3Yv38%2Fli1bxhXlcA7us1qtoGlUdzisVqtcJpO5ZIw4Z5xMZygUCu5cJpOJ1Dc0Ep1ORzIyMibNVmEYhku1OlN7jpypPUeys7O5v0%2B3l4zFYqlk072Sk5OJyWQiJpOJaLVal2sbDAZS39BIaBrVNPPqCgsLiUgk4r7UwsJC4o00K%2FZ8Op2OlJaWTjndqrS0lNQ3NBLnc%2BXm5t7Rvel0OhfySCSSca%2Bfm5s7JjeQEmqCX6vzr955eKObVGtrK0lOTnabhKlQKNy%2BqDO158YQLzc3lzhLO28kb7p77uTkZJKRkUFGS2qW2JRQk5BptOrJzs4mGo2GmEwm4q1rjH45YrHYI1ViMpmIVCp1Sdj0hnRih3N2cnZ2NjGZTKS1tZVYLJZKi8VS6Y7Y%2FkKqGbGXnL%2BowsLCO7aXPCEUwzBTfiGjSa9SqYg3e%2F1N9txWq1XufA9qtZpQQo0azr%2B8u%2Fmrq29odLFPpqOqztSec7HttFotmckJi1Ao9Pm09ntugHvLuJ2K8avRaKZ9LedaBzNBqNHfmzelpN939Kz%2B5zFu%2B1fFv76r1xocHIRTF6ppFw3Lzs7m8tGDgoIwU%2FVD2VKPn3%2F%2BOXy6O9a9ZC%2BrgvLz88m9UBVqtdorRr7JZJpx%2B8XZV%2BXLau%2FeXsxPxLavli%2FyB0LNypKIFJhbMeXOvYIpPIPFYqGEGg3WsDx58iRo29Wp4Q9%2F%2BAM7SfDpQrL3lFBsEJler0d9fb2W0sTzqn1sA6Mf%2FvCHNNrAeX2NnelJpVJqmHvo8WfXJIVC4V1ZVfBrT7mzo%2FBuLbvMllHf0OhS3Vin09GlF3fDuZpuRkaG1xaEZ8NobW0lBoPBJcKBLg574HTMz893%2BcJkMhlRKBTEYDCQ1tbWOSO5rFarnI0Jk0qlY%2BKjhEKhXywK%2B0SAnUqlGje4TCqVEoVCQbRard8FmXnqfVepVG5jttgxXtwWJZQHSyTO8UdwU0A%2BOTmZi5mqb2gkFoul0p%2BkmMViqWSL9buL0mRjrqRSqVcCDOd8JwXWWJdIJESr1Y6xIdy9AIZhSGlpKVGr1cRgMJAzted8UlU6d2xwF%2Bar0%2BkIawIwDOPX6t5nsl4GBkZy5%2BbPn4%2BsrKwcuVxevnPnTnR2dlYajUbm4%2F3%2Fib4BB862XUf7lSHYbDbo9foxHQtEIpE2MDBQm5CQgLS0NCQlJSE2NpYrjC%2Fg3w%2BBQKAHgMDAQK4A%2Fd0sRn%2F27Flue2Uy8O2ULKzNyceTTz7JFcE%2FevQooZ0U7nLYCTDS%2F04ul%2BOnQe%2BQa0MB6LA68K%2BeITRevo7TF23YX9XhcjxbH8BsNo%2BbIi4SiZhvsnyZ4OBgNo1KGxYWxh3DplcBQFhYGIqKivTT9VCfPn0aALAkOgQHfx0NUfpLmBf%2FNI%2B25phhPCAIQGJUEBKjgrDqkQgAwDsFS3DNPowOqwPNluuovzSAti47rg0Oo2%2FAAUvPTXT3OdB%2BZciFdFMtTGG325m3334b0ymixtZd2Jj5LUQI3de0iogYeZ6vvvoKJ06c0CYlJWnZCi7uwEpaX1uG8dt%2BeTeHhm8TLXAYiYsCkLJ4IX4su%2F33a%2FZh9A8OwzY4jL7rN2H%2FZp%2Fl6hB6bTdhtd0EAFy%2BOoS%2BgbEZw%2FND%2BDh2vhftV4awZ88ebNu2rXKqL5Bt%2FCgUCsE8LgLgPi0%2BMzMTJSUlMJvNWL16tUfnlkqlzNKlS0lqaiqee%2B45nyCXfzdgJA7wgqPBC4oAGbyKm4PdYyTaA4IAIHzUQwcGeHyJ8602LP3FCQBATk4Oo9VqPSZVZ2dn5Z%2F%2F%2FGcAwHNPhCJlsRA3x6mzIJPJeFqtloxuWDQRampquIIdxcXFjEKhIAqFYkabE%2Fk1oeZFpGGeWHqbXz1fY7jtEyBA4LF0mwwpi4X49U8ewq7%2F%2FhpGoxE5OTmMRqPxqOTOF198wbC1GtanL5z0unK5nJeSmkZs%2FX1cl9AJVDBaWlqwb98%2BrsqLUqnEp59%2Bqv3oo4%2B0M1USyCcJNTQ0JAcw4a%2BMFyQaIdPwbTuDF%2F4Q5g0sw62rZwEe32uq9c3n47BAeB9%2B88FFGI1GLF68GDqdjkxW26ClpYXb%2Fn5KGDyNH5%2FK%2FW3ZsgUXGpvIzjffQFlZGWpqavDoo4%2Fi08%2BMZCaK6fttxCYvKGLszuEb4IWIgFu3vH694p88hB3Px7mE4rS1tU041W9vH%2Blf%2FPR3w%2B%2Fqd5G0JIF34MABnlqt5iYd8uz1tArwVGynmcA2%2BWKYVNIxBvd46O3tBQCIH7w32TIFBQU8jUYDYKSPzGuvvUYooXx8ZilLCUPOk9%2FiXpqvRZ5u3LiRJ5WOkP7gwYOTSlFKKB9A6rdDOBvpG3vPp6A5UMYR%2Fvjx49Qo93Up9Z1vCFVXV4euK1cZtoovRlXlO3nyJAAgNPg%2B3BcY4PHs8uy584TtKuoOAoEAy5YtG9fvFBMdlcMwjFav1%2BMf%2F%2FgH5HI5JZQvY1ncA1gSHYLGywNY98xafPnll%2FLRvp%2BKigot21FrRcp8j8h0obGJLJc%2BwtUbnQRMfn4%2B2bFjxxi%2FU3h4ePny5cu1er0eZWVlOHDgAFV5voxvRwZhY%2BaIHdXc3IynnnpKu2%2FfPlJdXU3Ky8vJCy%2B8QNjyiY%2FEP%2BCRy6Czs7PyZzlyjkxCodDtcc779%2B%2FfD6VS6TbZg12jBPVD%2BYfa2yZfjLYuO%2FZXdbh4rJ2xJDoEH2xJRvh8%2FqQSymg0Muw5VCoV1q1bh%2FHW8hwOB36r2oWysjIolUoUFRVV%2BsqaHiXUHZDqnYIlWL08Als1F9HRx4PNZoNQKES44Aae%2Ff638B%2BMGNHhfI%2FU3YkTJ7h2uHl5eZMun7z44oukrGzE%2BL548aJbO25OEyokJMQvifVj2UI8LY1AQ8cg%2Bq7fxPzg%2B5AYFTQlI3w8lebJsR7aW1RC%2BVvUw2gSTYdMoLUNKKa76EwJRUFBCUVBCYWRcFv6aiih4K22qRSUUBQUlFAUlFAUlFAUlFAzgMDAQPo2KKEoKCihKCihKCihKCihKCgooSgooSgooSgo%2FItQAoGAvg1KKAoKSigKSigKSigKSigKCkooCkooCkooCgpKKApKKApKKO8gKCiIvo0pwtdK%2BQC0nI%2FP4LHHHgMA6PV6VFRUaNeuXSufKCX%2Fgw8%2B4Lbj4uL0lFAULsjIyNBLJBKmubkZmzdvxubNmz2q71BYWAhfanFGbSgfQWRk5Br9ocOQyWQe%2F09hYSHefvttHlV5FBivZ8vHH38sr6%2Bv107WjSo0NBQymWxcMjU1NbFt0yihJupkOdsRHh5eLpPJ7qjf3YXGJq6L6IYNG6jKo7gzHNC8z22npaVRQlFMH9XV1USpVHI21kRqcU4QyrkbOcXUVV1ubi73uaioiM7yKKaOnp4eeXl5OflO4hKuXazBYMBMtImlszw%2Fl0hHPzuCw4cPQ6%2B%2F7dvUaDTIysqiPYcpQZrIU5mrwDa%2BnipkMhl27dp1z%2B0mqvJ8EG1tbdMmk1AohEajwccff5wzk2TyWQk1aSXg8TqeB9zvt4SqqqqC2WyGUCjE1q1bIZFI3E5QhoaGAIwUaFu0aBGSkpJmxFbyeUJNNdHzVt8lzFuUNkKi4duO0OGOU0CA%2FyWNXrhwAcBIN6qXXnpp0m5UoOErXsbNPty8oAfp%2BRoAQPotGG76H8DRQ%2FUnlVCeiKRbQMAotTc8iOH2Y0BAEDA8CBCHX0gnHj8UNMBupl%2BCMAYYHsfpOTw4sW3lCyAO4MYV8MTrwYtJ51FCzfSNSksBfvgIqcYjli%2Fim%2FvlBUcj4LF3EfD4q7OWTH6l8ngRSbz7%2Fv0wSPsxcuvyURDzh988QajvSSbiAG6OhJ%2FwxOsxL3rlrJZKfu3Y5MWk8wJi0kGubbyM3tYo0qbFrb5LI2rvxhVgnhCYN%2B%2Fekowl0DwhECAALzgavPjt4C18uIP3gDiaGuUzCNbPMimxHhBH4wExeDHpmAeAtB8jxNEP0v1%2FQH8tSH%2F9KJ3pBaIRx8jk4JbN5bzzRMuA0EfAW5AEhC2ecyTyaUJNt6MCLyadxwOA%2BKdH3v0182U4bFG43g1ivQAy2AnejQ6QwasgDtttY56dIY5GQNComdlIc2leUAQlz1xcy%2BNedEQSeDHpY4XNNfNl7oPDFuX2JHxhh8u5KOji8KSE8xGcPXsWABAcHAx%2F9ZL7pNvAbDbD1t%2BHuRRh%2BeyzzxKj0QgASElJ8e8HIoT4xLBYLJUACDvUajWxWCyVvnJ%2F3hxWq1VuMpkIwzDE%2BZmlUinx92fzqZtRqVQuXzAAolAoiFarnRXkMplMRKVSkYyMjDHPqVaridVqlVNCeXkYDIYxv1x2SCQSUlpaSgwGA2ltbfVpklkslsr6hkai0%2BlIbm4uEQqFY55HKpWS0tLSWUEkdvAIIT5rW1RWVoLN4MA4EYqpqamIjo6GSCRCbGwsosQxWPhghP5epme3tbWRjo4ONDQ0wGw24%2FLlyzh16hRqamowTto5tm7d6nOxTF6Z7PgqoTAqNPYvFQfR0tKCpqYmVFdXe%2Fy%2FIpEIS5cuxUMPPYSwsDDExMQgJCQEgYGBCA8PnzAOy263Y3BwEH19fRgYGEB3dzd6e3vR2NiIkydPelz9JCMjA2lpaVi5ciXWrl07q5dg%2FIJQ7qRBV1cXamtrYTQawc6QfAUymQxZWVlYvnz5jEhMSih4J5XoX91XtNYr3bh06RKam5sxMDAAu92O3t5e2O12XL9%2BHTabDf39%2FRgcHITD4UBfXx8GBwfH1FsSiUQIDAyEQCAAn89HWFgYIiIiEBwcjLCwMAgEAggEAohEIsTHxyNOkoCY6Kgcf%2FYhUUJNg3RDQ0Pyb9QZM7qOgsPhAJ9%2Fe61PwL%2FfOURZHxgYWA4Ac500E%2BH%2FAaiKv7mXsenrAAAAAElFTkSuQmCC)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)

> **[📖 빌드 문서](.github/workflows/build.md)**

## 🚀 소개
`Winload`는 현대적인 터미널 환경에서 직관적이고 시각적인 네트워크 모니터링 기능을 제공합니다. 처음에는 Windows 환경에서 `nload`의 공백을 메우기 위한 도구로 시작되었으나, 현재는 Linux와 macOS까지 지원 범위를 확장했습니다.

## 🙏 감사의 말
Winload는 Roland Riegel의 고전적인 프로젝트인 「[nload](https://github.com/rolandriegel/nload)」에서 영감을 얻었습니다. 독창적인 아이디어와 훌륭한 사용자 경험을 제공해 준 원작자에게 깊은 감사를 표합니다.
https://github.com/rolandriegel/nload

## ✨ 주요 기능
- **두 가지 구현 방식 제공**
	- **Rust 버전**: 빠르고 메모리 안전하며, 단일 정적 바이너리로 제공되어 일상적인 모니터링에 최적화되어 있습니다.
	- **Python 버전**: 구조가 단순하여 프로토타이핑이나 기능 확장, 통합이 용이합니다.
- **교차 플랫폼 지원**: Windows, Linux, macOS (x64 및 ARM64)를 모두 지원합니다.
- **실시간 시각화**: 실시간으로 유입(Incoming) 및 유출(Outgoing) 트래픽 그래프와 처리량 통계를 보여줍니다.
- **미니멀한 UI**: `nload`의 사용성을 계승한 깔끔한 TUI(텍스트 사용자 인터페이스)를 제공합니다.

## 📊 성능 벤치마크
> ⚡ Winload (Rust)는 **~10ms의 시작 시간**과 **2MB 미만의 바이너리 크기**를 달성하여, Python 버전을 크게 능가하며 C++ nload와 대등한 효율성을 보여줍니다.

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🔧 소스에서 실행

### Python
```bash
git clone https://github.com/VincentZyuApps/winload.git
# 또는 Gitee에서 클론 (중국 본토에서 더 빠름):
# git clone https://gitee.com/vincent-zyu/winload.git
cd winload/python
uv run python -m winload
```

### Rust
```bash
git clone https://github.com/VincentZyuApps/winload.git
cd winload/rust
cargo run --release
cargo run --release -- --help    # 도움말 표시
cargo run --release -- --version # 버전 표시
```

## 🐍 Python 버전 설치
> 💡 **구현 참고사항**: PyPI 및 GitHub/Gitee 소스 코드만 Python 버전입니다.  
> Cargo만 Rust 소스 코드 로컬 빌드를 제공합니다.  
> 모든 다른 패키지 관리자(Scoop, AUR, npm, APT, RPM) 및 GitHub Releases는 **Rust 바이너리**를 제공합니다.
### Python (pip)
```bash
pip install winload
# uv 사용을 권장합니다:
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv --python 3.13
uv pip install winload
uv run winload
uv run python -c "import shutil; print(shutil.which('winload'))"
```

## 📥 Rust 버전 설치 (권장)
### npm (크로스 플래트폼)
```bash
# 권장（scoped）
npm install -g @vincentzyuapps/winload
# 대체（unscoped）
npm install -g winload-rust-bin
# 대체（GitHub Packages）
npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
# Windows에서는 System32\winload.exe와의 충돌을 피하기 위해 win-nload 사용
# Linux/macOS에서는 winload 또는 win-nload 모두 사용 가능
# 또는 npx 를 직접 사용
npx @vincentzyuapps/winload
```

> 4가지 사전 컴파일된 바이너리 포함: x86_64 & ARM64, Windows·Linux·macOS 대응.

### Cargo (소스 코드 빌드)
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop 이용)
> 📄 [Scoop Bucket (GitHub)](https://github.com/VincentZyuApps/scoop-bucket/blob/main/bucket/winload.json)
> 📄 [Scoop Bucket (Gitee)](https://gitee.com/vincent-zyu/scoop-bucket/blob/main/bucket/winload.json)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
# 또는 Gitee에서：
# scoop bucket add vincentzyu https://gitee.com/vincent-zyu/scoop-bucket
scoop update   # optional: 설치 전에 수동으로 bucket 목록 업데이트
scoop install winload
# 바이너리 파일 실행
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 기존 Windows Console 대신 [Windows Terminal](https://github.com/microsoft/terminal) 사용을 권장합니다. CJK 문자 렌더링과 TUI 환경이 더 우수합니다.
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```
> 💡 **모든 빌드는 Windows 10+가 필요합니다**（Rust 1.77+에서 Windows 7/8 지원이 중단되었습니다）。Scoop은 **x86_64** 및 **ARM64**용 **MSVC + Npcap** 빌드만 제공합니다.

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Debian & RedHat 계열 배포판 / Termux (간편 설치 스크립트)
> Debian/Ubuntu 및 파생 버전(Linux Mint, Pop!_OS, Deepin, UOS 등) 지원 (apt)

> Fedora/RHEL 및 파생 버전(Rocky Linux, AlmaLinux, CentOS Stream 등) 지원 (dnf)

> Android의 Termux (aarch64)도 지원

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash
which winload
```
> 📄 [설치 스크립트 소스 보기](https://github.com/VincentZyuApps/winload/blob/main/docs/scripts/install/install.sh)

**🇨🇳 Gitee 미러 (중국 본토 내 빠른 다운로드):**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash
which winload
```
> 📄 [Gitee 설치 스크립트 소스 보기](https://gitee.com/vincent-zyu/winload/blob/main/docs/scripts/install/install_gitee.sh)

> ⚠️ 위의 두 `curl ... | bash` 설치 스크립트는 **x86_64 / aarch64** 아키텍처에서 **apt**（Debian/Ubuntu）、**dnf**（Fedora/RHEL）또는 **Termux**（Android）를 사용하는 시스템을 지원합니다. 다른 플랫폼에서는 **npm**（`npm install -g @vincentzyuapps/winload`）또는 **Cargo**（`cargo install winload`）를 사용하세요.

### macOS / Linux（Homebrew）
> 📄 [Homebrew Formula (GitHub)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)
> 📄 [Homebrew Formula (Gitee)](https://gitee.com/vincent-zyu/homebrew-tap/blob/main/Formula/winload.rb)
> 최신 Homebrew에서는 설치 전에 서드파티 tap formula를 신뢰해야 할 수 있습니다.
```bash
brew tap vincentzyuapps/tap
brew trust vincentzyuapps/tap
# 또는 Gitee에서（수동 탭 클론）：
# git clone https://gitee.com/vincent-zyu/homebrew-tap.git "$(brew --prefix)/Library/Taps/vincentzyuapps/homebrew-tap"
brew update && brew install winload
which winload
```
> 💡 Homebrew는 **macOS**(Intel 및 Apple Silicon)와 **Linux**(x86_64 및 ARM64)를 지원합니다.

<details>
<summary>수동 설치</summary>

**DEB (Debian/Ubuntu):**
```bash
# GitHub Releases에서 최신 .deb 파일을 다운로드합니다.
sudo dpkg -i ./winload*.deb
# 또는 apt를 사용하여 의존성을 자동으로 해결하며 설치합니다.
sudo apt install ./winload*.deb
which winload
```

**RPM (Fedora/RHEL):**
```bash
sudo dnf install ./winload*.rpm
which winload
```

**또는 [GitHub Releases](https://github.com/VincentZyuApps/winload/releases)에서 바이너리를 직접 다운로드할 수 있습니다.**

</details>

## ⌨️ 사용법

```bash
winload              # 활성화된 모든 네트워크 인터페이스 모니터링
winload -t 200       # 새로고침 간격을 200ms로 설정
winload -d "Wi-Fi"   # 특정 장치 이름으로 시작 (부분 일치 가능)
winload --title "My Monitor" # 사용자 지정 헤더 제목 사용
winload -e           # TUI에 이모지 장식 활성화 🎉
winload --max-mode smart --max-half-life 10 # 부드러운 적응형 Y축 (기본값)
winload --max-mode legacy # nload 스타일 표시 히스토리 피크 스케일링
winload --max-mode fixed --max-y-value 10M # Y축 상한 고정
winload --npcap      # 127.0.0.1 루프백 트래픽 캡처 (Windows, Npcap 필요)
winload --netlink    # RTNETLINK 수동 활성화（Linux/Android, 기본 꺼짐）
```

### 옵션 상세

| 플래그 | 설명 | 기본값 |
|------|-------------|---------|
| `-t`, `--interval <MS>` | 새로고침 간격 (밀리초 단위) | `500` |
| `-a`, `--average <SEC>` | 평균 계산을 위한 윈도우 시간 (초 단위) | `300` |
| `-d`, `--device <NAME>` | 기본 장치 이름 (부분 일치 가능) | — |
| `--title [TITLE]` | 장치 헤더 위에 제목 줄 추가. 값이 없으면 `winload <version>`을 표시하고, 빈 문자열(또는 생략)이면 기본 장치 헤더만 표시 | — |
| `-e`, `--emoji` | TUI에서 이모지 장식 활성화 🎉 | 비활성 |
| `-U`, `--unicode` | 그래프에 Unicode 블록 문자 사용 (█▓░·) | 비활성 |
| `-u`, `--unit <UNIT>` | 표시 단위: `bit` 또는 `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | 바 스타일: `fill`, `color`, 또는 `plain` | `plain` |
| `--in-color <HEX>` | 수신 그래프 색상, 16진수 RGB (예: `0x00d7ff`) | Cyan |
| `--out-color <HEX>` | 송신 그래프 색상, 16진수 RGB (예: `0xffaf00`) | Gold |
| `--max-mode <MODE>` | Y축 스케일링 모드: `smart`, `legacy`, `fixed` | `smart` |
| `--max-half-life <SECS>` | smart 모드 지수 감쇠 반감기 | `10` |
| `--max-y-value <VALUE>` | fixed 모드 Y축 상한 (예: `10M`, `1G`, `500K`) | — |
| `-n`, `--no-graph` | 그래프를 숨기고 통계만 표시 | 비활성 |
| `--hide-separator` | 구분선(등호 행) 숨기기 | 비활성 |
| `--no-color` | 모든 TUI 색상 비활성화 (흑백 모드) | 비활성 |
| `--npcap` | **[Windows Rust Only]** Npcap을 통해 루프백 트래픽 캡처 | 비활성 |
| `--netlink` | **[Linux/Android Only]** 기본 백엔드 대신 RTNETLINK 사용 (Termux proot distro 또는 제한된 환경용) | 비활성 |
| `--debug-info` | 네트워크 인터페이스 디버그 정보 출력 후 종료 | — |
| `-h`, `--help` | 도움말 출력 (`--help --emoji`로 이모지 버전 확인 가능!) | — |
| `-V`, `--version` | 버전 정보 출력 | — |

> **Y축 스케일링 모드** — 다음 세 가지 시나리오는 상호 배타적입니다:
>
> | 모드 | 플래그 | 동작 |
> |------|--------|------|
> | **smart** | `--max-mode smart --max-half-life 10` | 기본값. 트래픽 급증 시 상승한 뒤 부드럽게 지수 감쇠합니다. |
> | **legacy** | `--max-mode legacy` | nload 스타일로 표시 중인 그래프 히스토리 피크에 따라 자동 스케일링합니다. |
> | **fixed** | `--max-mode fixed --max-y-value 10M` | Y축을 지정한 값으로 고정합니다. |
>
> `--max-y-value`는 `--max-mode fixed`에서만, `--max-half-life`는 `--max-mode smart`에서만 사용할 수 있습니다.

### 키보드 단축키

| 키 | 동작 |
|-----|--------|
| `←` / `→` 또는 `↑` / `↓` | 네트워크 장치 전환 |
| `F3` | 디버그 정보 오버레이 전환 (Minecraft 스타일) |
| `=` | 구분선 표시 여부 전환 |
| `c` | 색상 모드 켜기/끄기 전환 |
| `q` / `Esc` | 프로그램 종료 |

## 🪟 Windows 루프백 (127.0.0.1) 안내

Windows는 표준 API를 통해 루프백 트래픽을 보고하지 못하는 구조적 한계가 있습니다. 이는 [Windows 네트워크 스택의 기능적 결함](docs/win_loopback.md)에 기인합니다.

**Windows에서 루프백 트래픽을 모니터링하려면**, `--npcap` 플래그를 사용하십시오:

```bash
winload --npcap
```

이 기능을 사용하려면 [Npcap](https://npcap.com/#download)이 설치되어 있어야 하며, 설치 과정에서 "Support loopback traffic capture" 옵션이 활성화되어 있어야 합니다.

> 이전에는 Windows 자체의 `GetIfEntry` API를 직접 폴링하는 방식을 시도했으나, 루프백 인터페이스의 카운터는 항상 0으로 나타났습니다. 루프백 가상 인터페이스 뒤에는 데이터를 집계할 NDIS 드라이버가 존재하지 않기 때문입니다. 따라서 해당 코드 경로는 현재 제거되었습니다.

> 📖 Windows 루프백 문제에 대한 기술적인 상세 내용은 [docs/win_loopback.md](docs/win_loopback.md)를 참조하십시오.

## 🐧 Linux / Android / Termux Netlink

Linux 및 macOS에서는 별도의 설정 없이 루프백 트래픽 모니터링이 기본적으로 작동합니다.

**Linux/Android**에서 `/proc/net/dev`에 접근할 수 없는 경우（Termux proot distro 또는 기타 제한된 환경 등），`--netlink`를 사용하여 RTNETLINK를 통해 네트워크 통계를 직접 수집할 수 있습니다：

```bash
winload --netlink
```

> 참고：`--netlink`는 `--npcap`처럼 **수동으로 켜는 선택적 백엔드**이며, 플래그를 지정하지 않으면 활성화되지 않습니다. 일반 Linux/Android 실행은 기본 백엔드(Rust: sysinfo, Python: psutil)를 사용합니다. Python 에디션은 Linux/Android에서 `pyroute2`로 RTNETLINK를 사용합니다. macOS에서는 netlink를 사용할 수 없습니다.
>
> 📖 Linux/Android 네트워크 통계 수집 원리에 대한 자세한 내용은 [docs/linux_android_netlink.md](docs/linux_android_netlink.md)를 참조하십시오

## 🖼️ 미리보기
#### Python 버전 미리보기
![docs/images/preview-py.png](docs/images/preview-py.png)

#### Rust 버전 미리보기
![docs/images/preview-rust.png](docs/images/preview-rust.png)

##### Rust 버전 미리보기 GIF
![docs/images/preview-rust.gif](docs/images/preview-rust.gif)

##### 터미널 녹화
[![asciicast](https://asciinema.org/a/1030894.svg)](https://asciinema.org/a/1030894?t=30)

> ↑ [asciinema](https://github.com/asciinema/asciinema) 로 녹화

## 📦 의존성

### Python 버전

| 패키지 | 버전 | 설명 |
|:---|:---|:---|
| [![Python](https://img.shields.io/badge/Python-3.13.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13.11 | 프로그래밍 언어 |
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | 프로세스 및 시스템 유틸리티 |
| [![pyroute2](https://img.shields.io/badge/pyroute2-≥0.9.6-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/svinota/pyroute2) | ≥0.9.6 | Linux/Android RTNETLINK 백엔드 |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows curses 지원 |

### Rust 버전

| 패키지 | 버전 | 설명 |
|:---|:---|:---|
| [![Rust](https://img.shields.io/badge/Rust-1.93.0-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/) | 1.93.0 | 프로그래밍 언어 |
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | 터미널 UI 프레임워크 |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | 크로스 플랫폼 터미널 라이브러리 |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | 시스템 정보 라이브러리 |
| [![clap](https://img.shields.io/badge/clap-4-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | 명령줄 인자 파서 |
| [![pcap](https://img.shields.io/badge/pcap-2-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | 패킷 캡처 (선택 사항, Windows) |
## 🧭 맺음말

네트워크 트래픽은 무형으로 흐르고, 소리 없이 스쳐갑니다. 그러나 Winload는 그것에 형체를 부여하여, 터미널 위에서 수많은 패킷의 춤을 생생히 펼쳐 보입니다. 한 대의 기계가 숨 쉬는 그물의 맥박을 알고자 할 때, 이 도구는 책상 위의 작은 등불이 되어 주고, 밤바다를 항해하는 이에게 별이 되어 줍니다.

