![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> 轻量级实时终端网络流量监控工具，灵感来自 Linux 的 nload。

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

> **[📖 构建文档](.github/workflows/build.zh-cn.md)**

## 🚀 简介
`Winload` 是一个直观的终端网络流量监控工具。最初为 Windows 打造，弥补 `nload` 在 Windows 上的空白，现已支持 Linux 和 macOS。

## 🙏 致谢
Winload 的灵感来自 Roland Riegel 的经典 「[nload](https://github.com/rolandriegel/nload)」 项目，感谢原作者的创意与体验。
https://github.com/rolandriegel/nload

## ✨ 主要特性
- **双实现版本**
	- **Rust 版**: 快速、内存安全、单静态二进制文件，适合日常监控。
	- **Python 版**: 易于修改和扩展，适合原型开发或集成。
- **跨平台**: Windows、Linux、macOS（x64 & ARM64）。
- **实时可视化**: 实时上行/下行流量图和吞吐量统计。
- **简洁界面**: 干净的 TUI，沿袭 nload 的人体工程学设计。

## 📊 性能基准测试
> ⚡ Winload (Rust) 实现 **~10ms 启动速度** 和 **<2MB 二进制体积**，在效率上显著优于 Python 并与 C++ nload 相当。

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🔧 从源码运行

### Python
```bash
git clone https://github.com/VincentZyuApps/winload.git
# 或从 Gitee 克隆（中国大陆更快）：
# git clone https://gitee.com/vincent-zyu/winload.git
cd winload/python
uv run python -m winload
```

### Rust
```bash
git clone https://github.com/VincentZyuApps/winload.git
cd winload/rust
cargo run --release
cargo run --release -- --help    # 显示帮助
cargo run --release -- --version # 显示版本
```

## 🐍 Python 版本安装
> 💡 **实现说明**：仅 PyPI 和 GitHub/Gitee 源代码是 Python 版本。  
> 仅 Cargo 提供 Rust 源码供本地编译。  
> 所有其他包管理器（Scoop、AUR、npm、APT、RPM）及 GitHub Releases 均提供 **Rust 二进制文件**。
### Python (pip)
```bash
pip install winload
# 推荐使用 uv：
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv --python 3.13
uv pip install winload
uv run winload
uv run python -c "import shutil; print(shutil.which('winload'))"
```

## 📥 Rust 版本安装（推荐）
### npm (跨平台)
```bash
# 推荐（scoped）
npm install -g @vincentzyuapps/winload
# 备选（unscoped）
npm install -g winload-rust-bin
# 备选（GitHub Packages）
npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
# 在 Windows 上使用 win-nload 以避免与 System32\winload.exe 冲突
# 在 Linux/macOS 上，winload 和 win-nload 均可使用
# 或直接使用 npx
npx @vincentzyuapps/winload
```

> 包含 4 个预编译二进制文件：x86_64 & ARM64 版本，支持 Windows、Linux 和 macOS。

### Cargo (源码编译)
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop)
> 📄 [Scoop Bucket (GitHub)](https://github.com/VincentZyuApps/scoop-bucket/blob/main/bucket/winload.json)
> 📄 [Scoop Bucket (Gitee)](https://gitee.com/vincent-zyu/scoop-bucket/blob/main/bucket/winload.json)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
# 或从 Gitee 克隆：
# scoop bucket add vincentzyu https://gitee.com/vincent-zyu/scoop-bucket
scoop update   # optional: 提前手动更新 bucket 列表
scoop install winload
# 执行二进制文件
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 推荐使用 [Windows Terminal](https://github.com/microsoft/terminal) 而非旧版 Windows Console，以获得正确的中文字符渲染和更好的 TUI 体验。
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```
> 💡 **所有构建均需 Windows 10+**（Rust 1.77+ 已放弃支持 Windows 7/8）。Scoop 和 npm 默认提供 **x86_64** 和 **ARM64** 的 **MSVC + Npcap** 构建。这些构建现在会延迟加载 `wpcap.dll`，可降低未使用 `--npcap` 前的启动失败风险，但回环抓包仍然需要系统已安装 Npcap。

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Debian & RedHat 系发行版 / Termux（一键安装脚本）
> 支持 Debian/Ubuntu 及其下游 —— Linux Mint、Pop!_OS、Deepin、统信 UOS 等 (apt)

> 支持 Fedora/RHEL 及其下游 —— Rocky Linux、AlmaLinux、CentOS Stream 等 (dnf)

> 也支持 Android 上的 Termux (aarch64)

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash
which winload
```
> 📄 [查看安装脚本源码](https://github.com/VincentZyuApps/winload/blob/main/docs/scripts/install/install.sh)

**🇨🇳 Gitee 镜像（大陆地区下载更快）：**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash
which winload
```
> 📄 [查看 Gitee 安装脚本源码](https://gitee.com/vincent-zyu/winload/blob/main/docs/scripts/install/install_gitee.sh)

> ⚠️ 以上两个 `curl ... | bash` 安装脚本支持 **x86_64 / aarch64** 架构上使用 **apt**（Debian/Ubuntu）、**dnf**（Fedora/RHEL）或 **Termux**（Android）的系统。其他平台请使用 **npm**（`npm install -g @vincentzyuapps/winload`）或 **Cargo**（`cargo install winload`）安装。

### macOS / Linux（Homebrew）
> 📄 [Homebrew Formula (GitHub)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)
> 📄 [Homebrew Formula (Gitee)](https://gitee.com/vincent-zyu/homebrew-tap/blob/main/Formula/winload.rb)
> 较新的 Homebrew 可能要求先信任第三方 tap 的 formula 后再安装。
```bash
brew tap vincentzyuapps/tap
brew trust vincentzyuapps/tap
# 或从 Gitee（手动克隆 tap）：
# git clone https://gitee.com/vincent-zyu/homebrew-tap.git "$(brew --prefix)/Library/Taps/vincentzyuapps/homebrew-tap"
brew update && brew install winload
which winload
```
> 💡 Homebrew 支持 **macOS**（Intel 和 Apple Silicon）和 **Linux**（x86_64 和 ARM64）。

<details>
<summary>手动安装</summary>

**DEB (Debian/Ubuntu):**
```bash
# 从 GitHub Releases 下载最新 .deb 包
sudo dpkg -i ./winload*.deb
# 或使用 apt（自动处理依赖）
sudo apt install ./winload*.deb
which winload
```

**RPM (Fedora/RHEL):**
```bash
sudo dnf install ./winload*.rpm
which winload
```

**或者直接从 [GitHub Releases](https://github.com/VincentZyuApps/winload/releases) 下载二进制文件。**

</details>

## ⌨️ 用法

```bash
winload              # 监控所有活跃网络接口
winload -t 200       # 设置刷新间隔为 200ms
winload -d "Wi-Fi"   # 启动时定位到 Wi-Fi 网卡
winload --title "我的监视器" # 使用自定义顶部标题
winload -e           # 启用 emoji 装饰 🎉
winload --max-mode smart --max-half-life 10 # 平滑自适应 Y 轴（默认）
winload --max-mode legacy # nload 风格的可见历史峰值缩放
winload --max-mode fixed --max-y-value 10M # 固定 Y 轴上限
winload --npcap      # 捕获 127.0.0.1 回环流量 (Windows，需安装 Npcap)
winload --netlink    # 手动启用 RTNETLINK（Linux/Android，默认关闭）
```

### 参数选项

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-t`, `--interval <MS>` | 刷新间隔（毫秒） | `500` |
| `-a`, `--average <SEC>` | 平均值计算窗口（秒） | `300` |
| `-d`, `--device <NAME>` | 默认设备名（模糊匹配） | — |
| `--title [TITLE]` | 在设备标题上方添加标题行：不带值时显示 `winload <版本号>`；空字符串（或省略）时仅显示默认设备标题 | — |
| `-e`, `--emoji` | 启用 emoji 装饰 🎉 | 关闭 |
| `-U`, `--unicode` | 使用 Unicode 方块字符绘图（█▓░·） | 关闭 |
| `-u`, `--unit <UNIT>` | 显示单位：`bit` 或 `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | 状态栏样式：`fill`、`color` 或 `plain` | `plain` |
| `--in-color <HEX>` | 下行图形颜色，十六进制 RGB（如 `0x00d7ff`） | 青色 |
| `--out-color <HEX>` | 上行图形颜色，十六进制 RGB（如 `0xffaf00`） | 金色 |
| `--max-mode <MODE>` | Y 轴缩放模式：`smart`、`legacy` 或 `fixed` | `smart` |
| `--max-half-life <SECS>` | smart 模式指数衰减半衰期 | `10` |
| `--max-y-value <VALUE>` | fixed 模式固定 Y 轴上限（如 `10M`、`1G`、`500K`） | — |
| `-n`, `--no-graph` | 隐藏图形，仅显示统计信息 | 关闭 |
| `--hide-separator` | 隐藏分隔线（等于号一行） | 关闭 |
| `--no-color` | 禁用所有 TUI 颜色（单色模式） | 关闭 |
| `--npcap` | **[Windows Rust Only]** 通过 Npcap 捕获回环流量（推荐） | 关闭 |
| `--netlink` | **[Linux/Android Only]** 使用 RTNETLINK 替代默认后端（在 Termux proot distro 或受限环境中适用） | 关闭 |
| `--debug-info` | 打印网络接口调试信息后退出 | — |
| `-h`, `--help` | 打印帮助（`--help --emoji` 可查看 emoji 版！） | — |
| `-V`, `--version` | 打印版本号 | — |

> **Y 轴缩放模式**
>
> | 模式 | 参数 | 行为 |
> |------|------|------|
> | **smart** | `--max-mode smart --max-half-life 10` | 默认。流量突增时立即跳升，随后平滑指数回落。 |
> | **legacy** | `--max-mode legacy` | nload 风格，按当前可见图形窗口峰值自动缩放。 |
> | **fixed** | `--max-mode fixed --max-y-value 10M` | Y 轴锁定为指定值。 |
>
> `--max-y-value` 仅可用于 `--max-mode fixed`；`--max-half-life` 仅可用于 `--max-mode smart`。

### 快捷键

| 按键 | 功能 |
|------|------|
| `←` / `→` 或 `↑` / `↓` | 切换网络设备 |
| `F3` | 切换调试信息界面（Minecraft 风格） |
| `=` | 切换分隔线的显示/隐藏 |
| `c` | 切换颜色开/关 |
| `q` / `Esc` | 退出 |

## 🪟 Windows 回环流量 (127.0.0.1)

Windows 无法通过标准 API 报告回环流量——这是 [Windows 网络栈的功能缺失](docs/win_loopback.zh-cn.md)。

**要在 Windows 上捕获回环流量**，使用 `--npcap` 参数：

```bash
winload --npcap
```

需要安装 [Npcap](https://npcap.com/#download)，安装时勾选 "Support loopback traffic capture"。

> 我之前尝试过直接轮询 Windows 自带的 `GetIfEntry` API，但 loopback 的计数器始终为 0——loopback 伪接口背后根本没有 NDIS 驱动在计数。该代码路径已被移除。

> 📖 深入了解 Windows 回环为何失效，请阅读 [docs/win_loopback.zh-cn.md](docs/win_loopback.zh-cn.md)

## 🐧 Linux / Android / Termux Netlink

在 Linux 和 macOS 上，回环流量开箱即用，无需额外参数。

在 **Linux/Android** 上，如果无法访问 `/proc/net/dev`（例如在 Termux proot distro 或其他受限环境中），可使用 `--netlink` 通过 RTNETLINK 直接收集网络统计信息：

```bash
winload --netlink
```

> 注意：`--netlink` 和 `--npcap` 一样是**手动启用的可选后端**，默认不会启用；普通 Linux/Android 仍使用默认后端（Rust：sysinfo，Python：psutil）。Python 版在 Linux/Android 上通过 `pyroute2` 使用 RTNETLINK。macOS 不支持 netlink。
>
> 📖 深入了解 Linux/Android 网络统计采集原理，请阅读 [docs/linux_android_netlink.zh-cn.md](docs/linux_android_netlink.zh-cn.md)

## 🖼️ 预览
#### Python 版预览
![docs/images/preview-py.png](docs/images/preview-py.png)

#### Rust 版预览
![docs/images/preview-rust.png](docs/images/preview-rust.png)

##### Rust 版预览 GIF
![docs/images/preview-rust.gif](docs/images/preview-rust.gif)

##### 终端录制
[![asciicast](https://asciinema.org/a/1030894.svg)](https://asciinema.org/a/1030894?t=30)

> ↑ 使用 [asciinema](https://github.com/asciinema/asciinema) 录制

## 📦 依赖

### Python 版本

| 包 | 版本 | 说明 |
|:---|:---|:---|
| [![Python](https://img.shields.io/badge/Python-3.13.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13.11 | 编程语言 |
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | 进程和系统工具 |
| [![pyroute2](https://img.shields.io/badge/pyroute2-≥0.9.6-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/svinota/pyroute2) | ≥0.9.6 | Linux/Android 上的 RTNETLINK 后端 |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows curses 支持 |

### Rust 版本

| 包 | 版本 | 说明 |
|:---|:---|:---|
| [![Rust](https://img.shields.io/badge/Rust-1.93.0-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/) | 1.93.0 | 编程语言 |
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | 终端 UI 框架 |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | 跨平台终端库 |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | 系统信息库 |
| [![clap](https://img.shields.io/badge/clap-4-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | 命令行参数解析器 |
| [![pcap](https://img.shields.io/badge/pcap-2-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | 数据包捕获（可选，Windows） |
## 🧭 结语

网络流量本是无形无影之物，而 Winload 却能让它具象于眼前。数据包在终端中穿行，无声无息，却能将千丝万缕的吞吐之状尽数呈现。若你想读懂一台机器的网络脉搏，此工具既可作案头的一盏小灯，也可作夜航时的一颗星。

