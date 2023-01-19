import unittest
import parameterized as parameterized
from ohce import Ohce


class OhceTest(unittest.TestCase):
    # Test miroir
    @parameterized.parameterized.expand(["toto", "test"])
    def test_miroir(self,mot):
        # Quand on saisit une chaine
        ohce = Ohce()
        retour = ohce.miroir(mot)

        # Alors celle-ci est renvoyée en miroir
        self.assertIn(mot[::-1], retour)

if __name__ == '__main__':
    unittest.main()

