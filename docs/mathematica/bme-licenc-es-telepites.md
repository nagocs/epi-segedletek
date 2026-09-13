# BME-hallgatói hozzáférés és Mathematica-telepítés

[Kezdőlap](../../README.md) · [Mathematica-tartalomjegyzék](README.md)

**Cél:** saját gépen aktivált Mathematica, amelyben a `2 + 2` számítás 4-et ad. A hallgatói útvonal az oktató által megadott **SSO**, azaz egyszeri intézményi bejelentkezés. Legyen elérhető az egyetemi e-mail-fiókod és az intézményi belépéshez szükséges azonosítás.

## 1. Wolfram University Portal

Nyisd meg a [Wolfram University Portált / SiteInfo oldalt](https://www.wolfram.com/siteinfo/), és add meg az egyetemi e-mail-címedet. A szolgáltatás ez alapján mutatja a kapcsolódó intézményi hozzáférést. Ha intézményi belépőoldalra irányít, a szokásos egyetemi bejelentkezési lépéseket kövesd.

## 2. Wolfram-fiók

Ha már van Wolfram-fiókod, jelentkezz be. Ha nincs, a portál útmutatása alapján hozz létre egyet az egyetemi e-mail-címeddel. Nyisd meg az érkező megerősítő levelet, és igazold az e-mail-címet. E nélkül a következő lépések elakadhatnak.

Ha egy korábbi, magáncímes fiókban nem látszik a hallgatói jogosultság, térj vissza a SiteInfo oldalra az egyetemi címmel. Ne vásárolj új előfizetést csak azért, mert rossz fiókban nem jelenik meg a termék.

## 3. Letöltés

A Wolfram-fiók **My Products** részében keresd a Mathematicát, és válaszd a géped rendszeréhez tartozó letöltést. A termékek az újabb alkalmazásban **Wolfram** néven közös indítóból is elérhetők; a cél a Mathematica jogosultság használata.

Windowsra a Windows-telepítőt, macOS-re a kompatibilis macOS-változatot, Linuxra a Linux-csomagot válaszd. Letöltés előtt ellenőrizd a megadott rendszerkövetelményeket és a szabad lemezterületet.

## 4. Telepítés

- **Windows:** indítsd el a letöltött telepítőt, és kövesd a varázslót. Ha rendszerengedélyt kér, ellenőrizd, hogy a hivatalos Wolfram-telepítőt indítottad.
- **macOS:** nyisd meg a letöltött telepítőlemezképet/csomagot, és kövesd a benne megadott alkalmazástelepítési lépéseket.
- **Linux:** a letöltéshez mellékelt telepítési útmutatót kövesd. Ha `.sh` telepítőt kaptál, azt terminálból, a letöltött fájl pontos nevével indítsd; a telepítési könyvtártól függhet, szükséges-e rendszergazdai jogosultság.

Várd meg a telepítés végét, majd indítsd el az alkalmazást.

## 5. Aktiválás SSO-val

Az aktiválási ablakban kövesd a **bejelentkezéses / intézményi SSO** utat. Ha a felület külön **Activate through your organization** vagy **Single Sign-On** lehetőséget kínál, azt válaszd, és add meg az egyetemi e-mail-címet. A böngészőben fejezd be az intézményi hitelesítést, majd térj vissza az alkalmazásba. Ha jogosultságválasztást látsz, a hallgatói Mathematicát válaszd.

A feliratok kiadásonként eltérhetnek; a [Wolfram SSO-aktiválási útmutatója](https://support.wolfram.com/54713) az aktuális képernyőket is bemutatja.

## 6. Sikeres telepítés ellenőrzése

Hozz létre egy új notebookot a **File → New → Notebook** menüvel. Írd be: `2 + 2`, majd nyomj **Shift+Enter**-t. A kimenet 4 legyen. Ez a számítás tényleges futtatását ellenőrzi, nem csak a fájl megnyitását.

Mentsd el a notebookot egy saját mappába. Ezután nyisd meg az [első példát](../../peldak/01-masodfoku-egyenlet/README.md), és a leírt sorrendben futtasd.

## Ha a jogosultság hiányzik vagy lejárt

Ellenőrizd az e-mail-megerősítést és a használt fiókot, majd az intézményi belépést a SiteInfo oldalon. A jogosultság érvényességét és esetleges megújítását a fiókodban megjelenő adatok és az aktuális intézményi tájékoztatás alapján intézd; a segédlet nem feltételez automatikus, korlátlan időtartamú hozzáférést.

Intézményi hozzáférési problémával **Gergi Miklóshoz** fordulj az egyetemi kapcsolattartási csatornán. Ha nincs meg az elérhetősége, az előadás oktatójától kérheted. Termékhibához a [Wolfram támogatási oldalát](https://support.wolfram.com/) vagy az ügyfélszolgálatot használd. Jelszót, aktiválási adatot ne küldj nyilvános hibajegybe.

Az intézményi folyamat és a kapcsolattartó az oktató 2026. szeptember 13-án megadott tájékoztatásán alapul. Következő lépés: [első notebook](elso-notebook.md) · [hibakeresés](hibakereses.md).
