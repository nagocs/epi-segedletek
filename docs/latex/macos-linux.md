# LaTeX macOS és Linux alatt

[Kezdőlap](../../README.md) · [LaTeX-tartalomjegyzék](README.md)

**Cél:** helyi fordítóval és VS Code-dal futtatni az [első fordítási próbát](elso-forditas.md). Ha nem szeretnél helyi rendszert telepíteni, választhatod az [Overleafet](overleaf.md).

## macOS

1. Nyisd meg a [MacTeX hivatalos oldalát](https://tug.org/mactex/), és ellenőrizd a kiadás rendszerkövetelményét. A MacTeX a TeX Live macOS-es csomagolása.
2. Töltsd le a telepítőcsomagot, nyisd meg, és kövesd a telepítőt. A teljes csomagkészlet nagy letöltés lehet.
3. Telepítsd a [VS Code macOS-változatát](https://code.visualstudio.com/Download), és benne a **LaTeX Workshop** bővítményt (`James-Yu.latex-workshop`).
4. Indítsd újra a VS Code-ot. A Terminal panelen ellenőrizd a `pdflatex --version` és `latexmk -v` parancsokat.

Ha nem találja a fordítót, ellenőrizd a MacTeX útmutatója szerinti PATH-beállítást; a TeX programok szokásos belépési útja `/Library/TeX/texbin`. A VS Code-ot is újra kell indítani a környezet frissítéséhez.

## Ubuntu / Debian Linux

A következő parancsok ehhez a disztribúciócsaládhoz tartoznak, és rendszergazdai jogosultságot kérnek. Más rendszeren a saját csomagkezelő megfelelő csomagjait használd.

```bash
sudo apt update
sudo apt install texlive-latex-extra texlive-lang-european texlive-science latexmk
```

A csomagok a LaTeX alapjait, a bemutatott kiegészítőket, az európai nyelvek támogatását és a fordítás automatizálását biztosítják. Telepítsd a [VS Code-ot](https://code.visualstudio.com/Download), majd az Extensions panelről a **LaTeX Workshop** bővítményt. Új terminálban futtasd:

```bash
pdflatex --version
latexmk -v
```

## Fordítás mindkét rendszeren

Nyiss meg egy saját mappát a **File → Open Folder** menüvel. Hozd létre benne az [első fordítási próba](elso-forditas.md) fájlját. A parancspaletta macOS-en `Cmd+Shift+P`, Linuxon `Ctrl+Shift+P`. Indítsd a **LaTeX Workshop: Build LaTeX project**, majd a **View LaTeX PDF file** parancsot. A próba pdfLaTeX fordítót használ.

Elakadás esetén: [hibakeresés](hibakereses.md). Tovább: [alapműveletek](alapmuveletek.md).

Források: [TeX Live](https://tug.org/texlive/), [MacTeX](https://tug.org/mactex/), [LaTeX Workshop](https://github.com/James-Yu/LaTeX-Workshop/wiki/Install). A helyi ellenőrzés hatókörét az [ellenőrzési jegyzék](../ellenorzes.md) rögzíti.
