import langue_periode_dummy as langue_periode_dummy
import constantes_salutations as salutation

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
        langue_actuelle = langue.lower()
        periode_actuelle = periode.lower()
        if langue_actuelle == "francais":
            match periode_actuelle:
                case "matin":
                    return salutation.francais.MATIN
                case "apres_midi":
                    return salutation.francais.APRES_MIDI
                case "soiree":
                    return salutation.francais.SOIREE
                case "nuit":
                    return salutation.francais.NUIT

        if langue_actuelle == "anglais":
            match periode_actuelle:
                case "matin":
                    return  salutation.anglais.MATIN
                case "apres_midi":
                    return salutation.anglais.APRES_MIDI
                case "soiree":
                    return  salutation.anglais.SOIREE
                case "nuit":
                    return salutation.anglais.NUIT
    
    def au_revoir_langue_choisit(self,langue,periode):
        return langue_periode_dummy.revoir_langue_periode_dummy(langue,periode)
