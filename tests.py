# tests.py
import unittest
from operaciones import suma, resta, multiplicacion

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(0, 0), 0)
        self.assertEqual(resta(10, 15), -5)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
        self.assertEqual(multiplicacion(0, 5), 0)
        self.assertEqual(multiplicacion(-2, -2), 4)

if __name__ == '__main__':
    unittest.main()
