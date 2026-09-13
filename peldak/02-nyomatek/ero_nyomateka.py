"""Erő O pontra vett nyomatéka vektoriális szorzattal."""

import sympy as sp


def szamitas():
    # r_OA az O pontból az erő A támadáspontjába mutat, méterben.
    r_oa = sp.Matrix([1, 3, -2])
    ero = sp.Matrix([100, -300, 150])  # newton
    nyomatek_o = r_oa.cross(ero)  # N m; a sorrend fontos!
    # A keresztszorzat merőleges mindkét kiinduló vektorra.
    merolegesseg = (nyomatek_o.dot(r_oa), nyomatek_o.dot(ero))
    return r_oa, ero, nyomatek_o, merolegesseg


def main():
    r_oa, ero, nyomatek_o, merolegesseg = szamitas()
    print("r_OA [m]:", list(r_oa))
    print("F [N]:", list(ero))
    print("M_O [N m]:", list(nyomatek_o))
    print("Merőlegességi ellenőrzés:", merolegesseg)
    print("Fordított sorrend, F × r_OA:", list(ero.cross(r_oa)))


if __name__ == "__main__":
    main()
