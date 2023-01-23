import unittest
import parameterized as parameterized
from ohce import Ohce


class OhceTest(unittest.TestCase):
    # Test bien dit avec langue
    @parameterized.parameterized.expand([
        ("francais","radar", "Bien dit"),
        ("anglais","kayak", "Well said")
        ])
    def test_palindrome_langue(self,langue,mot,attendu):
        # QUAND on saisit un palindrome ET que l'on saisit une langue
        ohce = Ohce()

        # ALORS celui-ci est renvoyé
        retour_palindrome = ohce.miroir(mot,langue)
        self.assertIn(mot, retour_palindrome)

        # ET 'Bien dit' est renvoyé ensuite dans la langue correcte
        self.assertIn(attendu,retour_palindrome)
    
    @parameterized.parameterized.expand([
        ("francais","toto", "Bonjour"),
        ("anglais","test", "Hello")
        ])
    def test_bonjour_langue(self,langue,mot,attendu):
        #QUAND on saisit une chaîne ET une langue
        ohce = Ohce()

        #ALORS 'Bonjour' est renvoyé dans la langue choisis
        retour_palindrome = ohce.miroir(mot,langue)
        self.assertIn(attendu,retour_palindrome)

        #ET celle-ci est retourné en miroir
        self.assertIn(mot[::-1], retour_palindrome)
    
    @parameterized.parameterized.expand([
        ("francais","toto", "Au revoir"),
        ("anglais","test", "Good bye")
        ])
    def test_au_revoir_langue(self,langue,mot,attendu):
        # QUAND on saisit une chaine ET une langue
        ohce = Ohce()

        # ALORS celle-ci est retourné en miroir
        retour_palindrome = ohce.miroir(mot,langue)
        self.assertIn(mot[::-1], retour_palindrome)

        # ET 'au revoir' est envoyé ensuite dans la langue séléctioné
        self.assertIn(attendu,retour_palindrome)

if __name__ == '__main__':
    unittest.main()

