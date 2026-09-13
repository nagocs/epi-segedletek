# Javítás és közreműködés

[Kezdőlap](README.md)

Elírást, hibás linket vagy nem követhető telepítési lépést GitHub Issue-ban jelezhetsz. Írd le az operációs rendszert, az érintett útmutatót, a végrehajtott lépést, a várt és tényleges eredményt. Hibaüzenetet szövegként másolj be. Ne tegyél közzé jelszót, aktiválási adatot, NEPTUN-kódot vagy személyes adatot.

A repó célja rövid eszközbemutatók és kezdő útmutatók gyűjtése. Új példa is ezt szolgálja: konkrét tantárgyi házifeladat-megoldás, beadandósablon és előadásanyag ne kerüljön ide. A fájlnevek a témát nevezzék meg. A Python- és Mathematica-változat ugyanazokat az adatokat használja; a magyarázat tartalmazzon várt eredményt és független ellenőrzési szempontot.

## Ellenőrzés fejlesztőknek

A repó gyökerében, a [Python-környezet létrehozása](docs/python/README.md) után:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe scripts/check_links.py
```

macOS/Linux alatt:

```bash
./.venv/bin/python -m unittest discover -s tests -v
./.venv/bin/python scripts/check_links.py
```

A linkellenőrző a helyi célfájlok létezését vizsgálja; külső oldalak elérhetőségét és fejezetazonosítókat nem ellenőriz. A GitHub Actions ugyanezeket a vizsgálatokat Windows és Ubuntu környezetben futtatja push és pull request eseményre.

Mathematica-módosítás után indíts friss kernelt, nyisd meg a mentett notebookot, és felülről lefelé futtasd az összes bemeneti cellát. Vesd össze az eredményt a példa README-jével, ellenőrizd az ábraexportot is. LaTeX-részlet változtatása után fordítsd le a részletet a jelölt csomagokkal, a hivatkozások miatt kétszer. A telepítési útmutató változását az érintett rendszeren is érdemes végigpróbálni.

Az elvégzett és elmaradt próbákat pontosan rögzítsd az [ellenőrzési jegyzékben](docs/ellenorzes.md); az automatikus Python-teszt nem helyettesíti a Mathematica és az Overleaf kézi próbáját. Függőségfrissítéskor frissítsd a verziókat az útmutatókban is.
