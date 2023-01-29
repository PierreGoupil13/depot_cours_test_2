import unittest
import parameterized as parameterized
from ohce import Ohce

class OhceTest(unittest.TestCase):

    # Test salutation avec langue du systeme
    @parameterized.parameterized.expand([
        ("soiree","test", "Bonsoir"),
        ("nuit","test", "Bonne nuit"),
        ("matin","test", "Bonjour"),
        ])
    def test_miroir_langue_system(self,periode_journee,mot,attendu):
        # ETANT DONNE une langue systeme ET une période de la journée
        ohce = Ohce()

        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,None,periode_journee)

        # ALORS "salutation" est retournée avant tout dans la langue choisie
        self.assertIn(attendu,resultat)

    # Test au revoir avec periode du systeme
    @parameterized.parameterized.expand([
        ("francais","test", "Bonsoir"),
        ])
    def test_miroir_periode_system(self,langue,mot,attendu):
        # ETANT DONNE une langue ET une période de la journée du système
        ohce = Ohce()

        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,langue,None)

        # ALORS "au revoir" est retournée après tout dans la langue choisie
        self.assertIn(attendu,resultat)

    # Test miroir avec Input du systeme
    @parameterized.parameterized.expand([
        ("tset"),
        ("otot")
        ])
    def test_miroir_entree_systeme(self,attendu):
        # ETANT DONNE une langue ET une période de la journée
        ohce = Ohce()
        mot = input("Entrez un mot: \n ")
        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,None,None)

        # ALORS "au revoir" est retournée après tout dans la langue choisie
        self.assertIn(attendu,resultat)
    
    # Test palindrome avec Input du systeme
    @parameterized.parameterized.expand([
        ("kayak"),
        ("radar")
        ])
    def test_miroir_entree_systeme(self,attendu):
        # ETANT DONNE une langue ET une période de la journée
        ohce = Ohce()
        mot = input("Entrez un palindrome: \n ")
        # QUAND on saisit une chaine de caractère
        resultat = ohce.miroir(mot,None,None)

        # ALORS "au revoir" est retournée après tout dans la langue choisie
        self.assertIn(attendu,resultat)

if __name__ == '__main__':
    unittest.main()

