# Első program: szerkesztés, mentés, futtatás

[Kezdőlap](../../README.md) · [Python-tartalomjegyzék](README.md)

Előfeltétel: a [Windows](vscode-windows.md) vagy [macOS/Linux](macos-linux.md) telepítési útmutató kész. A `.venv` interpreter legyen kiválasztva a VS Code-ban.

## Egy rövid saját fájl

A VS Code-ban hozz létre a projekt gyökerében `elso_proba.py` nevű fájlt. Ezt te készíted, nem része a letöltött fájloknak. Írd bele, majd mentsd:

```python
hossz = 2.5
szelesseg = 4
terulet = hossz * szelesseg
print("Terület:", terulet, "m²")
```

Mindkét hosszúságot méterben értelmezzük. A Python itt puszta számokkal számol; a mértékegységet a megjegyzés és a kiírás közli, nem ellenőrzi automatikusan.

Az `=` értéket rendel egy változóhoz. A `*` szorzás. A `print` az idézőjeles szöveget és a kiszámított értéket kiírja. A tizedespont a Python-kód része: `2,5` más szerkezet lenne.

## Futtatás

Windows PowerShell, a projekt gyökeréből:

```powershell
.\.venv\Scripts\python.exe elso_proba.py
```

macOS/Linux:

```bash
./.venv/bin/python elso_proba.py
```

Elvárt kimenet: `Terület: 10.0 m²`. A VS Code **Run Python File in Terminal** parancsa is használható. A futtatás előtt ments: a program a lemezen lévő fájlt olvassa.

## Módosítás és ellenőrzés

Írd át a hossz értékét `3`-ra. Ments és futtass újra. Előre számold ki fejben az eredményt: most 12 négyzetméter várható. Ha a régi számot látod, ellenőrizd a mentést és azt, melyik fájlt indítottad el.

## Hibaüzenet olvasása

Egy elírt változónév `NameError`, egy hiányzó idézőjel `SyntaxError` hibához vezethet. A Python megadja a fájl és a sor helyét; a hiba utolsó sora nevezi meg a problémát. A behúzásnak is jelentése van: az itt bemutatott sorokat ne húzd beljebb.

A további példákban a `def` egy névvel meghívható műveletsort, azaz függvényt hoz létre. A `return` visszaadja az eredményt. Az `if __name__ == "__main__":` alatti rész közvetlen fájlfuttatáskor indul; a tesztek emiatt importálhatják a számítást anélkül, hogy minden kiírás lefutna.

Következő lépés: [SymPy-alapok](sympy-alapok.md) · [hibakeresés](hibakereses.md).
