# Lineáris egyenletrendszer

[Példák](../README.md) · [Python-fájl](linearis_egyenletrendszer.py) · [Mathematica-notebook](linearis_egyenletrendszer.nb)

Három dimenzió nélküli ismeretlent határozunk meg:

```text
10x + (5/2)y − 5z = 100
 2x − 5y    + 7z = 50
−5x + y     − z  = 1
```

## Futtatás

**Python a VS Code-ban:**

1. Nyisd meg a `linearis_egyenletrendszer.py` fájlt a bal oldali Explorerből.
2. A **Python: Select Interpreter** paranccsal válaszd ki a projekt `.venv` környezetét.
3. Mentsd a fájlt, majd a jobb felső **Run Python File** gomb menüjéből válaszd a **Run Python File in Terminal** műveletet.
4. Az eredményt az alsó **Terminal** panelen olvasd.

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
