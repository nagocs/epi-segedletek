# Mathematica-hibakeresés

[Kezdőlap](../../README.md) · [Mathematica-tartalomjegyzék](README.md)

| Jelenség | Teendő |
| --- | --- |
| Nincs termék a My Products alatt | Az egyetemi e-mail-címmel indultál a SiteInfo oldalon? Megerősítetted a címet? A megfelelő fiókban vagy? |
| Aktiválást kér / licenchiba | Kövesd újra az [SSO-útvonalat](bme-licenc-es-telepites.md); ellenőrizd a jogosultságot és az internetelérést. Intézményi problémával Gergi Miklóshoz fordulhatsz. |
| Megnyílik a notebook, de nem fut | A Mathematicában nyitottad meg, nem előnézetben? Shift+Entert nyomtál? A kernel aktivált? |
| Változatlanul visszaír egy parancsot | Nézd meg a nagybetűt és a szögletes zárójelet: `Sin[x]`, nem `sin(x)`. |
| Ismeretlen helyett szám jelenik meg | Korábbi érték maradt a kernelben. Futtasd a notebook eleji `ClearAll` cellát és utána a további cellákat. |
| Nincs kimenet | A sor végén `;` állhat. A számítás megtörténhetett; a kiíráshoz a változót külön cellában is kiértékelheted. |
| Más alakú képletet kaptál | Egyszerűsítsd a két alak különbségét. A tagok sorrendje nem lényeges. |
| Tizedes érték egzakt tört helyett | A bemeneten `0.5` helyett `1/2` kell az egzakt számításhoz. Később `N` kérhet közelítő értéket. |
| `NotebookDirectory` hibát ad | Előbb mentsd el a notebookot egy saját, írható mappába, majd futtasd az exportcellát. |
| Export nem sikerül | A mappa írható-e, és a PDF nincs-e más programban zárolva? A kiírt útvonalat vizsgáld. |
| Hiányzó csomagot említ a korábbi példa | A repó új `.nb` példáit használd: ezek nem igényelnek személyes ábrázolócsomagot. |

Módosítás után ne csak az utolsó cellát futtasd: az előző definíciókat is frissíteni kell. A program régi kimenete nem bizonyítja, hogy a mostani változat működik.

Hibajelzéskor hasznos a `$Version` kimenete és az első hibaüzenet. Jelszót vagy aktiválási adatot ne másolj bele. [Wolfram támogatás](https://support.wolfram.com/).
