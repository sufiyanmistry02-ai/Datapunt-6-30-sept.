from recept import Recept
from ingredient import Ingredient
from stap import Stap
from database import init_db, sla_op_in_db, laad_recepten_uit_db

def toon_overzicht(recepten):
    print("\nBeschikbare recepten:")
    for idx, r in enumerate(recepten, start=1):
        print(f"{idx}. {r.get_naam()}")
    keuze = input("\nKies een receptnummer om te bekijken of druk Enter om terug te gaan: ").strip()
    if not keuze:
        return

    try:
        nummer = int(keuze)
        if 1 <= nummer <= len(recepten):
            recept = recepten[nummer - 1]
            personen_input = input("Voor hoeveel personen is dit recept? ")
            try:
                personen = int(personen_input)
                recept.set_aantal_personen(personen)
            except ValueError:
                print("Geen geldig getal, standaard 1 persoon gebruikt.")

            plantaardig = input("Wil je de plantaardige versie? (ja/nee) ").strip().lower()
            if plantaardig == "ja":
                alternatieven = recept.plantaardige_versie()
                if alternatieven:
                    print("\nPlantaardige alternatieven:")
                    for alt in alternatieven:
                        print("-", alt)
                else:
                    print("\nGeen plantaardige alternatieven beschikbaar.")

            print()
            print(recept)

            pdf = input("Wil je dit recept als PDF opslaan? (ja/nee) ").strip().lower()
            if pdf == "ja":
                recept.exporteer_naar_pdf()

            opslaan = input("Wil je dit recept opslaan in de database? (ja/nee) ").strip().lower()
            if opslaan == "ja":
                sla_op_in_db(recept)

            verwijder = input("\nWil je dit recept verwijderen uit het geheugen (niet DB)? (ja/nee) ").strip().lower()
            if verwijder == "ja":
                del recepten[nummer - 1]
                print("Recept verwijderd uit geheugen.")
        else:
            print("Ongeldige keuze.")
    except ValueError:
        print("Voer een geldig nummer in.")

def voeg_recept_toe(recepten):
    naam = input("Naam van het nieuwe recept: ").strip()
    omschrijving = input("Korte omschrijving: ").strip()
    try:
        personen = int(input("Aantal personen (getal): ").strip() or "1")
    except ValueError:
        personen = 1

    nieuw = Recept(naam, omschrijving, personen)

    print("\nVoeg ingrediënten toe (laat naam leeg om te stoppen):")
    while True:
        in_naam = input("Ingrediëntnaam: ").strip()
        if not in_naam:
            break
        try:
            hoeveelheid = float(input("Hoeveelheid (getal): "))
        except ValueError:
            print("Ongeldige hoeveelheid, probeer opnieuw.")
            continue
        eenheid = input("Eenheid (bijv. gram, ml, theelepels): ").strip()
        try:
            kcal = float(input("Kcal per eenheid (getal, bv. per gram of ml): ").strip() or "0")
        except ValueError:
            kcal = 0
        alternatief = input("Plantaardig alternatief (Enter voor geen): ").strip() or None
        nieuw.voeg_ingredient_toe(Ingredient(in_naam, hoeveelheid, eenheid, kcal, alternatief))

    print("\nVoeg bereidingsstappen toe (laat beschrijving leeg om te stoppen):")
    while True:
        stap_tekst = input("Stap: ").strip()
        if not stap_tekst:
            break
        tip = input("Tip voor deze stap? (Enter voor geen): ").strip() or None
        nieuw.voeg_stap_toe(Stap(stap_tekst, tip))

    recepten.append(nieuw)
    print(f"\nRecept '{naam}' is toegevoegd!\n")

def toon_recepten_uit_db():
    recepten_db = laad_recepten_uit_db()
    if not recepten_db:
        print("\nEr staan nog geen recepten in de database.\n")
        return
    print("\n=== Recepten uit database ===")
    for r in recepten_db:
        print(r)
        print("-" * 40)

