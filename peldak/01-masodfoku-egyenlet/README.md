# Másodfokú egyenlet és grafikon

[Példák](../README.md) · [Python-fájl](masodfoku_egyenlet.py) · [Mathematica-notebook](masodfoku_egyenlet.nb)

A dimenzió nélküli `f(x) = 2x² − 5x + 2` függvény zérushelyeit keressük. Ez a legjobb első példa: a pontos számolás, az ellenőrzés és az ábrázolás is látható benne.

## Futtatás

Windows, a repó gyökeréből:

```powershell
.\.venv\Scripts\python.exe peldak/01-masodfoku-egyenlet/masodfoku_egyenlet.py
```

macOS/Linux:

```bash
./.venv/bin/python peldak/01-masodfoku-egyenlet/masodfoku_egyenlet.py
```

Mathematicában nyisd meg a fenti notebookot, majd haladj felülről lefelé a bemeneti cellákon **Shift+Enter** segítségével. Az export előtt a notebook legyen lemezre mentve, mert a mentési helyét használjuk.

## Mi történik?

1. Létrehozunk egy valós `x` szimbólumot és egy kifejezést. Pythonban a hatvány `**`, Mathematicában `^`.
2. Az `Eq(f, 0)` / `f == 0` egyenletet ad a megoldó eljárásnak.
3. Minden kapott gyököt visszahelyettesítünk az eredeti függvénybe.
4. Ábrázoljuk a függvényt, majd PDF-et és PNG-t mentünk a notebook vagy program melletti `kimenet` mappába.

## Várt eredmény

A két gyök **1/2 és 2**, mindkét visszahelyettesítési maradék **0**. Kézzel is ellenőrizhető: `(2x − 1)(x − 2)` felbontásából ugyanazok a gyökök adódnak. A felfelé nyíló parabola ezeknél az értékeknél metszi a vízszintes tengelyt.

Pythonból `masodfoku_fuggveny.pdf` és `.png`, Mathematicából `masodfoku_fuggveny_mathematica.pdf` és `.png` készül. Az export nem nyit külön ábraablakot Pythonban; a kiírt útvonalon nyisd meg a fájlt. A [grafikon útmutató](../../docs/python/abrakeszites.md) elmagyarázza a rajzolás sorait.

## Próbáld ki

Változtasd az állandó tagot 2-ről 0-ra. Futtatás előtt próbáld szorzattá alakítani az új kifejezést. Ellenőrizd, hogy a kapott gyökök és a grafikon metszéspontjai egyeznek. Ha összetettebb példán dolgozol, a grafikon csak szemléltetés: a mintavételezés önmagában nem bizonyítja a gyökök teljességét.
