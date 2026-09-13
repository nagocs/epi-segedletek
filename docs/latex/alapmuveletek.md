# LaTeX-alapműveletek rövid részleteken

[Kezdőlap](../../README.md) · [LaTeX-tartalomjegyzék](README.md)

Előbb végezd el az [első fordítást](elso-forditas.md). Az alábbi részletek külön kipróbálható műveletek: a **preambulum** kódját a `\begin{document}` elé, a **törzs** kódját a dokumentum kezdete és vége közé illeszd. A csomagbetöltéseket ne másold be többször.

## Bekezdés és címsor

Törzs:

```latex
\section{Jelölések}
Ez az első bekezdés.

Ez a második bekezdés. Egy \emph{fontos szó} kiemelhető.
```

Az üres sor új bekezdést kezd. A szerkesztőben egyszer megnyomott Enter általában szóközként jelenik meg. A `\section` számozott címsort készít; nem kell kézzel beírnod az előtte álló számot. A `\\` sorváltás nem általános bekezdésformázó eszköz.

## Képlet és egyenlethivatkozás

Preambulum:

```latex
\usepackage{amsmath}
```

Törzs:

```latex
A függvény: \(f(x)=x^2\). A deriváltját a
\eqref{eq:derivalt} egyenlet mutatja.
\begin{equation}
  f'(x)=2x.
  \label{eq:derivalt}
\end{equation}
```

A `\(...\)` soron belüli matematikai mód. Az `equation` külön sorba szedi és számozza a képletet. A `label` belső nevet ad neki, az `eqref` ezt alakítja számmá. Kétszeri fordítás után a hivatkozás nem `??`, hanem az egyenlet száma. Számozás nélküli kiemelt képlethez `\[...\]` is használható. A változók jelentését szövegben definiáld.

## Mértékegység

Preambulum:

```latex
\usepackage{siunitx}
\sisetup{output-decimal-marker={,}}
```

Törzs:

```latex
A próbatest hossza \qty{2.5}{\metre}.
A sebesség \qty{3.2}{\metre\per\second}.
```

A bemenetben pont szerepel, a dokumentum a beállítás miatt tizedesvesszőt ír. A csomag gondoskodik a szám és az álló mértékegység közötti megfelelő közről. A `qty` a siunitx 3 parancsa; régi csomagnál frissítés kellhet. [siunitx dokumentáció](https://ctan.org/pkg/siunitx).

## Ábra és képaláírás

Előfeltétel: legyen egy saját `grafikon.png` fájlod a `.tex` mellett. Overleafben előbb töltsd fel. A [Python ábrakészítési útmutató](../python/abrakeszites.md) megmutatja, hogyan készül kép; gyakorláshoz bármely saját kis PNG is megfelelő.

Preambulum:

```latex
\usepackage{graphicx}
```

Törzs:

```latex
Az ábrázolást a \ref{fig:grafikon}. ábra mutatja.
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.7\linewidth]{grafikon.png}
  \caption{A vizsgált függvény grafikonja.}
  \label{fig:grafikon}
\end{figure}
```

Az ábra alatti `caption` feliratot ad; a `label` a felirat után álljon. A `width` a rendelkezésre álló szélességhez igazít. A `[htbp]` elhelyezési lehetőségeket kér: a LaTeX másik megfelelő helyre is teheti az ábrát. A feliratban nevezd meg, mit ábrázolsz. Ha PNG helyett saját PDF-et használsz, a fájlnevet is írd át. A PDF kiterjesztés önmagában nem garantál vektoros tartalmat.

## Táblázat

Törzs, külön csomag nélkül:

```latex
\begin{table}[htbp]
  \centering
  \caption{Két szemléltető adat.}
  \label{tab:adatok}
  \begin{tabular}{lr}
    Jel & Érték \\
    \hline
    A & 2 \\
    B & 5 \\
  \end{tabular}
\end{table}
Az adatokat a \ref{tab:adatok}. táblázat foglalja össze.
```

Az `l` balra, az `r` jobbra igazított oszlopot jelent. Az `&` az oszlopok között, a `\\` a sorok végén áll. Itt a táblázatfelirat felül van. Fizikai adatoknál az egységet is tüntesd fel, például az oszlopfejben.

## Egyszerű forráshivatkozás

Az alábbi kis próba nem igényel külön bibliográfiai fájlt vagy programot. Törzs:

```latex
A függvény használatát a dokumentáció ismerteti~\cite{sympy-docs}.
\begin{thebibliography}{9}
  \bibitem{sympy-docs}
  SymPy Development Team: SymPy Documentation.
  https://docs.sympy.org/ (megtekintve: 2026. szeptember 13.).
\end{thebibliography}
```

A `cite` és `bibitem` azonos kulcsa köti össze a szöveget a forrással. A próba megértése után nagyobb irodalomjegyzékhez külön bibliográfiai eszköz tanulható. A tényleges munkában konkrét oldalra hivatkozz, a saját megtekintési dátumoddal és az előírt stílussal.

## Gyakori különleges karakterek

A százalékjel kommentet kezd; látható százalékhoz `\%` kell. Az aláhúzás matematikában index, normál szövegben `\_` alakban írható. A kapcsos zárójelek parancsargumentumokat fognak közre, párjuknak meg kell lennie. Egyszerre egy részletet változtass, és utána fordíts: így könnyebb megtalálni a hibát.

## További parancsok és gyorsreferenciák

| Hivatkozás | Mit találsz benne? |
| --- | --- |
| [Overleaf: matematikai kifejezések](https://www.overleaf.com/learn/latex/Mathematical_expressions) | Matematikai módok és gyakran használt parancsok, példákkal |
| [Overleaf: LaTeX-tudástár](https://www.overleaf.com/learn) | Tematikus útmutatók képletekhez, táblázatokhoz, ábrákhoz és hivatkozásokhoz |
| [LaTeX cheat sheet – CTAN](https://ctan.org/pkg/latexcheat) | Tömör parancsösszefoglaló; a **Documentation** részből letölthető |

A példáknál figyeld a szükséges csomagokat: a `\usepackage{...}` sorokat a preambulumba kell tenni.

Elakadás esetén: [hibakeresés](hibakereses.md).
