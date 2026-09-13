# Kezdés: a segédlet letöltése és használata

[Kezdőlap](../README.md)

A GitHub itt egy fájlgyűjtemény és olvasható útmutató. A `README.md` az adott mappa magyarázó oldala; a `.md` a Markdown szövegformátum kiterjesztése. Kattints a linkekre: nem kell sorban minden oldalt elolvasnod.

## 1. Letöltés

1. Nyisd meg a [repó kezdőlapját](https://github.com/nagocs/epi).
2. A fájllista felett válaszd a **Code**, majd a **Download ZIP** lehetőséget.
3. A letöltött ZIP-en Windowson jobb kattintás → **Az összes kibontása**. macOS-en dupla kattintással, Linuxon az archívumkezelővel csomagold ki.
4. Nyisd meg a kicsomagolt mappát. Abban a mappában dolgozz, ahol a `README.md`, a `requirements.txt`, a `docs` és a `peldak` látszik. Ezt nevezzük a **projekt gyökerének**.

Ne az archívumon belül indítsd el a programokat. A ZIP nem rendes munkamappa. Ha a repóhoz még csak meghívással van hozzáférésed, a letöltés előtt jelentkezz be a meghívott GitHub-fiókkal. Nyilvános repó letöltéséhez nincs szükség fiókra.

## 2. Melyik fájl mire való?

| Fájl vagy mappa | Szerep |
| --- | --- |
| `docs/` | Telepítési és használati leírások |
| `peldak/` | Rövid matematikai eszközbemutatók |
| `.py` fájl | Python-program; a Python futtatja |
| `.nb` fájl | Mathematica-notebook; a Mathematica nyitja meg |
| `requirements.txt` | A Python-példákhoz szükséges csomagok és verzióik |
| `.vscode/` | Ajánlott bővítmények és közös szerkesztőbeállítások |

Windows Fájlkezelőben kapcsold be a fájlnévkiterjesztések megjelenítését a **Nézet / Megjelenítés** környékén. Így nem hozol létre véletlenül `proba.py.txt` nevű szövegfájlt.

## 3. A mappa megnyitása VS Code-ban

A VS Code-ban **File → Open Folder** segítségével a projekt gyökerét nyisd meg. A bal oldali Explorerben látni fogod a fájlokat. A `.vscode/extensions.json` ajánlásokat tartalmaz: a választott útvonalhoz szükséges bővítményt telepítsd. A programok futtatásához engedélyezd a munkamappa használatát, ha a VS Code rákérdez és ellenőrizted, hogy ezt a repót nyitottad meg.

A **Terminal → New Terminal** egy parancsbeviteli panelt nyit. Írj be egy parancsot, majd nyomj Entert. A további Windows-parancsok PowerShellhez, a macOS/Linux-parancsok az ottani shellhez készültek. A Python `>>>` jele más környezetet jelent: oda ne írj telepítési parancsokat. Onnan `exit()` segítségével léphetsz vissza.

## 4. Saját módosítások és frissítés

Kezdetben készíts másolatot a kipróbálandó példafájlról. A letöltött új ZIP-et külön mappába bontsd ki, így a saját változtatásaid megmaradnak. Új kiadásnál a Python-csomagokat az új `requirements.txt` alapján telepítsd. A `.venv` környezetet gépek között ne másold: az útmutató alapján újra létrehozható.

Ha már ismered a Gitet, a klónozás is használható, de a segédlet követéséhez nem szükséges.

Következő lépés: [eszközválasztás](eszkozvalasztas.md).

Forrás: [GitHub: forrásarchívum letöltése](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives).
