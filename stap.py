class Stap:
    def __init__(self, beschrijving: str, tip: str = None):
        self.__beschrijving = beschrijving
        self.__tip = tip

    def get_tip(self):
        return self.__tip

    # === Getter voor database ===
    def get_beschrijving(self):
        return self.__beschrijving

    def __str__(self):
        if self.__tip:
            return f"{self.__beschrijving} (Tip: {self.__tip})"
        return self.__beschrijving
