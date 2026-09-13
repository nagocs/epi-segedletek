# SymPy-alapok

[Kezdőlap](../../README.md) · [Python-tartalomjegyzék](README.md)

Előfeltétel: [telepített csomagok](vscode-windows.md) és egy [futtatható saját `.py` fájl](elso-program.md). A következő blokkokat ugyanabba a próbafájlba, sorrendben írhatod.

## Szimbólum és kifejezés

```python
import sympy as sp

x = sp.symbols("x", real=True)
f = 2*x**2 - 5*x + 2
print(f)
```

Az `import` betölti a csomagot, az `as sp` rövid nevet ad neki. Az `x` itt szimbólum, nem számérték. A `real=True` azt mondja, hogy valós változóként kezeljük. Az `f` szimbolikus kifejezés: nem Python-függvény, ezért nem `f(2)` módon helyettesítünk bele.

## Egyenlet és visszahelyettesítés

```python
egyenlet = sp.Eq(f, 0)
gyokok = sp.solve(egyenlet, x)
print(gyokok)
print([sp.simplify(f.subs(x, gyok)) for gyok in gyokok])
```

Kimenet: `[1/2, 2]`, majd `[0, 0]`. Az `Eq` egyenletet épít, a `solve` a megadott változóra keres értékeket. A `subs` behelyettesít, a `simplify` egyszerűsít. A szögletes zárójelben lévő kifejezés mindegyik gyökre elvégzi ugyanazt az ellenőrzést és listába gyűjti az eredményeket.

## Egzakt és közelítő érték

```python
fele = sp.Rational(1, 2)
print(fele)
print(sp.sqrt(2))
print(sp.N(sp.sqrt(2), 10))
```

A `Rational` pontos törtet ad. A sima Python `1/2` már a SymPy előtt lebegőpontos `0.5` értékké válik. A szimbolikus ágban ezért egész számokból képzett törtekkel dolgozunk. A `N(..., 10)` tíz számjegyes numerikus kiértékelést kér, nem tíz tizedesjegyet.

## Deriválás és integrálás

```python
print(sp.diff(f, x))
print(sp.integrate(f, x))
print(sp.integrate(f, (x, 0, 1)))
```

Az első a derivált, a második egy primitív függvény, a harmadik határozott integrál. A primitív függvényekhez tetszőleges additív állandó tartozhat; a SymPy egy képviselőt ad vissza. A részletes példában mindkét integrálás külön szerepel.

## Rövid szintaktikai emlékeztető

| Szándék | Python/SymPy alak |
| --- | --- |
| Szorzás | `2*x`, nem `2x` |
| Hatvány | `x**2`, nem `x^2` |
| Értékadás | `f = ...` |
| Egyenlet létrehozása | `sp.Eq(bal, jobb)` |
| Tizedestört | `2.5` |
| Pontos tört | `sp.Rational(5, 2)` |
| Szinusz | `sp.sin(x)`; radiánban értelmezett szög |

A `==` Pythonban összehasonlítás, nem ismeretlenes egyenletépítő parancs. Szimbolikus azonosságok ellenőrzésekor gyakran a két oldal különbségét egyszerűsítjük. A változó feltevései és az értelmezési tartomány is számítanak: például valós `x` mellett `sqrt(x**2)` nem mindig `x`.

Következő lépés: [másodfokú egyenlet](../../peldak/01-masodfoku-egyenlet/README.md) · [hibakeresés](hibakereses.md).

Források: [SymPy: gyakori buktatók](https://docs.sympy.org/latest/tutorials/intro-tutorial/gotchas.html), [egyenletek](https://docs.sympy.org/latest/tutorials/intro-tutorial/solvers.html), [kalkulus](https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html).