def main():
    init_db()  # database klaarzetten

    recepten = []

    # Recept 1: Kip Kerrie
    kip_kerrie = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    kip_kerrie.voeg_ingredient_toe(Ingredient("Kipdijfilet", 250, "gram", 2.10, "tofu"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("gesneden ui", 75, "gram", 0.40))
    kip_kerrie.voeg_ingredient_toe(Ingredient("gehakte knoflook", 20, "gram", 1.50))
    kip_kerrie.voeg_ingredient_toe(Ingredient("kerrie masala", 0.75, "eetlepels", 3.00))
    kip_kerrie.voeg_ingredient_toe(Ingredient("gehakte tomatenblik", 0.25, "blik", 80.00))
    kip_kerrie.voeg_ingredient_toe(Ingredient("zonnebloemolie", 25, "mililiter", 8.84))
    kip_kerrie.voeg_ingredient_toe(Ingredient("grstd en gmln komijn", 0.5, "theelepels", 3.70))
    kip_kerrie.voeg_ingredient_toe(Ingredient("zout", 0.5, "theelepels", 0.00))
    kip_kerrie.voeg_ingredient_toe(Ingredient("maggiblokje", 0.25, "blokje", 10.00))
    kip_kerrie.voeg_ingredient_toe(Ingredient("water", 31.25, "mililiter", 0.00))
    kip_kerrie.voeg_stap_toe(Stap("Doe de zonnebloemolie in de pan en verhit dit.", "Niet te heet zetten."))
    kip_kerrie.voeg_stap_toe(Stap("Bak de uitjes en knoflook tot bruin, niet zwart."))
    kip_kerrie.voeg_stap_toe(Stap("Voeg kerrie masala toe, snij kip/tofu ondertussen."))
    kip_kerrie.voeg_stap_toe(Stap("Blus af met tomaten uit blik."))
    kip_kerrie.voeg_stap_toe(Stap("Voeg kip/tofu toe en laat sudderen."))
    kip_kerrie.voeg_stap_toe(Stap("Na 10 minuten water, zout en maggi toevoegen."))
    kip_kerrie.voeg_stap_toe(Stap("Kook door tot kip gaar is of tofu zacht; serveer met rijst."))
    recepten.append(kip_kerrie)

    # Recept 2: Wentelteefjes
    wentelteefjes = Recept("Wentelteefjes", "Zoete ontbijt van oud brood met ei en melk")
    wentelteefjes.voeg_ingredient_toe(Ingredient("brood", 3, "sneetjes", 80.00, "plantaardig brood"))
    wentelteefjes.voeg_ingredient_toe(Ingredient("ei", 2, "stuks", 78.00, "vegan-ei"))
    wentelteefjes.voeg_ingredient_toe(Ingredient("melk", 250, "mililiter", 0.60, "sojamelk"))
    wentelteefjes.voeg_ingredient_toe(Ingredient("gemalen kaneel", 2, "gram", 3.00))
    wentelteefjes.voeg_ingredient_toe(Ingredient("suiker", 50, "gram", 4.00))
    wentelteefjes.voeg_stap_toe(Stap("Kluts de eieren in een bord."))
    wentelteefjes.voeg_stap_toe(Stap("Meng melk, kaneel en suiker."))
    wentelteefjes.voeg_stap_toe(Stap("Wentel brood in melkmengsel en daarna in ei."))
    wentelteefjes.voeg_stap_toe(Stap("Bak in koekenpan met boter tot krokant laagje."))
    recepten.append(wentelteefjes)

    # Recept 3: Aardappelpuree
    aardappelpuree = Recept("Aardappelpuree", "Romige aardappelpuree")
    aardappelpuree.voeg_ingredient_toe(Ingredient("aardappels", 166.70, "gram", 0.77))
    aardappelpuree.voeg_ingredient_toe(Ingredient("water", 0.83, "liter", 0.00))
    aardappelpuree.voeg_ingredient_toe(Ingredient("zout", 0.33, "gram", 0.00))
    aardappelpuree.voeg_ingredient_toe(Ingredient("zwarte peper", 0.33, "gram", 2.50))
    aardappelpuree.voeg_ingredient_toe(Ingredient("nootmuskaat", 0.33, "gram", 5.00))
    aardappelpuree.voeg_ingredient_toe(Ingredient("ongez. slagroom", 42.00, "mililiter", 3.45, "aquafaba"))
    aardappelpuree.voeg_ingredient_toe(Ingredient("roomboter", 16.70, "gram", 7.17, "margarine"))
    aardappelpuree.voeg_stap_toe(Stap("Schil en snijd de aardappels in stukken."))
    aardappelpuree.voeg_stap_toe(Stap("Kook de aardappels gaar."))
    aardappelpuree.voeg_stap_toe(Stap("Giet af en pureer de aardappels."))
    aardappelpuree.voeg_stap_toe(Stap("Voeg slagroom/aquafaba en boter/margarine toe; roer tot glad."))
    aardappelpuree.voeg_stap_toe(Stap("Breng op smaak met zout, peper en nootmuskaat."))
    recepten.append(aardappelpuree)

    while True:
        print("\n=== Hoofdmenu ===")
        print("1. Overzicht bekijken")
        print("2. Nieuw recept toevoegen")
        print("3. Afsluiten")
        print("4. Recepten uit database tonen")

        keuze = input("Maak een keuze: ").strip()
        if keuze == "1":
            toon_overzicht(recepten)
        elif keuze == "2":
            voeg_recept_toe(recepten)
        elif keuze == "3":
            print("Programma afgesloten.")
            break
        elif keuze == "4":
            toon_recepten_uit_db()
        else:
            print("Ongeldige keuze.")

if __name__ == "__main__":
    main()