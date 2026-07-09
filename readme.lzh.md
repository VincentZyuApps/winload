![winload](https://socialify.git.ci/VincentZyu233/winload/image?custom_language=Rust&description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F250448479%3Fs%3D200%26v%3D4&name=1&owner=1&pulls=1&stargazers=1&theme=Auto)
![onefetch](docs/images/onefetch.png)

# Winload <img src="docs/images/miku.png" height="32px">

> 輕若飛鴻，疾若奔雷；居終端之一隅，而觀網脈之往來。其意取自 Linux 之 `nload`，而為今世諸機所用。

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

> **[📖 構築之書](.github/workflows/build.zh-cn.md)**

## 🚀 序
`Winload` 者，終端中觀網流之器也。初生於 Windows，欲補 `nload` 不能行於其上之闕；今則兼濟 Linux、macOS，亦及諸架構。

## 🙏 謝
Winload 之靈感，承 Roland Riegel 之經典「[nload](https://github.com/rolandriegel/nload)」。前賢鑿井，後人飲水；其構想與體驗，皆為此器開山之石。
https://github.com/rolandriegel/nload

## ✨ 要義
- **雙本並行**
	- **Rust 本**：迅疾、安穩、內存無虞，且可成一靜態二進制，日常巡網最宜。
	- **Python 本**：易改易拓，若欲試新意、接旁器、作雛形，取之甚便。
- **橫行諸臺**：Windows、Linux、macOS（x64 & ARM64）皆可用。
- **即時成圖**：入流出流，頃刻見其高下；吞吐之數，如觀潮汐。
- **界面清簡**：承 `nload` 舊風，不事繁飾，而所需皆在。

## 📊 功力校驗
> ⚡ Winload（Rust）可得 **約 10ms 啟動**，二進制 **小於 2MB**。較 Python 本輕捷甚多，與 C++ nload 之效亦可相頡頏。

![Winload Benchmark](docs/benchmark/benchmark.svg)

## 🔧 自源而行

### Python
```bash
git clone https://github.com/VincentZyuApps/winload.git
# 中土網路若遲，亦可取 Gitee：
# git clone https://gitee.com/vincent-zyu/winload.git
cd winload/python
uv run python -m winload
```

### Rust
```bash
git clone https://github.com/VincentZyuApps/winload.git
cd winload/rust
cargo run --release
cargo run --release -- --help    # 示助
cargo run --release -- --version # 示版
```

## 🐍 Python 本安置
> 💡 **本末之辨**：PyPI 與 GitHub/Gitee 所得者，乃 Python 本。  
> 僅 Cargo 提供 Rust 原始碼供本地編譯。  
> 所有其他套件管理器（Scoop、AUR、npm、APT、RPM）及 GitHub Releases 均提供 **Rust 二進制**。
### Python (pip)
```bash
pip install winload
# uv 之用法亦佳：
# https://docs.astral.sh/uv/getting-started/installation/
# https://gitee.com/wangnov/uv-custom/releases
uv venv --python 3.13
uv pip install winload
uv run winload
uv run python -c "import shutil; print(shutil.which('winload'))"
```

## 📥 Rust 本安置（薦）
### npm（跨平台）
```bash
# 主薦（scoped）
npm install -g @vincentzyuapps/winload
# 佐選（unscoped）
npm install -g winload-rust-bin
# 佐選（GitHub Packages）
npm install -g @vincentzyuapps/winload --registry https://npm.pkg.github.com
# Windows 上以 win-nload 避 System32\winload.exe 之衝
# Linux/macOS 上 winload 與 win-nload 皆可用
# 或徑以 npx 行之
npx @vincentzyuapps/winload
```

> 內置 4 預編二進制：x86_64 & ARM64，遍及 Windows、Linux、macOS。

### Cargo（自源編鑄）
```bash
cargo install winload
cargo install --list
```
### Windows (Scoop)
> 📄 [Scoop Bucket (GitHub)](https://github.com/VincentZyuApps/scoop-bucket/blob/main/bucket/winload.json)
> 📄 [Scoop Bucket (Gitee)](https://gitee.com/vincent-zyu/scoop-bucket/blob/main/bucket/winload.json)
```powershell
scoop bucket add vincentzyu https://github.com/VincentZyuApps/scoop-bucket
# 或取諸 Gitee：
# scoop bucket add vincentzyu https://gitee.com/vincent-zyu/scoop-bucket
scoop update   # 可先手動刷新 bucket
scoop install winload
# 行二進制
win-nload
Get-Command win-nload # Powershell
where win-nload # CMD
```
> 💡 宜用 [Windows Terminal](https://github.com/microsoft/terminal)，其 CJK 字元之渲染較舊版精確，TUI 體驗亦佳。
> ```powershell
> scoop bucket add versions
> scoop install windows-terminal-preview
> wtp
> ```
> 💡 **諸構皆需 Windows 10+**（Rust 1.77+ 已棄 Windows 7/8）。Scoop 與 npm 預設供 **x86_64** 與 **ARM64** 之 **MSVC + Npcap** 構。今延後載入 `wpcap.dll`，可減未用 `--npcap` 時啟動失誤之虞，然回環抓包仍需系統已裝 Npcap。

### Arch Linux (AUR):
```bash
paru -S winload-rust-bin
which winload
```

### Debian & RedHat 系發行版 / Termux（一令而裝）
> 支援 Debian/Ubuntu 及其下游 —— Linux Mint、Pop!_OS、Deepin、統信 UOS 等（apt）

> 支援 Fedora/RHEL 及其下游 —— Rocky Linux、AlmaLinux、CentOS Stream 等（dnf）

> 亦支援 Android 之 Termux（aarch64）

```bash
curl -fsSL https://raw.githubusercontent.com/VincentZyuApps/winload/main/docs/scripts/install/install.sh | bash
which winload
```
> 📄 [觀安裝腳本之源](https://github.com/VincentZyuApps/winload/blob/main/docs/scripts/install/install.sh)

**🇨🇳 Gitee 鏡像（中土下載更速）：**
```bash
curl -fsSL https://gitee.com/vincent-zyu/winload/raw/main/docs/scripts/install/install_gitee.sh | bash
which winload
```
> 📄 [觀 Gitee 安裝腳本之源](https://gitee.com/vincent-zyu/winload/blob/main/docs/scripts/install/install_gitee.sh)

> ⚠️ 上二 `curl ... | bash` 安裝腳本支援 **x86_64 / aarch64** 架構之 **apt**（Debian/Ubuntu）、**dnf**（Fedora/RHEL）或 **Termux**（Android）系統。他方平臺請以 **npm**（`npm install -g @vincentzyuapps/winload`）或 **Cargo**（`cargo install winload`）安裝。

### macOS / Linux（Homebrew）
> 📄 [Homebrew Formula (GitHub)](https://github.com/VincentZyuApps/homebrew-tap/blob/main/Formula/winload.rb)
> 📄 [Homebrew Formula (Gitee)](https://gitee.com/vincent-zyu/homebrew-tap/blob/main/Formula/winload.rb)
> 近版 Homebrew 或須先信第三方 tap formula，然後可裝。
```bash
brew tap vincentzyuapps/tap
brew trust vincentzyuapps/tap
# 或從 Gitee（手動克隆 tap）：
# git clone https://gitee.com/vincent-zyu/homebrew-tap.git "$(brew --prefix)/Library/Taps/vincentzyuapps/homebrew-tap"
brew update && brew install winload
which winload
```
> 💡 Homebrew 支援 **macOS**（Intel 與 Apple Silicon）與 **Linux**（x86_64 與 ARM64）。

<details>
<summary>手動安裝</summary>

**DEB（Debian/Ubuntu）：**
```bash
# 從 GitHub Releases 下載最新 .deb 包
sudo dpkg -i ./winload*.deb
# 或以 apt（自動理依賴）
sudo apt install ./winload*.deb
which winload
```

**RPM（Fedora/RHEL）：**
```bash
sudo dnf install ./winload*.rpm
which winload
```

**或逕自 [GitHub Releases](https://github.com/VincentZyuApps/winload/releases) 下載二進制。**

</details>

## ⌨️ 用法

```bash
winload              # 監所有活網口
winload -t 200       # 置刷新間隔 200ms
winload -d "Wi-Fi"   # 啟時徑定 Wi-Fi 網卡
winload --title "吾監" # 自訂頂標題
winload -e           # 啟 emoji 飾 🎉
winload --max-mode smart --max-half-life 10 # 智適 Y 軸（默）
winload --max-mode legacy # nload 舊式，以可見歷史峰值縮放
winload --max-mode fixed --max-y-value 10M # 固 Y 軸上限
winload --npcap      # 捕 127.0.0.1 回環流（Windows，需 Npcap）
winload --netlink    # 手啟 RTNETLINK（Linux/Android，默關）
```

### 參數

| 參數 | 說明 | 預設 |
|------|------|------|
| `-t`, `--interval <MS>` | 刷新間隔（毫秒） | `500` |
| `-a`, `--average <SEC>` | 均值計算窗（秒） | `300` |
| `-d`, `--device <NAME>` | 預設裝置名（模糊比對） | — |
| `--title [TITLE]` | 裝置標題上增一行：不帶值則示 `winload <版號>`；空字串（或略）則僅示預設裝置標題 | — |
| `-e`, `--emoji` | TUI 中啟 emoji 飾 🎉 | 關 |
| `-U`, `--unicode` | 用 Unicode 方塊字繪圖（█▓░·） | 關 |
| `-u`, `--unit <UNIT>` | 示單位：`bit` 或 `byte` | `bit` |
| `-b`, `--bar-style <STYLE>` | 條樣式：`fill`、`color` 或 `plain` | `plain` |
| `--in-color <HEX>` | 入图形色，十六進 RGB（如 `0x00d7ff`） | 青 |
| `--out-color <HEX>` | 出图形色，十六進 RGB（如 `0xffaf00`） | 金 |
| `--max-mode <MODE>` | Y 軸縮放模式：`smart`、`legacy`、`fixed` | `smart` |
| `--max-half-life <SECS>` | smart 模式指數衰減半衰期 | `10` |
| `--max-y-value <VALUE>` | fixed 模式固定 Y 軸上限（如 `10M`、`1G`、`500K`） | — |
| `-n`, `--no-graph` | 隱圖，僅示統計 | 關 |
| `--hide-separator` | 隱分隔線（等號一行） | 關 |
| `--no-color` | 禁 TUI 色（單色） | 關 |
| `--npcap` | **[Windows Rust Only]** 以 Npcap 捕回環流 | 關 |
| `--netlink` | **[Linux/Android Only]** 以 RTNETLINK 代預設後端（Termux proot distro 或受限境中用） | 關 |
| `--debug-info` | 印網口除錯信息後退 | — |
| `-h`, `--help` | 示助（`--help --emoji` 可得 emoji 版！） | — |
| `-V`, `--version` | 示版號 | — |

> **Y 軸縮放模式**
>
> | 模式 | 參數 | 行為 |
> |------|------|------|
> | **smart** | `--max-mode smart --max-half-life 10` | 默認。流突增則升，後以指數平滑回落。 |
> | **legacy** | `--max-mode legacy` | nload 舊式，依可見圖形窗口峰值自縮放。 |
> | **fixed** | `--max-mode fixed --max-y-value 10M` | Y 軸鎖定為指定值。 |
>
> `--max-y-value` 惟 `--max-mode fixed` 可用；`--max-half-life` 惟 `--max-mode smart` 可用。

### 捷鍵

| 鍵 | 功 |
|----|----|
| `←` / `→` 或 `↑` / `↓` | 切網口 |
| `F3` | 切除錯信息層（Minecraft 風） |
| `=` | 切分隔線顯隱 |
| `c` | 切色開關 |
| `q` / `Esc` | 退 |

## 🪟 Windows 回環流（127.0.0.1）

Windows 不能以標準 API 報回環流——此 [Windows 網棧之缺](docs/win_loopback.zh-tw.md)。

**欲捕回環流於 Windows**，用 `--npcap` 參：

```bash
winload --npcap
```

需裝 [Npcap](https://npcap.com/#download)，裝時勾 "Support loopback traffic capture"。

> 嘗試輪詢 Windows 之 `GetIfEntry` API，然 loopback 計數恆零——loopback 虛口背後無 NDIS 驅以數之。今已去其徑。

> 📖 欲知其詳，請閱 [docs/win_loopback.zh-tw.md](docs/win_loopback.zh-tw.md)

## 🐧 Linux / Android / Termux Netlink

Linux 及 macOS 上，回環流開箱即用，無需他參。

在 **Linux/Android** 上，若 `/proc/net/dev` 不可讀（如 Termux proot distro 或其他受限之境），可以 `--netlink` 參，逕以 RTNETLINK 取網絡之數：

```bash
winload --netlink
```

> 註：`--netlink` 如 `--npcap`，乃手啟之可選後端，默不啟；常規 Linux/Android 仍用預設後端（Rust: sysinfo，Python: psutil）。Python 本於 Linux/Android 以 `pyroute2` 用 RTNETLINK。macOS 無 netlink。
>
> 📖 欲知其詳，請閱 [docs/linux_android_netlink.zh-tw.md](docs/linux_android_netlink.zh-tw.md)

## 🖼️ 一覽
#### Python 本
![docs/images/preview-py.png](docs/images/preview-py.png)

#### Rust 本
![docs/images/preview-rust.png](docs/images/preview-rust.png)

##### Rust 本 GIF
![docs/images/preview-rust.gif](docs/images/preview-rust.gif)

##### 終端錄
[![asciicast](https://asciinema.org/a/1030894.svg)](https://asciinema.org/a/1030894?t=30)

> ↑ 以 [asciinema](https://github.com/asciinema/asciinema) 錄

## 📦 所賴

### Python 本

| 包 | 版 | 說 |
|:---|:---|:---|
| [![Python](https://img.shields.io/badge/Python-3.13.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/) | 3.13.11 | 編程言語 |
| [![psutil](https://img.shields.io/badge/psutil-≥7.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/giampaolo/psutil) | ≥7.0 | 進程及系統工具 |
| [![pyroute2](https://img.shields.io/badge/pyroute2-≥0.9.6-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/svinota/pyroute2) | ≥0.9.6 | Linux/Android RTNETLINK 後端 |
| [![windows-curses](https://img.shields.io/badge/windows--curses-≥2.0-FFD43B?style=flat-square&logo=python&logoColor=white)](https://github.com/zhirui2020/windows-curses) | ≥2.0 | Windows curses 支援 |

### Rust 本

| 包 | 版 | 說 |
|:---|:---|:---|
| [![Rust](https://img.shields.io/badge/Rust-1.93.0-CE422B?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/) | 1.93.0 | 編程言語 |
| [![ratatui](https://img.shields.io/badge/ratatui-0.29-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/ratatui-org/ratatui) | 0.29 | 終端 UI 框架 |
| [![crossterm](https://img.shields.io/badge/crossterm-0.28-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/crossterm-rs/crossterm) | 0.28 | 跨平臺終端庫 |
| [![sysinfo](https://img.shields.io/badge/sysinfo-0.32-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/GuillaumeGomez/sysinfo) | 0.32 | 系統信息庫 |
| [![clap](https://img.shields.io/badge/clap-4-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/clap-rs/clap) | 4 | 命令列參解析器 |
| [![pcap](https://img.shields.io/badge/pcap-2-000000?style=flat-square&logo=rust&logoColor=white)](https://github.com/pcap-parser/pcap) | 2 | 包捕（可選，Windows） |
## 🧭 結語

夫網流無形，而 Winload 使之有象；包行於終端，聲息不驚，卻能令千端萬緒之吞吐，盡呈目前。若欲知一機之網脈，是器可為案上小燈，亦可為夜航之星。

