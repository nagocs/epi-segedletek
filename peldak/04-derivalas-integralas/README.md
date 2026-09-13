# Deriválás és integrálás

[Példák](../README.md) · [Python-fájl](derivalas_integralas.py) · [Mathematica-notebook](derivalas_integralas.nb)

Két dimenzió nélküli függvényt vizsgálunk: `f(x) = x³ + 3x² − 2` és `g(x) = exp(−x/2) sin(x)`. A szinusz argumentuma radiánban értendő. A példa deriváltat, primitív függvényt és a `[0, 1]` intervallumon vett határozott integrált számít.

## Futtatás

Windows, a repó gyökeréből:

```powershell
.\.venv\Scripts\python.exe peldak/04-derivalas-integralas/derivalas_integralas.py
```

macOS/Linux:

```bash
./.venv/bin/python peldak/04-derivalas-integralas/derivalas_integralas.py
```

Mathematicában a fenti notebook bemeneti celláin felülről lefelé haladj **Shift+Enter** segítségével.

## A három művelet különbsége

A `diff` / `D` a deriváltat adja. Az `integrate(kifejezes, x)` / `Integrate[kifejezes, x]` egy primitív függvényt ad. A primitívek családjához hozzá kell gondolni a **+ C** tetszőleges állandót, amelyet a program nem ír bele a szimbolikus kifejezésbe.

A határozott integrálnál az alsó és felső határt is megadjuk: Pythonban `(x, 0, 1)`, Mathematicában `{x, 0, 1}`. Ennek eredménye itt egy szám, nem egy újabb x-függvény. A határozott integrál előjeles; nem mindig azonos a grafikon és a tengely közötti geometriai területtel.

## Várt eredmény

- `f'(x) = 3x² + 6x`; egy primitív: `x⁴/4 + x³ − 2x`; a határozott integrál **−3/4**.
- `g'(x) = exp(−x/2) [cos(x) − sin(x)/2]`.
- A g egy primitívje `−(2/5) exp(−x/2) [sin(x) + 2cos(x)]`; a határozott integrál közelítőleg **0,333680888164203**.

Mindkét primitív visszaderiválásával az eredeti függvényt kapjuk: a különbség egyszerűsítés után nulla. Az eltérő alakú kifejezéseket a különbségük egyszerűsítésével lehet összevetni. Két helyes primitív egymástól állandóban is eltérhet.
