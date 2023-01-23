import unittest
import parameterized as parameterized
from ohce import Ohce

class OhceTest(unittest.TestCase):
    # Test salutation avec langue et periode
    @parameterized.parameterized.expand([
        ("francais","matin","test", "Bonjour"),
        ("anglais","matin","toto", "Good morning"),
        ("francais","apres_midi","test", "Bonjour"),
        ("anglais","apres_midi","toto", "Good afternoon"),
        ])
    def test_miroir_langue_periode_salutation(self,langue,periode_journee,mot,attendu):
        # ETANT DONNE une langue ET une période de la journée
        ohce = Ohce()

        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,langue,periode_journee)

        # ALORS "salutation" est retournée avant tout dans la langue choisie
        self.assertIn(attendu,resultat)

    # Test au revoir avec langue et periode
    @parameterized.parameterized.expand([
        ("francais","matin","test", "Au revoir"),
        ("anglais","matin","toto", "Good bye"),
        ("francais","nuit","test", "Bonne nuit"),
        ("anglais","nuit","toto", "Good night")
        ])
    def test_miroir_langue_periode_revoir(self,langue,periode_journee,mot,attendu):
        # ETANT DONNE une langue ET une période de la journée
        ohce = Ohce()

        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,langue,periode_journee)

        # ALORS "au revoir" est retournée après tout dans la langue choisie
        self.assertIn(attendu,resultat)

if __name__ == '__main__':
    unittest.main()

