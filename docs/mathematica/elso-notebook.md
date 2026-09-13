# Első notebook: cellák, futtatás, változók

[Kezdőlap](../../README.md) · [Mathematica-tartalomjegyzék](README.md)

Előfeltétel: [aktivált Mathematica](bme-licenc-es-telepites.md). A notebook `.nb` fájl, amely szöveges és kódcellákat tartalmaz. A kódot a kernel számolja ki; a kernelben korábbi változóértékek is megmaradhatnak.

## Számolás egy cellában

Új notebookban írd be, majd **Shift+Enter**:

```wolfram
2 + 2
```

A kimenet 4. Az egyszerű Enter többnyire új sort kezd a cellán belül; a Shift+Enter a kiértékelés. Az `In[...]` és `Out[...]` jelzések a számítás be- és kimeneteit azonosítják.

Új kódcellába:

```wolfram
ClearAll[x, f];
f = 2*x^2 - 5*x + 2;
Solve[f == 0, x, Reals]
```

Elvárt kimenet: `{{x -> 1/2}, {x -> 2}}`. A nyíl helyettesítési szabályt jelent. Az `f` itt kifejezés, nem `f[x_]` alakban definiált függvény. Az `x` értékének törlése azért kell, hogy szimbolikus változóként induljunk.

## Jelölések, amelyekre figyelj

| Jel | Jelentés |
| --- | --- |
| `=` | Értékadás: `a = 2` |
| `==` | Egyenlőség: `x^2 == 2` |
| `:=` | Késleltetett definíció, például `h[t_] := t^2` |
| `[]` | Függvényargumentum: `Sin[x]` |
| `{}` | Lista: `{1, 2, 3}` |
| `()` | Csoportosítás, nem függvényhívás |
| `^` | Hatványozás |
| `;` | A sor eredményének megjelenítését elnyomja |
| `/.` | Helyettesítési szabály alkalmazása: `f /. x -> 2` |
| `(* ... *)` | Megjegyzés |

A beépített függvények nagybetűvel kezdődnek: `Solve`, `D`, `Integrate`, `Sin`. Saját változónévnek inkább kisbetűs nevet válassz; az `E`, `I`, `N`, `D` például foglalt jelentésű lehet. Egzakt törthöz `1/2`, közelítő tizedeshez `0.5` írható. A szinusz argumentuma radiánban értendő.

## A kiadott notebook használata

1. [Töltsd le a repót](../kezdes.md), és a `.nb` fájlt a Mathematicával nyisd meg. A GitHub nyers fájlnézete nem számítást futtató felület.
2. Olvasd el a magyarázó szöveget. A kódcellákon haladj felülről lefelé, mindegyiket Shift+Enterrel értékeld ki.
3. A példák elején `ClearAll` törli a saját változók korábbi értékeit. Egy alsó cella önmagában nem feltétlenül fut az előzmények nélkül.
4. Összevetéshez az adott példa README-jében szereplő eredményeket használd.
5. Módosítás előtt ments saját másolatot. Átírás után a kapcsolódó későbbi cellákat is futtasd újra.

Az összes cella kiértékeléséhez az **Evaluation → Evaluate Notebook** menü használható. A tiszta futás ellenőrzéséhez a kernel leállítása és újraindítása után futtasd a notebookot elejétől. A **Quit Kernel** menü elhelyezése verziófüggő; az `Evaluation` menüben keresd. A notebookban nem mentett változtatásokat előbb mentsd el.

A grafikont mentő példánál előbb magát a notebookot is mentsd: a `NotebookDirectory[]` csak mentett notebook helyét tudja megadni. A grafikon exportálása az azonos nevű korábbi kimenetet felülírja.

Következő lépés: [példák](../../peldak/README.md) · [hibakeresés](hibakereses.md).

Források: [Wolfram Solve](https://reference.wolfram.com/language/ref/Solve.html), [ClearAll](https://reference.wolfram.com/language/ref/ClearAll.html).
