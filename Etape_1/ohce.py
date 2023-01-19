class Ohce:
    def miroir(self,mot):
        miroir = mot[::-1]
        if mot == miroir:
            return miroir + " \nBien dit"
        return miroir
