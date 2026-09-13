"""Lineáris rendszer egzakt együtthatókkal és maradékellenőrzéssel."""

import sympy as sp


def szamitas():
    x, y, z = sp.symbols("x y z", real=True)
    egyenletek = [
        sp.Eq(10*x + sp.Rational(5, 2)*y - 5*z, 100),
        sp.Eq(2*x - 5*y + 7*z, 50),
        sp.Eq(-5*x + y - z, 1),
    ]
    # A dict=True változónév -> érték megfeleltetést kér, listába csomagolva.
    eredmenyek = sp.solve(egyenletek, (x, y, z), dict=True)
    eredmeny = eredmenyek[0]  # Ennek a konkrét rendszernek egy megoldása van.
    maradekok = [
        sp.simplify((eq.lhs - eq.rhs).subs(eredmeny))
        for eq in egyenletek
    ]
    return (x, y, z), egyenletek, eredmeny, maradekok


def main():
    valtozok, _, eredmeny, maradekok = szamitas()
    for valtozo in valtozok:
        ertek = eredmeny[valtozo]
        print(f"{valtozo} = {ertek}; közelítőleg {float(ertek):.1f}")
    print("Egyenletek maradékai:", maradekok)


if __name__ == "__main__":
    main()
