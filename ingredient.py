class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str, kcal_per_eenheid: float = 0, plantaardig_alternatief: str = None):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__basis_hoeveelheid = hoeveelheid
        self.__kcal_per_eenheid = kcal_per_eenheid
        self.__plantaardig = plantaardig_alternatief

    def bereken_kcal(self) -> float:
        return self.__kcal_per_eenheid * self.__hoeveelheid

    def schaal_hoeveelheid(self, factor: float):
        self.__hoeveelheid = self.__basis_hoeveelheid * factor

    def get_plantaardig(self):
        return self.__plantaardig

    # === Getters voor database ===
    def get_naam(self):
        return self.__naam

    def get_hoeveelheid(self):
        return self.__hoeveelheid

    def get_eenheid(self):
        return self.__eenheid

    def get_kcal_per_eenheid(self):
        return self.__kcal_per_eenheid

    def __str__(self):
        extra = f" ({self.bereken_kcal():.0f} kcal)" if self.__kcal_per_eenheid else ""
        return f"{self.__naam}: {self.__hoeveelheid} {self.__eenheid}{extra}"
