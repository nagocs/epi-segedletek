# Az első LaTeX-fordítás

[Kezdőlap](../../README.md) · [LaTeX-tartalomjegyzék](README.md)

**Előfeltétel:** [Overleaf-projekt](overleaf.md) vagy működő [helyi telepítés](vscode-windows.md). **Cél:** egy magyar mondat megjelenítése PDF-ben. Ez technikai próba, nem beadandó vagy dokumentumsablon.

## A teljes fordítási próba

Overleafben a `main.tex` tartalmát cseréld le erre. Helyben `forditasi_proba.tex` néven, UTF-8 kódolással mentsd el; a VS Code alapértelmezése megfelelő.

```latex
\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage[magyar]{babel}
\begin{document}
Árvíztűrő tükörfúrógép. Működik a fordítás.
\end{document}
```

A `documentclass` kiválaszt egy általános dokumentumosztályt. A `fontenc` a betűk kódolását, a `babel` a magyar nyelvi működést segíti. A mai LaTeX az UTF-8 forrást alapértelmezetten kezeli. A `begin` és `end` közé kerül a megjelenítendő tartalom. Az előtte lévő rész a preambulum, ide kerülnek a csomagok.

Válaszd a **pdfLaTeX** fordítót. Overleafben **Recompile**, VS Code-ban a parancspalettából **LaTeX Workshop: Build LaTeX project** indítja a fordítást. Helyben parancssorból is kipróbálhatod, a próbafájlt tartalmazó mappában:

```text
latexmk -pdf forditasi_proba.tex
```

## Mit kell látnod?

Egy rövid magyar mondatot, helyes hosszú ő és ű betűkkel. A PDF-előnézet helyben a LaTeX Workshop **View LaTeX PDF file** parancsával nyitható meg. A `.log` és `.aux` fájlok a fordítás munkafájljai; a `.tex` a forrás, a `.pdf` az olvasható eredmény.

Írd át a második mondatot, ments, fordíts újra. Csak akkor sikeres a próba, ha az új mondatot látod. Hibás fordítás után régi PDF is maradhat a mappában.

Következő lépés: [független LaTeX-alapműveletek](alapmuveletek.md) · [hibakeresés](hibakereses.md).

Források: [Overleaf LaTeX-bevezető](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes), [magyar nyelvi támogatás](https://ctan.org/pkg/babel-hungarian).
