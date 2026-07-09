![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> Linuxの「nload」にインスパイアされた、軽量でリアルタイムなネットワーク帯域幅およびトラフィック監視用CLIツールです。

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

> **[📖 ビルドドキュメント](.github/workflows/build.md)**

## 🚀 はじめに
`Winload`は、直感的で視覚的なネットワークモニターをモダンなターミナルにもたらします。もともとはWindowsにおける`nload`の代替ツールとして開発が始まりましたが、現在はLinuxやmacOSもサポートしています。

## 🙏 謝辞
Winloadは、Roland Riegel氏によるクラシックなプロジェクト「[nload](https://github.com/rolandriegel/nload)」にインスパイアされています。素晴らしいアイデアとユーザー体験に深く感謝いたします。
https://github.com/rolandriegel/nload

## ✨ 主な特徴
- **2つの実装エディション**
	- **Rust版**: 高速、メモリ安全、単一の静的バイナリ。日常的な監視に最適です。
	- **Python版**: プロトタイプ作成や統合のために、ハックや拡張が容易です。
- **クロスプラットフォーム**: Windows、Linux、macOS (x64 & ARM64) に対応。
- **リアルタイムの可視化**: 送受信トラフィックのライブグラフとスループット統計を表示。
- **ミニマルなUI**: nloadの使い勝手を踏襲したクリーンなTUI（テキストユーザインターフェース）。

## 📊 パフォーマンスベンチマーク
> ⚡ Winload (Rust) は **~10ms の起動時間** と **2MB未満のバイナリサイズ** を達成し、Python版を大幅に上回り、C++製 nload と同等の効率を実現しています。

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🔧 ソースから実行

### Python
```bash
git clone https://github.com/VincentZyuApps/winload.git
# または Gitee からクローン（中国本土で高速）：
# git clone https://gitee.com/vincent-zyu/winload.git
cd winload/python
uv run python -m winload
```

### Rust
```bash
git clone https://github.com/VincentZyuApps/winload.git
cd winload/rust
cargo run --release
cargo run --release -- --help    # ヘルプを表示
cargo run --release -- --version # バージョンを表示
```

## 🐍 Python 版 インストール
> 💡 **実装に関する注記**: PyPI および GitHub/Gitee のソースコードのみが Python 版です。  
> Cargo のみが Rust ソースコードのローカルビルドを提供します。  
> すべて他方のパッケージマネージャー（Scoop、AUR、npm、APT、RPM）および GitHub Releases は **Rust バイナリ** を提供しています。
### Python (pip)
```bash
pip install winload
# uv の使用を推奨：
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv --python 3.13
uv pip install winload
uv run winload
uv run python -c "import shutil; print(shutil.which('winload'))"
```

## 📥 Rust 版 インストール（推奨）
### npm (クロスプラットフォーム)
```bash
# 推奨（scoped）
npm install -g @vincentzyuapps/winload
# 代替（unscoped）
npm install -g winload-rust-bin
# 代替（GitHub Packages）
npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
# Windows では System32\winload.exe との競合を避けるため win-nload を使用
# Linux/macOS では winload と win-nload のどちらも使用可能
# または npx を直接使用
npx @vincentzyuapps/winload
```

> 4つのプリコンパイル済みバイナリを含む：x86_64 & ARM64 対応、Windows・Linux・macOS に対応。

### Cargo (ソースからビルド)
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop)
> 📄 [Scoop Bucket (GitHub)](https://github.com/VincentZyuApps/scoop-bucket/blob/main/bucket/winload.json)
> 📄 [Scoop Bucket (Gitee)](https://gitee.com/vincent-zyu/scoop-bucket/blob/main/bucket/winload.json)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
# または Gitee から：
# scoop bucket add vincentzyu https://gitee.com/vincent-zyu/scoop-bucket
scoop update   # optional: インストール前に bucket を手動更新
scoop install winload
# バイナリファイルを実行
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 レガシーの Windows Console ではなく、[Windows Terminal](https://github.com/microsoft/terminal) の使用を推奨します。CJK 文字の正確なレンダリングとより良い TUI 体験が得られます。
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```
> 💡 **すべてのビルドに Windows 10+ が必要です**（Rust 1.77+ は Windows 7/8 をサポートしなくなりました）。Scoop と npm は既定で **x86_64** および **ARM64** 向けの **MSVC + Npcap** ビルドを提供します。これらのビルドは `wpcap.dll` を遅延読み込みするようになったため、`--npcap` を使う前の起動失敗リスクは下がりましたが、ループバック取得には引き続きシステムに Npcap が必要です。

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Debian & RedHat 系ディストロ / Termux (ワンライナー)
> Debian/Ubuntu およびその派生版（Linux Mint, Pop!_OS, Deepin, UOS等）をサポート (apt)

> Fedora/RHEL およびその派生版（Rocky Linux, AlmaLinux, CentOS Stream等）をサポート (dnf)

> Android の Termux (aarch64) もサポート

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash
which winload
```
> 📄 [インストールスクリプトのソースを表示](https://github.com/VincentZyuApps/winload/blob/main/docs/scripts/install/install.sh)

**🇨🇳 Giteeミラー（中国本土内での高速ダウンロード）：**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash
which winload
```
> 📄 [Giteeインストールスクリプトを表示](https://gitee.com/vincent-zyu/winload/blob/main/docs/scripts/install/install_gitee.sh)

> ⚠️ 上記の2つの `curl ... | bash` インストールスクリプトは、**x86_64 / aarch64** アーキテクチャ上で **apt**（Debian/Ubuntu）、**dnf**（Fedora/RHEL）、または **Termux**（Android）を使用するシステムをサポートしています。その他のプラットフォームでは **npm**（`npm install -g @vincentzyuapps/winload`）または **Cargo**（`cargo install winload`）をご利用ください。

### macOS / Linux（Homebrew）
> 📄 [Homebrew Formula (GitHub)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)
> 📄 [Homebrew Formula (Gitee)](https://gitee.com/vincent-zyu/homebrew-tap/blob/main/Formula/winload.rb)
> 最近の Homebrew では、インストール前にサードパーティ tap の formula を信頼する必要がある場合があります。
```bash
brew tap vincentzyuapps/tap
brew trust vincentzyuapps/tap
# または Gitee から（手動クローン）：
# git clone https://gitee.com/vincent-zyu/homebrew-tap.git "$(brew --prefix)/Library/Taps/vincentzyuapps/homebrew-tap"
brew update && brew install winload
which winload
```
> 💡 Homebrew は **macOS**（Intel および Apple Silicon）と **Linux**（x86_64 および ARM64）をサポートしています。

<details>
<summary>手動インストール</summary>

**DEB (Debian/Ubuntu):**
```bash
# GitHub Releasesから最新の .deb をダウンロード
sudo dpkg -i ./winload*.deb
# または apt を使用（依存関係を自動解決）
sudo apt install ./winload*.deb
which winload
```

**RPM (Fedora/RHEL):**
```bash
sudo dnf install ./winload*.rpm
which winload
```

**または、[GitHub Releases](https://github.com/VincentZyuApps/winload/releases) からバイナリを直接ダウンロードしてください。**

</details>

## ⌨️ 使い方

```bash
winload              # すべてのアクティブなネットワークインターフェースを監視
winload -t 200       # 更新間隔を200ミリ秒に設定
winload -d "Wi-Fi"   # 特定のデバイス名で開始
winload --title "My Monitor" # カスタムヘッダータイトルを使う
winload -e           # 絵文字装飾を有効にする 🎉
winload --max-mode smart --max-half-life 10 # スムーズな適応型 Y 軸（既定）
winload --max-mode legacy # nload 風の表示履歴ピークスケーリング
winload --max-mode fixed --max-y-value 10M # Y 軸上限を固定
winload --npcap      # 127.0.0.1 ループバックトラフィックをキャプチャ (Windows, Npcapが必要)
winload --netlink    # RTNETLINK を手動で有効化（Linux/Android、既定はオフ）
```

### オプション

| フラグ | 説明 | デフォルト |
|------|-------------|---------|
| `-t`, `--interval <MS>` | 更新間隔（ミリ秒） | `500` |
| `-a`, `--average <SEC>` | 平均値計算のウィンドウ時間（秒） | `300` |
| `-d`, `--device <NAME>` | デフォルトのデバイス名（部分一致可） | — |
| `--title [TITLE]` | デバイスヘッダーの上にタイトル行を追加。値なしは `winload <version>`、空文字列（または省略）は既定のデバイスヘッダーのみ表示 | — |
| `-e`, `--emoji` | TUIで絵文字装飾を有効にする 🎉 | オフ |
| `-U`, `--unicode` | グラフにUnicodeブロック文字を使用 (█▓░·) | オフ |
| `-u`, `--unit <UNIT>` | 表示単位: `bit` または `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | バースタイル: `fill`, `color`, `plain` | `plain` |
| `--in-color <HEX>` | 受信グラフの色、16進数RGB (例: `0x00d7ff`) | シアン |
| `--out-color <HEX>` | 送信グラフの色、16進数RGB (例: `0xffaf00`) | ゴールド |
| `--max-mode <MODE>` | Y 軸スケーリングモード：`smart`、`legacy`、`fixed` | `smart` |
| `--max-half-life <SECS>` | smart モードの指数減衰半減期 | `10` |
| `--max-y-value <VALUE>` | fixed モードの Y 軸上限（例：`10M`、`1G`、`500K`） | — |
| `-n`, `--no-graph` | グラフを非表示にし、統計のみを表示 | オフ |
| `--hide-separator` | 区切り線（イコール記号の行）を非表示にする | オフ |
| `--no-color` | すべてのTUIカラーを無効にする（モノクロモード） | オフ |
| `--npcap` | **[Windows Rust Only]** Npcap経由でループバックをキャプチャ | オフ |
| `--netlink` | **[Linux/Android Only]** RTNETLINK を既定バックエンドの代わりに使用（Termux proot distro や制限された環境向け） | オフ |
| `--debug-info` | インターフェースのデバッグ情報を表示して終了 | — |
| `-h`, `--help` | ヘルプを表示 (`--help --emoji` で絵文字版ヘルプ！) | — |
| `-V`, `--version` | バージョンを表示 | — |

> **Y軸スケーリングモード**
>
> | モード | フラグ | 動作 |
> |--------|--------|------|
> | **smart** | `--max-mode smart --max-half-life 10` | 既定。スパイク時に上昇し、その後スムーズに指数減衰します。 |
> | **legacy** | `--max-mode legacy` | nload 風に、表示中のグラフ履歴ピークで自動スケーリングします。 |
> | **fixed** | `--max-mode fixed --max-y-value 10M` | Y 軸を指定値に固定します。 |
>
> `--max-y-value` は `--max-mode fixed` 専用、`--max-half-life` は `--max-mode smart` 専用です。

### キーボードショートカット

| キー | アクション |
|-----|--------|
| `←` / `→` または `↑` / `↓` | ネットワークデバイスを切り替える |
| `F3` | デバッグ情報オーバーレイの切り替え（Minecraft 風） |
| `=` | 区切り線の表示/非表示を切り替える |
| `c` | カラーのオン/オフを切り替える |
| `q` / `Esc` | 終了 |

## 🪟 Windows ループバック (127.0.0.1) について

Windowsの標準的なAPIでは、ループバックトラフィックを正しく報告できません。これは[Windowsのネットワークスタックにおける機能的な制限](docs/win_loopback.md)によるものです。

**Windowsでループバックトラフィックをキャプチャする場合**は、`--npcap` フラグを使用してください：

```bash
winload --npcap
```

これには、セットアップ時に「Support loopback traffic capture（ループバックトラフィックキャプチャのサポート）」を有効にして [Npcap](https://npcap.com/#download) をインストールする必要があります。

> 以前、Windows独自の `GetIfEntry` APIを直接ポーリングする方法を試みましたが、ループバックのカウンタは常に0でした。ループバックの疑似インターフェースの背後には、カウントを行うためのNDISドライバが存在しないためです。そのため、そのコードパスは削除されました。

> 📖 なぜWindowsのループバックが制限されているのかについての詳細は、[docs/win_loopback.md](docs/win_loopback.md) を参照してください。

## 🐧 Linux / Android / Termux Netlink

LinuxおよびmacOSでは、ループバックトラフィックは追加のフラグなしで標準で動作します。

**Linux/Android** で `/proc/net/dev` にアクセスできない場合（Termux proot distro やその他の制限された環境など）、`--netlink` を使用して RTNETLINK 経由でネットワーク統計を直接収集できます：

```bash
winload --netlink
```

> 注：`--netlink` は `--npcap` と同じく**手動で有効化する任意のバックエンド**で、フラグを渡さない限り有効になりません。通常の Linux/Android では既定バックエンド（Rust: sysinfo、Python: psutil）を使用します。Python 版は Linux/Android 上で `pyroute2` により RTNETLINK を使用します。macOS では netlink は利用できません。
>
> 📖 Linux/Android ネットワーク統計収集の詳細は、[docs/linux_android_netlink.md](docs/linux_android_netlink.md) を参照してください

## 🖼️ プレビュー
#### Python版 プレビュー
![docs/images/preview-py.png](docs/images/preview-py.png)

#### Rust版 プレビュー
![docs/images/preview-rust.png](docs/images/preview-rust.png)

##### Rust版 プレビュー GIF
![docs/images/preview-rust.gif](docs/images/preview-rust.gif)

##### ターミナル録画
[![asciicast](https://asciinema.org/a/1030894.svg)](https://asciinema.org/a/1030894?t=30)

> ↑ [asciinema](https://github.com/asciinema/asciinema) で録画

## 📦 依存関係

### Python版

| パッケージ | バージョン | 説明 |
|:---|:---|:---|
| [![Python](https://img.shields.io/badge/Python-3.13.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13.11 | プログラミング言語 |
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | プロセス・システムユーティリティ |
| [![pyroute2](https://img.shields.io/badge/pyroute2-≥0.9.6-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/svinota/pyroute2) | ≥0.9.6 | Linux/Android の RTNETLINK バックエンド |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows カーサポート |

### Rust版

| パッケージ | バージョン | 説明 |
|:---|:---|:---|
| [![Rust](https://img.shields.io/badge/Rust-1.93.0-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/) | 1.93.0 | プログラミング言語 |
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | ターミナルUIフレームワーク |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | クロスプラットフォームターミナルライブラリ |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | システム情報ライブラリ |
| [![clap](https://img.shields.io/badge/clap-4-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | コマンドライン引数パーサー |
| [![pcap](https://img.shields.io/badge/pcap-2-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | パケットキャプチャ（オプション、Windows） |
## 🧭 結語

ネットの流れは形なく、Winload はそれに姿を与える。パケットは端末を行き交い、音もなく、気配もない。しかし、その一つひとつの行き来を、余すところなく目の当たりにすることができる。一つのマシンのネットワークの鼓動を知りたいとき、この道具は机の上の小さな灯火となり、夜を渡る船の星となるのである。

