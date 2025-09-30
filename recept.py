class Recept:
    def __init__(self, naam: str, omschrijving: str, aantal_personen: int = 1):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredienten = []
        self.__stappen = []
        self.__aantal_personen = aantal_personen

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredienten.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def totaal_kcal(self):
        return sum(ing.kcal() for ing in self.__ingredienten)

    def kcal_per_persoon(self):
        if self.__aantal_personen > 0:
            return self.totaal_kcal() / self.__aantal_personen
        return self.totaal_kcal()

    def toon_plantaardig(self):
        tekst = f"=== {self.__naam} (plantaardig) ===\n{self.__omschrijving}\n"
        tekst += f"(voor {self.__aantal_personen} personen)\n\nIngrediënten:\n"
        for ing in self.__ingredienten:
            tekst += f"- {ing.alternatief()}\n"
        return tekst

    def __str__(self):
        tekst = f"=== {self.__naam} ===\n{self.__omschrijving}\n"
        tekst += f"(voor {self.__aantal_personen} personen)\n\nIngrediënten:\n"
        for ing in self.__ingredienten:
            tekst += f"- {ing}\n"
        tekst += "\nStappen:\n"
        for i, st in enumerate(self.__stappen, start=1):
            tekst += f"{i}. {st}\n"
        tekst += f"\nTotaal kcal: {self.totaal_kcal():.0f} kcal"
        tekst += f"\nPer persoon: {self.kcal_per_persoon():.0f} kcal"
        return tekst
