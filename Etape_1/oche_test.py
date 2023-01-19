import unittest
from ohce import Ohce
class OhceTest(unittest.TestCase):
    # Test miroir
    def test_miroir(self,mot):
        
        # Quand on saisit une chaine
        ohce = Ohce()
        retour = ohce.miroir(mot)

        # Alors celle-ci est renvoyée en miroir
        self.assertIn(mot[::-1], retour)
        

