"""A matematikai eredmények és az ábraexport ellenőrzése."""

import importlib.util
from pathlib import Path
import tempfile
import unittest

import mpmath
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def load_example(folder, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "peldak" / folder / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PeldakTest(unittest.TestCase):
    def test_quadratic_roots_and_factorization(self):
        module = load_example("01-masodfoku-egyenlet", "masodfoku_egyenlet")
        x, f, roots, residuals = module.szamitas()
        self.assertEqual(set(roots), {sp.Rational(1, 2), sp.Integer(2)})
        self.assertEqual(sp.expand(f - (2*x - 1)*(x - 2)), 0)
        self.assertEqual(residuals, [0, 0])

    def test_plot_exports(self):
        module = load_example("01-masodfoku-egyenlet", "masodfoku_egyenlet")
        x, f, roots, _ = module.szamitas()
        with tempfile.TemporaryDirectory() as directory:
            files = module.abra_mentese(x, f, roots, Path(directory) / "abra")
            self.assertEqual({p.suffix for p in files}, {".pdf", ".png"})
            signatures = {".pdf": b"%PDF-", ".png": b"\x89PNG\r\n\x1a\n"}
            for path in files:
                self.assertTrue(path.read_bytes().startswith(signatures[path.suffix]))
                self.assertGreater(path.stat().st_size, 1000)

    def test_moment_components_and_geometry(self):
        module = load_example("02-nyomatek", "ero_nyomateka")
        r, force, moment, perpendicular = module.szamitas()
        self.assertEqual(list(moment), [-150, -350, -600])
        self.assertEqual(perpendicular, (0, 0))
        self.assertEqual(force.cross(r), -moment)
        self.assertEqual(r.cross(2*force), 2*moment)
        self.assertEqual(r.cross(10*r), sp.zeros(3, 1))

    def test_linear_system_independent_matrix_check(self):
        module = load_example("03-egyenletrendszer", "linearis_egyenletrendszer")
        variables, _, result, residuals = module.szamitas()
        values = sp.Matrix([result[v] for v in variables])
        self.assertEqual(list(values), [sp.Rational(-133, 5), sp.Rational(-2052, 5), sp.Rational(-1392, 5)])
        matrix = sp.Matrix([[10, sp.Rational(5, 2), -5], [2, -5, 7], [-5, 1, -1]])
        self.assertNotEqual(matrix.det(), 0)
        self.assertEqual(matrix*values, sp.Matrix([100, 50, 1]))
        self.assertEqual(residuals, [0, 0, 0])

    def test_calculus_identities_and_numerical_quadrature(self):
        module = load_example("04-derivalas-integralas", "derivalas_integralas")
        x, results = module.szamitas()
        self.assertEqual(results["f"]["derivalt"], 3*x**2 + 6*x)
        self.assertEqual(results["f"]["integral"], sp.Rational(-3, 4))
        expected_g_derivative = sp.exp(-x/2)*(sp.cos(x) - sp.sin(x)/2)
        self.assertEqual(sp.simplify(results["g"]["derivalt"] - expected_g_derivative), 0)
        for data in results.values():
            self.assertEqual(data["ellenorzes"], 0)
            primitive = data["primitiv"]
            self.assertEqual(sp.simplify(primitive.subs(x, 1) - primitive.subs(x, 0) - data["integral"]), 0)
        numerical = mpmath.quad(lambda t: mpmath.exp(-t/2)*mpmath.sin(t), [0, 1])
        self.assertAlmostEqual(float(results["g"]["integral"]), float(numerical), places=12)


if __name__ == "__main__":
    unittest.main()
