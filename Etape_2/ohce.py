class Ohce:
    def miroir(self,mot, langue):
        miroir = mot[::-1]
        mot_palindrome = self.langue_palindrome(langue)
        if mot == miroir:
            return miroir + mot_palindrome
        return "Bonjour \n " + miroir + "\n Au revoir"
    
    def langue_palindrome(self,langue):
        langue_actuelle = langue.lower()
        if langue_actuelle == "francais":
            return "\n Bien dit"
        else :
            return "\n Well said"
        
