import unittest
import parameterized as parameterized
from ohce import Ohce

class OhceTest(unittest.TestCase):
    # Test salutation avec langue et periode
    @parameterized.parameterized.expand([
        ("francais","matin","test", "Bonjour"),
        ("anglais","matin","toto", "Good Morning")
        ])
    def test_palindrome_langue(self,langue,periode_journee,mot,attendu):
        # ETANT DONNE une langue ET une période de la journée
        ohce = Ohce()

        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,langue,periode_journee)
        print(resultat)
        # ALORS "salutation" est retournée avant tout dans la langue choisie
        self.assertIn(attendu,resultat)

    # Test au revoir avec langue et periode
    @parameterized.parameterized.expand([
        ("francais","matin","test", "Au revoir"),
        ("anglais","matin","toto", "Good bye")
        ])
    def test_palindrome_langue(self,langue,periode_journee,mot,attendu):
        # ETANT DONNE une langue ET une période de la journée
        ohce = Ohce()

        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,langue,periode_journee)
        print(resultat)
        # ALORS "au revoir" est retournée après tout dans la langue choisie
        self.assertIn(attendu,resultat)
        
if __name__ == '__main__':
    unittest.main()

