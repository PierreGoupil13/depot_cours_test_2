class Ohce:
    def miroir(self,mot, langue):
        miroir = mot[::-1]
        bien_dit_langue = self.langue_palindrome(langue)
        bonjour_langue_choisit = self.bonjour_langue(langue)

        if mot == miroir:
            return miroir + bien_dit_langue
        return bonjour_langue_choisit + "\n " + miroir + "\n Au revoir"
    
    def langue_palindrome(self,langue):
        langue_actuelle = langue.lower()
        if langue_actuelle == "francais":
            return "\n Bien dit"
        else :
            return "\n Well said"
    
    def bonjour_langue(self,langue):
        return ""
