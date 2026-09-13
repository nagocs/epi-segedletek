"""Deriváltak, primitív függvények és 0–1 közötti határozott integrálok."""

import sympy as sp


def szamitas():
    x = sp.symbols("x", real=True)
    fuggvenyek = {
        "f": x**3 + 3*x**2 - 2,
        "g": sp.exp(-sp.Rational(1, 2)*x)*sp.sin(x),
    }
    eredmenyek = {}
    for nev, kifejezes in fuggvenyek.items():
        derivalt = sp.diff(kifejezes, x)
        primitiv = sp.integrate(kifejezes, x)
        integral = sp.integrate(kifejezes, (x, 0, 1))
        # A primitív visszaderiválásával az eredeti függvényt kell kapnunk.
        ellenorzes = sp.simplify(sp.diff(primitiv, x) - kifejezes)
        eredmenyek[nev] = {
            "kifejezes": kifejezes,
            "derivalt": derivalt,
            "primitiv": primitiv,
            "integral": integral,
            "ellenorzes": ellenorzes,
        }
    return x, eredmenyek


def main():
    _, eredmenyek = szamitas()
    for nev, adatok in eredmenyek.items():
        print(f"{nev}(x) = {adatok['kifejezes']}")
        print("Derivált:", adatok["derivalt"])
        print("Egy primitív függvény (+ C):", adatok["primitiv"])
        print("Határozott integrál [0, 1]:", adatok["integral"])
        print("Közelítő érték:", sp.N(adatok["integral"], 15))
        print("Visszaderiválás maradéka:", adatok["ellenorzes"])
        print()


if __name__ == "__main__":
    main()
