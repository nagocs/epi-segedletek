# Python Windows alatt, VS Code-dal

[Kezdőlap](../../README.md) · [Python-tartalomjegyzék](README.md)

**Cél:** a letöltött példaprogram futtatása a projekt saját Python-környezetében. Szükséged lesz internetre a telepítéshez és a [kicsomagolt repóra](../kezdes.md).

## 1. Python telepítése

Ha a `py -3.14 --version` parancs már Python 3.14-et ír ki, folytathatod a VS Code-dal. Új telepítéshez a [python.org letöltési oldaláról](https://www.python.org/downloads/) telepítsd a **Python Install Manager** eszközt. A hivatalos Windows-útmutató ezt az útvonalat ismerteti.

A Windows Start menüjéből nyiss Terminalt vagy PowerShellt. Az új telepítéskezelővel telepítsd a 3.14-es sorozatot:

```powershell
pymanager install 3.14
py -3.14 --version
```

Az első parancs letölti a Pythont, a második a verzióját mutatja. A javítóverzió eltérhet; a példákat Python 3.14.2-vel ellenőriztük.

Régebbi Python-telepítő mellett a `py` indítóprogram létezhet anélkül, hogy `pymanager` lenne. Egy már működő 3.14-es telepítést nem kell lecserélni. Ha újonnan telepített programot nem talál a parancssor, indíts új terminált. [Python hivatalos Windows-útmutató](https://docs.python.org/3/using/windows.html).

## 2. VS Code és bővítmény

Telepítsd a [VS Code-ot](https://code.visualstudio.com/Download). Az Extensions panelen (`Ctrl+Shift+X`) telepítsd a Microsoft **Python** bővítményét, azonosítója `ms-python.python`. A szerkesztő és a bővítmény nem helyettesíti a Python futtatóprogramját.

Válaszd a **File → Open Folder** menüt, és a repó gyökerét nyisd meg. A bal oldalon látszódjon a `requirements.txt` és a `peldak` mappa. Indíts új terminált a **Terminal → New Terminal** menüvel; a következő parancsok ehhez a mappához viszonyítottak.

## 3. Saját virtuális környezet

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

A `.venv` egy új mappa lesz a projekten belül, saját Pythonnal és csomagokkal. A `-m venv` a környezetkészítő modult futtatja. A második parancs a **környezet saját Pythonjával** telepíti a felsorolt csomagokat. Az `-r` azt jelenti: a telepítendők listáját fájlból olvassa.

A csomagtelepítéshez közvetlenül a környezet Pythonját hívjuk, ezért nincs szükség `Activate.ps1` futtatására vagy PowerShell-házirend módosítására. A letöltés végén nem lehet piros telepítési hiba. Ellenőrizd:

```powershell
.\.venv\Scripts\python.exe -c "import sympy, numpy, matplotlib; print(sympy.__version__, numpy.__version__, matplotlib.__version__)"
```

Elvárt kimenet a rögzített csomaglistával:

```text
1.14.0 2.4.1 3.10.8
```

## 4. Interpreter kiválasztása a VS Code-ban

Nyomd meg a `Ctrl+Shift+P` kombinációt, keresd a **Python: Select Interpreter** parancsot. Válaszd a projekt `.venv` környezetét. Ha nincs a listában, az **Enter interpreter path** lehetőséggel tallózd ki a `.venv\Scripts\python.exe` fájlt. Ez határozza meg, mivel fut a szerkesztőből indított Python-fájl.

## 5. Futtatás a VS Code-ban

1. A bal oldali Explorerben nyisd meg a `peldak/01-masodfoku-egyenlet/masodfoku_egyenlet.py` fájlt.
2. Mentsd el (`Ctrl+S`).
3. A szerkesztő jobb felső sarkában kattints a **Run Python File** háromszögre. A mellette lévő lenyíló menüben a **Run Python File in Terminal** műveletet válaszd, ha több futtatási lehetőség látszik.
4. Az eredmény az alsó **Terminal** panelen jelenik meg, a kiválasztott `.venv` környezetből futtatva.

Ugyanez a szerkesztőben jobb kattintással, a **Run → Python File in Terminal** menüből is elérhető.

A gyökök `[1/2, 2]`, a visszahelyettesítési maradékok `[0, 0]` lesznek. A program a példamappán belüli `kimenet` mappába ment egy PDF-et és egy PNG-t; a teljes helyet kiírja. Nem nyit automatikusan ábraablakot.

Következő lépés: [első saját program](elso-program.md) · [Python-hibakeresés](hibakereses.md).

Forrás: [VS Code Python-útmutató](https://code.visualstudio.com/docs/python/python-tutorial).
