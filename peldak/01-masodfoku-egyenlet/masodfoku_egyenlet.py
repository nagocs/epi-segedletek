"""Másodfokú egyenlet: egzakt gyökök, ellenőrzés és grafikon."""

from pathlib import Path

import sympy as sp


def szamitas():
    """A szimbolikus eredményeket visszaadja, fájlt nem hoz létre."""
    x = sp.symbols("x", real=True)
    f = 2*x**2 - 5*x + 2
    gyokok = sp.solve(sp.Eq(f, 0), x)
    # Minden gyöknél az eredeti kifejezés értékét nézzük meg.
    maradekok = [sp.simplify(f.subs(x, gyok)) for gyok in gyokok]
    return x, f, gyokok, maradekok


def abra_mentese(x, f, gyokok, kimeneti_mappa):
    """PDF-et és PNG-t ment; a meglévő azonos nevű kimeneteket felülírja."""
    import numpy as np
    # Ablak nélküli rajzolás: terminálból és automatikus ellenőrzésben is működik.
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_agg import FigureCanvasAgg

    numerikus_f = sp.lambdify(x, f, "numpy")
    x_ertekek = np.linspace(-1, 3, 401)
    fig = Figure(figsize=(6.4, 4.0), layout="constrained")
    FigureCanvasAgg(fig)
    ax = fig.subplots()
    ax.plot(x_ertekek, numerikus_f(x_ertekek), label=r"$2x^2-5x+2$")
    ax.scatter([float(gyok) for gyok in gyokok], [0]*len(gyokok),
               color="tab:red", zorder=3, label="Gyökök")
    ax.axhline(0, color="0.4", linewidth=0.8)
    ax.set_xlabel("x (dimenzió nélküli)")
    ax.set_ylabel("f(x) (dimenzió nélküli)")
    ax.grid(alpha=0.25)
    ax.legend()
    kimeneti_mappa = Path(kimeneti_mappa)
    kimeneti_mappa.mkdir(parents=True, exist_ok=True)
    fajlok = []
    for formatum in ("pdf", "png"):
        fajl = kimeneti_mappa / f"masodfoku_fuggveny.{formatum}"
        fig.savefig(fajl, dpi=180)
        fajlok.append(fajl)
    return fajlok


def main():
    x, f, gyokok, maradekok = szamitas()
    print("Gyökök:", gyokok)
    print("Visszahelyettesítési maradékok:", maradekok)
    kimenet = Path(__file__).resolve().parent / "kimenet"
    for fajl in abra_mentese(x, f, gyokok, kimenet):
        print("Mentett ábra:", fajl)


if __name__ == "__main__":
    main()
