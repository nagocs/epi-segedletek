# Erő nyomatéka egy pontra

[Példák](../README.md) · [Python-fájl](ero_nyomateka.py) · [Mathematica-notebook](ero_nyomateka.nb)

Az `r_OA = (1, 3, −2) m` helyvektor az O pontból az erő A támadáspontjába mutat. Az erő `F = (100, −300, 150) N`. Jobbsodrású derékszögű koordinátarendszerben az **O pontra** vett nyomaték `M_O = r_OA × F`.

## Futtatás

**Python a VS Code-ban:**

1. Nyisd meg a `ero_nyomateka.py` fájlt a bal oldali Explorerből.
2. A **Python: Select Interpreter** paranccsal válaszd ki a projekt `.venv` környezetét.
3. Mentsd a fájlt, majd a jobb felső **Run Python File** gomb menüjéből válaszd a **Run Python File in Terminal** műveletet.
4. Az eredményt az alsó **Terminal** panelen olvasd.

Mathematicában a fenti notebook bemeneti celláin felülről lefelé haladj **Shift+Enter** segítségével.

## Mit jelentenek a műveletek?

A SymPy `Matrix([1, 3, -2])` oszlopvektort hoz létre; a Mathematica ugyanitt listát használ. A `.cross(...)` / `Cross[...]` vektoriális szorzatot ad. A `.dot(...)` / `Dot[...]` skalárszorzat, amelyet a merőlegesség vizsgálatára használunk.

Az egységeket ebben a rövid példában a megjegyzések és a kiírások rögzítik, a program nem végez automatikus egységátváltást. Minden adatot a megadott egységben kell beírni.

## Várt eredmény és ellenőrzés

`M_O = (−150, −350, −600) N m`. Például az első komponens kézzel: `3·150 − (−2)·(−300) = −150`.

A nyomaték skalárszorzata mind a helyvektorral, mind az erővel nulla. Ez szükséges geometriai ellenőrzés, de önmagában nem igazolja a nagyságot vagy az előjelet. Fordított sorrendben az eredmény `(150, 350, 600)`, vagyis az eredeti ellentettje. A keresztszorzat sorrendje tehát lényeges.
