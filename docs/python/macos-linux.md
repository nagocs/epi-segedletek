# Python macOS és Linux alatt, VS Code-dal

[Kezdőlap](../../README.md) · [Python-tartalomjegyzék](README.md)

**Cél:** saját virtuális környezetben elindítani a példákat. Előbb [töltsd le és csomagold ki](../kezdes.md) a repót.

## macOS: Python és VS Code

A [python.org letöltési oldalán](https://www.python.org/downloads/macos/) válassz a gépeddel kompatibilis Python 3.14 telepítőt. Nyisd meg a `.pkg` fájlt, és kövesd a telepítést. A Python telepítési mappájában található `Install Certificates.command` futtatása a python.org-os macOS-telepítésnél segíthet a HTTPS-tanúsítványok beállításában; kövesd a telepítő utasítását. A rendszer saját Pythonját ne módosítsd.

Telepítsd a [VS Code-ot](https://code.visualstudio.com/Download), majd a Microsoft **Python** bővítményt (`ms-python.python`). A **File → Open Folder** segítségével nyisd meg a repót. Új terminálban ellenőrizd:

```bash
python3.14 --version
python3.14 -m venv .venv
```

## Ubuntu / Debian: Python és VS Code

A következő parancsok az adott rendszer csomagtárolójából telepítenek, ezért az elérhető Python-verzió a rendszer kiadásától függ:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 --version
python3 -m venv .venv
```

A környezetkészítő parancsot a repó gyökerében futtasd. A példák referencia-verziója 3.14; ha a disztribúciód mást ad, a csomagtelepítés és az ellenőrző futtatás eredményét is vizsgáld meg. A rögzített NumPy miatt legalább Python 3.11 szükséges. Régebbi rendszernél válassz támogatott újabb Python-telepítést a rendszered hivatalos útmutatója szerint. Ne telepíts projektcsomagokat `sudo pip` segítségével a rendszer Pythonjába.

Telepítsd a [VS Code-ot](https://code.visualstudio.com/Download) és a Microsoft **Python** bővítményt. Más Linux-disztribúción az ottani csomagkezelő megfelelő csomagjait használd.

## Mindkét rendszeren: csomagok és futtatás

A projektgyökérben létrehozott környezethez:

```bash
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python -c "import sympy, numpy, matplotlib; print(sympy.__version__, numpy.__version__, matplotlib.__version__)"
./.venv/bin/python peldak/01-masodfoku-egyenlet/masodfoku_egyenlet.py
```

A verziók: `1.14.0 2.4.1 3.10.8`. A gyökök: `[1/2, 2]`; a visszahelyettesítési maradékok nullák. A grafikon a példamappa `kimenet` almappájában készül el, akkor is, ha nincs grafikus kijelző.

A parancspalettában (**Python: Select Interpreter**) válaszd ki a `.venv/bin/python` fájlt. macOS-en `Cmd+Shift+P`, Linuxon `Ctrl+Shift+P` nyitja a palettát. Ezután a megnyitott `.py` fájl a **Run Python File in Terminal** paranccsal is indítható. Aktiválás nem szükséges a fenti, közvetlen környezeti parancsokhoz.

Következő lépés: [első program](elso-program.md) · [hibakeresés](hibakereses.md).

Források: [Python macOS-útmutató](https://docs.python.org/3/using/mac.html), [virtuális környezetek](https://docs.python.org/3/library/venv.html), [VS Code Python](https://code.visualstudio.com/docs/python/python-tutorial).
