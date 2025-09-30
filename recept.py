from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class Recept:
    def __init__(self, naam: str, omschrijving: str, aantal_personen: int = 1):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []
        self.__aantal_personen = aantal_personen

    def get_naam(self):
        return self.__naam

    def get_omschrijving(self):
        return self.__omschrijving

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def set_aantal_personen(self, aantal: int):
        """Zorgt ervoor dat de ingredienten naar het aantal personen word aangepast."""
        self.__aantal_personen = aantal
        factor = aantal
        for ing in self.__ingredient_list:
            ing.schaal_hoeveelheid(factor)

    def get_aantal_personen(self):
        return self.__aantal_personen

    def totaal_kcal(self) -> float:
        """Som van alle kcal in het recept."""
        return sum(ing.bereken_kcal() for ing in self.__ingredient_list)

    def plantaardige_versie(self):
        """Geeft een lijst van de eventuele plantaardige altenatieven."""
        alternatieven = []
        for ing in self.__ingredient_list:
            if ing.get_plantaardig():
                alternatieven.append(ing.get_plantaardig())
        return alternatieven

    def __str__(self):
        tekst = f"=== {self.__naam} === (voor {self.__aantal_personen} personen)\n"
        tekst += f"{self.__omschrijving}\n\nIngrediënten:\n"
        for ing in self.__ingredient_list:
            tekst += f"- {ing}\n"
        tekst += f"\nTotaal kcal: {self.totaal_kcal():.0f}\n"
        tekst += "\nStappen:\n"
        for i, st in enumerate(self.__stappen, start=1):
            tekst += f"{i}. {st}\n"
        return tekst

    def exporteer_naar_pdf(self, bestandsnaam=None):
        if bestandsnaam is None:
            bestandsnaam = f"{self.__naam.replace(' ', '_')}.pdf"

        w, h = A4
        c = canvas.Canvas(bestandsnaam, pagesize=A4)
        c.setTitle(self.__naam)

        # Titel
        c.setFont("Helvetica-Bold", 20)
        c.drawString(50, h - 50, f"{self.__naam}")

        # Omschrijving
        c.setFont("Helvetica", 12)
        c.drawString(50, h - 80, self.__omschrijving)

        # Ingrediënten
        y = h - 120
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Ingrediënten:")
        y -= 20
        c.setFont("Helvetica", 12)
        for ing in self.__ingredient_list:
            c.drawString(60, y, f"- {ing}")
            y -= 15

        # Stappen
        y -= 20
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Stappen:")
        y -= 20
        c.setFont("Helvetica", 12)
        for idx, st in enumerate(self.__stappen, start=1):
            c.drawString(60, y, f"{idx}. {st}")
            y -= 15
            if y < 60:
                c.showPage()
                y = h - 50
                c.setFont("Helvetica", 12)

        # Totaal kcal
        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, f"Totaal kcal: {self.totaal_kcal():.0f}")

        c.showPage()
        c.save()
        print(f"PDF opgeslagen als: {bestandsnaam}")

    # === Getters voor database ===
    def get_ingredienten(self):
        return self.__ingredient_list

    def get_stappen(self):
        return self.__stappen
