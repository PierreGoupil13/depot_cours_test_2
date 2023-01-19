import unittest
import parameterized as parameterized
from ohce import Ohce


class OhceTest(unittest.TestCase):
    # Test miroir
    @parameterized.parameterized.expand(["toto", "test"])
    def test_miroir(self,mot):
        # QUAND on saisit une chaine
        ohce = Ohce()
        retour = ohce.miroir(mot)

        # ALORS celle-ci est renvoyée en miroir
        self.assertIn(mot[::-1], retour)
        
    @parameterized.parameterized.expand(["radar", "kayak"])
    def test_palindrome(self,mot):
        # QUAND on saisit un palindrome
        ohce = Ohce()
        retour = ohce.miroir(mot)

        # ALORS celui-ci est renvoyé
        retour_palindrome = ohce.miroir(mot)
        self.assertIn(mot, retour_palindrome)

        # ET 'Bien dit' est renvoyé ensuite
        self.assertIn("Bien dit",retour_palindrome)

if __name__ == '__main__':
    unittest.main()

