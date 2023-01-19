class Ohce:
    def miroir(self,mot):
        miroir = mot[::-1]
        if mot == miroir:
            return miroir + " \n Bien dit"
        return "Bonjour \n " + miroir + "\n Au revoir"
