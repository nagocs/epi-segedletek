# Overleaf: LaTeX a böngészőben

[Kezdőlap](../../README.md) · [LaTeX-tartalomjegyzék](README.md)

**Cél:** egy saját próbaprojektben átírsz egy mondatot, lefordítod, és letöltöd az eredményt. Ehhez internet, böngésző és Overleaf-fiók kell; Python és helyi TeX-telepítés nem szükséges.

## 1. Fiók és üres projekt

1. Nyisd meg az [Overleafet](https://www.overleaf.com/), regisztrálj vagy jelentkezz be.
2. A projektek oldalán indíts új projektet a **New project** lehetőséggel, és válaszd az üres projektet (**Blank project**). A felület nyelvétől és verziójától a felirat eltérhet.
3. Adj neki tetszőleges nevet, például `LaTeX proba`.
4. A bal oldali fájllistában nyisd meg a `main.tex` fájlt. A forráskód szerkesztéséhez használd a **Code Editor** nézetet, ha nézetválasztót látsz.

A fájllista a projekted fájljait mutatja, a szerkesztőben a kódot írod, a PDF-előnézetben a fordítás eredménye látszik. A kód módosítása és a PDF frissülése külön művelet.

## 2. Első fordítás

Cseréld le a `main.tex` tartalmát az [első fordítás](elso-forditas.md) rövid kódjára. A projekt beállításaiban a fordító legyen **pdfLaTeX**. Kattints a **Recompile** gombra. A PDF-ben az „Árvíztűrő tükörfúrógép. Működik a fordítás.” mondatnak kell megjelennie.

Írd át a második mondatot, majd fordíts újra. A PDF-ben is az új szöveget keresd. Ha az előző eredményt látod, nézd meg a fordítási hibákat: hibás forrás mellett a korábbi PDF is megmaradhat.

## 3. PDF és forrás megőrzése

A PDF-előnézet letöltés gombjával töltsd le az eredményt. Nyisd meg a letöltött fájlt is. A PDF a megjelenített eredmény; a szerkeszthető forrást a projekt tartalmazza. Saját biztonsági másolathoz a projekt menüjében a forrás letöltését is választhatod; ennek eredménye általában ZIP.

Saját kép beillesztéséhez előbb töltsd fel a képfájlt a projekt fájllistájának feltöltés funkciójával. A kódban a feltöltött fájl nevét használd, ne a számítógéped helyi elérési útját. Ezt külön bemutatja az [alapműveletek oldala](alapmuveletek.md).

## Ha nem sikerül

Piros hiba esetén nyisd meg a napló/hiba panelt, és az első hibánál kezdj. Gyakori ok a hiányzó zárójel, a rossz fordító vagy a fel nem töltött kép. A teljes segédlet ZIP-jét ne töltsd fel: ebben Python- és Mathematica-fájlok is vannak, amelyek nem részei a LaTeX-projektednek.

Következő lépés: [LaTeX-alapműveletek](alapmuveletek.md) · [hibakeresés](hibakereses.md).

Források: [Overleaf bevezető](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes), [fordító kiválasztása](https://docs.overleaf.com/getting-started/recompiling-your-project/selecting-a-tex-live-version-and-latex-compiler). A felületet a szolgáltató változtathatja; a lépések az eszközök szerepét is megadják.
