# Mathematica és Python/SymPy: műveletek megfeleltetése

[Kezdőlap](../../README.md) · [Mathematica](README.md) · [Python](../python/README.md)

A két környezet ugyanazt a matematikát más szintaxissal írja le. Ne másold át változtatás nélkül a parancsokat.

| Cél | Mathematica | Python / SymPy |
| --- | --- | --- |
| Előkészítés | `ClearAll[x, f]` | `import sympy as sp`, majd `x = sp.symbols("x", real=True)` |
| Kifejezés | `f = 2*x^2 - 5*x + 2` | `f = 2*x**2 - 5*x + 2` |
| Egyenlet | `f == 0` | `sp.Eq(f, 0)` |
| Gyökök | `Solve[f == 0, x, Reals]` | `sp.solve(sp.Eq(f, 0), x)` |
| Behelyettesítés | `f /. x -> 2` | `f.subs(x, 2)` |
| Egyszerűsítés | `Simplify[f]` | `sp.simplify(f)` |
| Egzakt tört | `5/2` | `sp.Rational(5, 2)` |
| Derivált | `D[f, x]` | `sp.diff(f, x)` |
| Primitív függvény | `Integrate[f, x]` | `sp.integrate(f, x)` |
| Határozott integrál | `Integrate[f, {x, 0, 1}]` | `sp.integrate(f, (x, 0, 1))` |
| Numerikus érték | `N[Sqrt[2], 10]` | `sp.N(sp.sqrt(2), 10)` |
| Vektoriális szorzat | `Cross[r, ero]`, listákkal | `r.cross(ero)`, `sp.Matrix` objektumokkal |

Az előkészítés itt külön parancsokat jelent; a teljesen futtatható változatokat a [példafájlokban](../../peldak/README.md) találod. A `Solve` helyettesítési szabályokat, a SymPy az itt használt hívásban gyöklistát ad. Egyenletrendszernél a Python-példa `dict=True` argumentummal változó–érték szótárat kér.

A kifejezések kiírási sorrendje eltérhet. Például `6*x + 3*x^2` és `3*x^2 + 6*x` ugyanazt jelenti. Az ellenőrzés a matematikai azonosságot vizsgálja, nem a megjelenített karakterek egyezését.

Források: [Wolfram dokumentáció](https://reference.wolfram.com/language/), [SymPy bevezető](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html). Következő lépés: [példák](../../peldak/README.md).
