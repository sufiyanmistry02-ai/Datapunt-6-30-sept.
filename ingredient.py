class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str, kcal_per_100g: float, plantaardig_alternatief=None):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal_per_100g = kcal_per_100g
        self.__plantaardig_alternatief = plantaardig_alternatief

    def kcal(self):
        return (self.__hoeveelheid / 100) * self.__kcal_per_100g

    def alternatief(self):
        return self.__plantaardig_alternatief if self.__plantaardig_alternatief else self.__naam

    def __str__(self):
        tekst = f"{self.__naam}: {self.__hoeveelheid} {self.__eenheid} ({self.kcal():.0f} kcal)"
        if self.__plantaardig_alternatief:
            tekst += f" | alternatief: {self.__plantaardig_alternatief}"
        return tekst
