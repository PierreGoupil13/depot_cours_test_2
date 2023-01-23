import langue_periode_dummy as langue_periode_dummy
class Ohce:

    def miroir(self,mot, langue,periode):
        miroir = mot[::-1]
        bien_dit_langue = self.langue_palindrome(langue)
        bonjour_langue_choisit = self.salutation_langue_periode(langue,periode)
        au_revoir_langue_choisit = self.au_revoir_langue_choisit(langue,periode)

        if mot == miroir:
            return miroir + bien_dit_langue
        return bonjour_langue_choisit + "\n " + miroir + "\n " + au_revoir_langue_choisit
    
    def langue_palindrome(self,langue):
        langue_actuelle = langue.lower()
        if langue_actuelle == "francais":
            return "\n Bien dit"
        else :
            return "\n Well said"
    
    def salutation_langue_periode(self,langue,periode):
        return langue_periode_dummy.salutation_langue_periode_dummy(langue,periode)
    
    def au_revoir_langue_choisit(self,langue,periode):
        return langue_periode_dummy.revoir_langue_periode_dummy(langue,periode)
