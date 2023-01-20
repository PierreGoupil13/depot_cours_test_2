import unittest
import parameterized as parameterized
from ohce import Ohce


class OhceTest(unittest.TestCase):
    # Test bien dit avec langue
    @parameterized.parameterized.expand([
        ("francais","radar", "Bien dit"),
        ("anglais","kayak", "Well said")
        ])
    def test_palindrome(self,langue,mot,attendu):
        # QUAND on saisit un palindrome ET que l'on saisit une langue
        ohce = Ohce().langue_palindrome(langue)
        retour = ohce.miroir(mot)

        # ALORS celui-ci est renvoyé
        retour_palindrome = ohce.miroir(mot)
        self.assertIn(mot, retour_palindrome)

        # ET 'Bien dit' est renvoyé ensuite dans la langue correcte
        self.assertIn(attendu,retour_palindrome)


if __name__ == '__main__':
    unittest.main()

