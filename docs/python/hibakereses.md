# Python-hibakeresés

[Kezdőlap](../../README.md) · [Python-tartalomjegyzék](README.md)

A VS Code-ban a **Python: Select Interpreter** paranccsal válaszd ki a projekt `.venv` környezetét. A futtatógomb ezt a Pythont használja; a csomagtelepítési parancsokat a repó gyökerében nyitott terminálban add ki.

| Jelenség | Teendő |
| --- | --- |
| `py` / `python3.14` nem található | Ellenőrizd a telepítést, nyiss új terminált. Régi Windows launcher és új Install Manager eltéréseit a telepítési útmutató ismerteti. |
| A `pymanager` nem található | Ez az új Python Install Manager parancsa. Már működő 3.14-es telepítés mellett nincs rá szükség; új telepítéshez a hivatalos managert használd. |
| `requirements.txt` nem található | Nem a repó gyökerében állsz. Nyisd meg azt a mappát, amelyben ez a fájl látszik. |
| `.venv/.../python` nem található | Létrehoztad a környezetet ebben a mappában? ZIP-en belül dolgozol? A rendszeredhez való útvonalat használod? |
| `ModuleNotFoundError: sympy` | A csomagok másik Pythonhoz kerülhettek. A `.venv` Pythonjával futtasd a `-m pip install -r requirements.txt` parancsot. |
| Futtatógombbal hiba, terminálból jó | **Python: Select Interpreter** → a projekt `.venv` környezete. |
| `SyntaxError` telepítési parancsnál | A Python `>>>` promptjába írtad? `exit()` után a normál terminálban futtasd. |
| `NameError` | Elírt név, hiányzó import vagy szimbólumdefiníció. Nézd meg a jelzett sort. |
| `TypeError` hatványozásnál | Pythonban `**` a hatvány; a `^` más művelet. |
| Nem jelent meg ábraablak | A példa fájlba ment. Nyisd meg a kiírt `kimenet` útvonalat. |
| PowerShell tiltja az aktiválást | A leírt közvetlen `.venv\Scripts\python.exe` parancsokhoz nem kell aktiváló szkript. |
| `externally-managed-environment` Linuxon | Rendszer-Pythonba próbálsz telepíteni. Hozd létre a `.venv`-et, és a saját Pythonjával telepíts. |
| SSL/tanúsítvány- vagy proxyhiba | Ellenőrizd az internetet és az intézményi hálózat beállítását; ne kapcsold ki a HTTPS-ellenőrzést. macOS python.org-telepítésnél lásd a tanúsítványtelepítési lépést. |
| `No matching distribution` | Ellenőrizd a Python-verziót, a csomag nevét és a hálózati hozzáférést; használd a referencia-környezetet. |

Windowsos diagnosztika, a repó gyökeréből:

```powershell
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable); print(sys.version)"
.\.venv\Scripts\python.exe -m pip --version
```

macOS/Linux alatt a fenti két parancsban `.\.venv\Scripts\python.exe` helyett `./.venv/bin/python` szerepeljen. A kiírt útvonalakban a projekted `.venv` mappáját keresd.

Segítséghez add meg a parancsot és a teljes hibaüzenetet, de a személyes útvonalrészeket kitakarhatod.
