class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredienten = []
        self.__stappen = []

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredienten.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def __str__(self):
        tekst = f"=== {self.__naam} ===\n{self.__omschrijving}\n\nIngrediënten:\n"
        for ing in self.__ingredienten:
            tekst += f"- {ing}\n"
        tekst += "\nStappen:\n"
        for i, st in enumerate(self.__stappen, start=1):
            tekst += f"{i}. {st}\n"
        return tekst
