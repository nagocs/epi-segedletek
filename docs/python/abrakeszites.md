# Grafikon készítése és mentése

[Kezdőlap](../../README.md) · [Python-tartalomjegyzék](README.md)

A [másodfokú egyenlet példája](../../peldak/01-masodfoku-egyenlet/README.md) teljes, futtatható ábrázolást tartalmaz. Az alábbi magyarázat ahhoz a fájlhoz kapcsolódik.

## Képletből pontok

A SymPy kifejezésből a `sp.lambdify(x, f, "numpy")` numerikusan kiértékelhető függvényt készít. A `np.linspace(-1, 3, 401)` 401 egyenletesen elhelyezett pontot ad a megadott tartományon. Ezeken kiértékeljük a függvényt, majd összekötjük az értékeket.

A sűrű mintavételezés szemléltetést ad, nem bizonyítja, hogy egy másik függvénynek nincsenek a pontok között elrejtett sajátosságai. A matematikai vizsgálat és a grafikon egymást egészíti ki.

## Feliratok és stílus

A `Figure(...)` létrehozza az ábrát, a `fig.subplots()` a koordinátarendszert. A `FigureCanvasAgg(fig)` lehetővé teszi az ablak nélküli rajzolást. Az `ax.plot` rajzol, az `ax.set_xlabel` és `ax.set_ylabel` a tengelyeket nevezi meg. A példában `x` és `f(x)` dimenzió nélküli mennyiségek. Fizikai grafikonon a változóhoz egység is kell, például `t [s]`.

Az `ax.scatter` külön jelöli a gyököket. Az `ax.legend` az eltérő jelölések jelentését írja ki. Ha egyetlen egyértelmű görbe van, jelmagyarázat nem mindig szükséges. A rácsvonal legyen halvány, hogy ne nyomja el a görbét.

## Két kimeneti formátum

A program a példafájl melletti `kimenet` mappába ment:

- `masodfoku_fuggveny.pdf`: a program vonalai és szövege vektorosan exportálhatók, dokumentumba illesztéshez alkalmas;
- `masodfoku_fuggveny.png`: raszteres kép, gyors megnyitáshoz vagy olyan felülethez, ahol képfájl kell.

A `fig.savefig` fájlkiterjesztésből választ formátumot. A PNG-nél `dpi=180` adja a felbontást. A PDF tartalmazhat raszteres elemeket is, tehát más forrású PDF-nél ne a kiterjesztésből ítélj.

A fájlok mentési helyét a `Path(__file__).resolve().parent` adja: ez a programfájl mappája. Emiatt a mentés a futtatás aktuális munkamappájától független. A következő futás ugyanazokat a generált képfájlokat felülírja; ha egy korábbi változat kell, előbb másold át.

## Megnyitás és használat

A kiírt útvonalon nyisd meg a PNG-t a VS Code Exploreréből vagy a fájlkezelőből. A példaprogram szándékosan nem nyit felugró ábraablakot, így terminálból is lefut. LaTeX-be illesztéshez másold a kiválasztott képet a saját LaTeX-projektedbe, és használd a [beillesztési részletet](../latex/alapmuveletek.md).

Próbáld ki: módosítsd az ábrázolás tartományát, majd figyeld meg, mennyire láthatók a gyökök. Változtasd meg a görbe színét is; a matematika ettől nem módosul.

Forrás: [Matplotlib: Figure.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html). [Vissza a példákhoz](../../peldak/README.md).
