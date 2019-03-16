"""
Simpel unittest demo samt modularisering
Disse kodelinjer er beregnet til at blive importeret som modul
Hvis scriptet køres fra prompt, så køres i stedet unittests. 
"""
import unittest

def f_plus_1(x):
    return x + 1


def f_i_anden(x):
    return x * x


class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(f_plus_1(3), 4)

    def test_2(self):
        self.assertEqual(f_i_anden(3), 9)

    def test_3(self):
        self.assertIsNotNone(f_i_anden(0), 'Skal give et resultat')


if __name__ == '__main__':
    unittest.main()
