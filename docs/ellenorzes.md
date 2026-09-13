# Ellenőrzési jegyzék

[Kezdőlap](../README.md) · [Közreműködés](../CONTRIBUTING.md)

Az útmutatók és a példák 2026. szeptember 13-án készültek. A telepítési leírások hivatalos dokumentációra támaszkodnak; a releváns forrásokat az egyes oldalakon találod. Az egyetemi Mathematica-hozzáférés leírását az oktató által megadott SSO-folyamat egészíti ki.

## Ellenőrzések

Helyi ellenőrzés Windows alatt, külön létrehozott virtuális környezetben: Python **3.14.2**, SymPy **1.14.0**, NumPy **2.4.1**, Matplotlib **3.10.8**. A három közvetlen függőség verzióját a `requirements.txt` rögzíti; a közvetett függőségek nincsenek külön zárolva.

| Vizsgálat | Eredmény |
| --- | --- |
| Öt automatizált Python-teszt | Sikeres: gyökök és faktorizálás; PDF/PNG export; nyomaték és geometriai azonosságok; egyenletrendszer független mátrixos ellenőrzése; deriváltak, integrálok és numerikus kvadratúra |
| Négy Python-program önálló futtatása | Mind sikeres, a programok mappájától eltérő munkamappából is |
| SymPy-alapok útmutató Python-kódblokkjai | Egymás után futtatva sikeresek |
| Helyi Markdown-linkek | 34 oldal, 187 link, nincs hiányzó célfájl |
| LaTeX első próba és hat műveleti részlet | Mind a hét próba kétszer lefordult a helyi MiKTeX pdfLaTeX fordítójával; nincs feloldatlan hivatkozás, hiányzó karakter vagy túllógást jelző Overfull figyelmeztetés |
| Python-grafikon | PDF és PNG létrejött; a PNG feliratai, gyökjelölései és elrendezése vizuálisan ellenőrizve |

A LaTeX-próbák átmeneti fájlokkal készültek; a repóban az útmutatók rövid kódrészletei érhetők el. A helyi MiKTeX-próba nem jelenti a TeX Live telepítési folyamat kipróbálását.

## Kézi ellenőrzést igénylő környezetek

- **Mathematica:** a helyi Wolfram 14.1 kernel licencaktiválási hibát jelzett, ezért a notebookokat nem sikerült valódi Mathematica-kernelben futtatni. A Python-változatok ellenőrzése a notebookok végrehajthatóságát nem igazolja. Aktivált gépen friss kernellel, felülről lefelé kell kipróbálni a négy notebookot, az elsőnél az exportot is.
- **Egyetemi SSO:** az útmutató az oktatói tájékoztatást követi. Hallgatói fiókkal a teljes belépés és jogosultságkiadás nem lett végigpróbálva.
- **Overleaf:** fiókba belépve a teljes böngészős munkafolyamat nem lett végigpróbálva. A helyi LaTeX-fordítás külön ellenőrzés.
- **Telepítések:** új Windows-, macOS- és Linux-gépen nem történt teljes telepítési próba. A menüpontok és a telepítők felülete később változhat.

A GitHub Actions futásai a repó **Actions** lapján láthatók. A zöld Python-futás az ott felsorolt automatizált ellenőrzésekre vonatkozik.
