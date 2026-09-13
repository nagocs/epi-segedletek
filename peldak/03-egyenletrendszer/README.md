# Lineáris egyenletrendszer

[Példák](../README.md) · [Python-fájl](linearis_egyenletrendszer.py) · [Mathematica-notebook](linearis_egyenletrendszer.nb)

Három dimenzió nélküli ismeretlent határozunk meg:

```text
10x + (5/2)y − 5z = 100
 2x − 5y    + 7z = 50
−5x + y     − z  = 1
```

## Futtatás

Windows, a repó gyökeréből:

```powershell
.\.venv\Scripts\python.exe peldak/03-egyenletrendszer/linearis_egyenletrendszer.py
```

macOS/Linux:

```bash
./.venv/bin/python peldak/03-egyenletrendszer/linearis_egyenletrendszer.py
```

Mathematicában a notebook bemeneti celláin felülről lefelé haladj **Shift+Enter** segítségével.

## Miért így írjuk?

Pythonban a `Rational(5, 2)` egzakt törtet ad; a Python önmagában végrehajtott `5/2` művelete lebegőpontos számot adna. Mathematicában az egész számokból írt `5/2` eleve egzakt. A numerikus közelítést a végén kérjük.

A Python `solve(..., dict=True)` szótárak listáját adja. A szótár a változókhoz rendeli a kapott értékeket. Mathematicában a `Solve` helyettesítési szabályokat ad, amelyeket a `/.` operátor alkalmaz. Ennél a rögzített rendszernél egyetlen eredmény van, ezért vesszük a lista első elemét. Ez a lépés más rendszerre csak az eredmény vizsgálata után vihető át: lehet üres lista vagy paraméteres eredmény is.

## Várt eredmény

| Változó | Egzakt érték | Tizedes alak |
| --- | --- | --- |
| x | −133/5 | −26,6 |
| y | −2052/5 | −410,4 |
| z | −1392/5 | −278,4 |

Mindhárom egyenletben a bal oldal mínusz jobb oldal **0**. A negatív értékek ebben az algebrai példában megengedettek. Fizikai alkalmazásban külön vizsgáld, hogy az előjel és a tartomány megfelel-e a modellnek.

## Próbáld ki

Az első egyenlet jobb oldalát változtasd 100-ról 101-re. Figyeld meg, hogy több ismeretlen értéke is módosulhat. Végezd el újra az összes egyenlet visszahelyettesítési ellenőrzését; a régi eredmény kiírása önmagában nem ellenőrzés.
