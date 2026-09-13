# LaTeX Windows alatt, VS Code-dal

[Kezdőlap](../../README.md) · [LaTeX-tartalomjegyzék](README.md)

**Cél:** a saját gépeden egy `.tex` fájlból PDF-et készítesz. Három összetevő dolgozik együtt:

| Összetevő | Feladat |
| --- | --- |
| TeX Live | A fordító és a LaTeX-csomagok |
| Visual Studio Code | A forrásfájl szerkesztése |
| LaTeX Workshop | A VS Code-ból indított fordítás és PDF-előnézet |

## 1. TeX Live

Ha már van működő TeX Live vagy MiKTeX a gépeden, előbb próbáld ki a 3. pont ellenőrző parancsait. Új telepítéshez a LaTeX Workshop által is javasolt **TeX Live** az alapútvonal.

Nyisd meg a [TeX Live hivatalos oldalát](https://tug.org/texlive/), majd az ottani letöltési/telepítési útmutatót. Windowsra a telepítőt válaszd, indítsd el, és kövesd a telepítő lépéseit. A teljes csomagkészlet jelentős lemezterületet és letöltési időt igényel, de a későbbi hiányzó csomagokkal kevesebb teendőd lesz. Várd meg a sikeres befejezést. Ne válassz Linuxhoz készült parancsokat Windowson.

## 2. Szerkesztő és bővítmény

1. Telepítsd a [Visual Studio Code-ot](https://code.visualstudio.com/Download). Ez külön termék a Visual Studiótól.
2. Indítsd el, és az Extensions panelen (`Ctrl+Shift+X`) keresd a **LaTeX Workshop** bővítményt, James Yu kiadásában; azonosítója `James-Yu.latex-workshop`.
3. Telepítés után zárd be és indítsd újra a VS Code-ot. Ez különösen fontos, ha a TeX-et a szerkesztő futása közben telepítetted.

## 3. Ellenőrzés

A **Terminal → New Terminal** panelbe írd külön-külön:

```powershell
pdflatex --version
latexmk -v
```

Mindkettő verzióinformációt kell kiírjon. A `latexmk` szükség szerint többször is elindítja a fordítást, például a kereszthivatkozások feloldásához. Ha a rendszer nem találja valamelyik parancsot, előbb a telepítést és a PATH-ot ellenőrizd a [hibakeresés](hibakereses.md) alapján.

## 4. Saját fordítási próba

A **File → Open Folder** menüben nyiss meg egy saját próbamappát. Hozz létre benne `forditasi_proba.tex` nevű fájlt, és másold bele az [első fordítás](elso-forditas.md) rövid, elmagyarázott kódját. Mentsd el.

Nyisd meg a parancspalettát (`Ctrl+Shift+P`), majd keresd a **LaTeX Workshop: Build LaTeX project** parancsot. A parancsot a `.tex` fájl aktív szerkesztőlapjáról indítsd. A recept kiválasztásakor a `latexmk` / pdfLaTeX útvonalat használd. A **LaTeX Workshop: View LaTeX PDF file** paranccsal nyisd meg az eredményt. Átírás után mentés és újabb fordítás következik.

Ha a repó mappájában dolgozol, saját próbamappának használhatod a `tmp/latex-proba/` könyvtárat; ez helyi munkafájloknak van fenntartva. A külön megnyitott saját mappában is működik a bővítmény alapbeállítása.

## Ha már MiKTeX-et használsz

A MiKTeX megfelelő alternatíva. Az alapértelmezett `latexmk` recepthez **Perl** is szükséges; ezt például a [Strawberry Perl](https://strawberryperl.com/) biztosítja. A MiKTeX Console-ban keresd meg és telepítsd/frissítsd a szükséges csomagokat. MiKTeX és TeX Live párhuzamos telepítése helyett előbb a meglévőt tedd működőképessé.

Következő lépés: [alapműveletek](alapmuveletek.md) · [hibakeresés](hibakereses.md).

Forrás: [LaTeX Workshop telepítési dokumentáció](https://github.com/James-Yu/LaTeX-Workshop/wiki/Install).
