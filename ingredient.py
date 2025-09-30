class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str, kcal_per_100g: float):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal_per_100g = kcal_per_100g

    def kcal(self):
        # kcal berekenen op basis van hoeveelheid (gram/ml)
        return (self.__hoeveelheid / 100) * self.__kcal_per_100g

    def __str__(self):
        return f"{self.__naam}: {self.__hoeveelheid} {self.__eenheid} ({self.kcal():.0f} kcal)"
