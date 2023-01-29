import langue_periode_dummy as langue_periode_dummy
import constantes_salutations as salutation
import constantes_revoir as revoir
import locale
import datetime

class Ohce:

    def miroir(self,mot, langue,periode):
        if locale.getlocale()[0] == "fr_FR":
            langue = "francais"
        else:
            langue = "anglais"

        # On se connecte a l'heure du systeme
        time = datetime.datetime.now().strftime("%H")
        # Puis on applique l'heure a une des periodes definies
        if time >= "06" and time <= "12":
            periode = "matin"
        elif time >= "13" and time <= "18":
            periode = "apres_midi" 
        elif time >= "19" and time <= "23":
            periode = "soiree"
        else:
            periode = "nuit"

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
                    return salutation.anglais.MATIN
                case "apres_midi":
                    return salutation.anglais.APRES_MIDI
                case "soiree":
                    return salutation.anglais.SOIREE
                case "nuit":
                    return salutation.anglais.NUIT

        return langue_periode_dummy.revoir_langue_periode_dummy(langue,periode)
        

    def au_revoir_langue_choisit(self,langue,periode):
        langue_actuelle = langue.lower()
        periode_actuelle = periode.lower()

        if langue_actuelle == "anglais":
            match periode_actuelle:
                case "matin":
                    return  revoir.anglais.MATIN
                case "apres_midi":
                    return revoir.anglais.APRES_MIDI
                case "soiree":
                    return  revoir.anglais.SOIREE
                case "nuit":
                    return revoir.anglais.NUIT
        
        if langue_actuelle == "francais":
            match periode_actuelle:
                case "matin":
                    return  revoir.francais.MATIN
                case "apres_midi":
                    return revoir.francais.APRES_MIDI
                case "soiree":
                    return  revoir.francais.SOIREE
                case "nuit":
                    return revoir.francais.NUIT
        return langue_periode_dummy.revoir_langue_periode_dummy(langue,periode)
