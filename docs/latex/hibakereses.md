# LaTeX-hibakeresés

[Kezdőlap](../../README.md) · [LaTeX-tartalomjegyzék](README.md)

Először mentsd el a forrást, fordíts, majd a napló **első hibáját** keresd. Egy hiányzó zárójel sok további üzenetet okozhat. A régi PDF jelenléte nem jelenti azt, hogy az új fordítás sikerült.

| Jelenség | Mit ellenőrizz? |
| --- | --- |
| `pdflatex` / `latexmk` nem található, `ENOENT` | A TeX-disztribúció telepítve van-e? Újraindítottad-e a VS Code-ot? A terminálban működik-e a verzióparancs? |
| MiKTeX mellett Perl-hiány | A default `latexmk` recepthez telepíts Perlt, például Strawberry Perlt, és indíts új terminált. |
| `File ...sty not found` | Hiányzó LaTeX-csomag. MiKTeX Console vagy TeX Live csomagkezelő segítségével telepítsd; Overleafben ellenőrizd az elírást. |
| `Undefined control sequence` | Elírt parancs vagy hiányzó csomag; `\qty` esetén siunitx 3 szükséges. |
| `Missing $ inserted` | Matematikai parancs került szöveges módba, vagy aláhúzás szerepel fájlnévben. Használj matematikai módot, illetve `\_` jelet. |
| `Runaway argument` / `... ended ...` | Hiányozhat `}` vagy egy `\end{...}`. A jelzett sor előtti részt is vizsgáld. |
| `File ...png not found` | A kép valóban a projektben van-e? A név, kiterjesztés, kis-/nagybetű és relatív útvonal pontos-e? |
| `??` a hivatkozás | Fordíts újra; a `label`/`ref` kulcsok egyezzenek. Ábránál a `label` a `caption` után legyen. |
| Magyar karakterek hibásak | A fájl UTF-8 legyen, és a próba pdfLaTeX fordítóval, T1 és magyar babel beállítással fusson. |
| Az ábra elmozdul | A `figure` úsztatott elem: a LaTeX elhelyezési szabályokat követ. Próbálj kisebb ábrát és megfelelő `[htbp]` kérést. |
| `Overfull ...` figyelmeztetés | Valami kilóg a sorból vagy oldalból. Nézd meg a PDF-et; rövidíts, törd a hosszú képletet vagy igazíts az ábraméreten. |

Ha a bővítményből nem fordul, próbáld a `.tex` mappájában a `latexmk -pdf forditasi_proba.tex` parancsot. Ha ez sem működik, valószínűleg a TeX-telepítés vagy a forrás a gond. Ha működik, a VS Code kiválasztott projektjét és receptjét vizsgáld.

Segítségkéréshez add meg a rendszert, fordítót, az első hibaüzenetet és a lehető legkisebb reprodukáló kódrészletet. [Hibajelzés](../../CONTRIBUTING.md).
