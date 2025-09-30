from recept import Recept
from ingredient import Ingredient
from stap import Stap

def main():
    # Recept 1: Kip Kerrie
    kip_kerrie = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes", 2)
    kip_kerrie.voeg_ingredient_toe(Ingredient("Kipdijfilet", 250, "gram", 239))
    kip_kerrie.voeg_ingredient_toe(Ingredient("gesneden ui", 75, "gram", 40))
    kip_kerrie.voeg_ingredient_toe(Ingredient("gehakte knoflook", 20, "gram", 149))
    kip_kerrie.voeg_ingredient_toe(Ingredient("kerrie masala", 10, "gram", 325))
    kip_kerrie.voeg_ingredient_toe(Ingredient("tomatenblokjes", 100, "gram", 18))
    kip_kerrie.voeg_ingredient_toe(Ingredient("zonnebloemolie", 25, "ml", 884))

    kip_kerrie.voeg_stap_toe(Stap("Doe de zonnebloemolie in de pan en verhit dit."))
    kip_kerrie.voeg_stap_toe(Stap("Bak de ui en knoflook totdat deze bruin worden."))
    kip_kerrie.voeg_stap_toe(Stap("Voeg de kerrie masala toe en roer goed door."))
    kip_kerrie.voeg_stap_toe(Stap("Voeg de tomatenblokjes en kip toe en laat sudderen."))

    # Recept 2: Wentelteefjes
    wentelteefjes = Recept("Wentelteefjes", "Zoet ontbijt van oud brood met ei en melk", 1)
    wentelteefjes.voeg_ingredient_toe(Ingredient("brood", 90, "gram", 265))
    wentelteefjes.voeg_ingredient_toe(Ingredient("ei", 2, "stuks", 155))
    wentelteefjes.voeg_ingredient_toe(Ingredient("melk", 200, "ml", 42))

    wentelteefjes.voeg_stap_toe(Stap("Kluts de eieren in een bord."))
    wentelteefjes.voeg_stap_toe(Stap("Meng melk en suiker in een kom."))
    wentelteefjes.voeg_stap_toe(Stap("Wentel het brood door het mengsel en bak goudbruin."))

    # Recept 3: Aardappelpuree
    aardappelpuree = Recept("Aardappelpuree", "Romige aardappelpuree", 3)
    aardappelpuree.voeg_ingredient_toe(Ingredient("aardappels", 500, "gram", 77))
    aardappelpuree.voeg_ingredient_toe(Ingredient("slagroom", 50, "ml", 345))
    aardappelpuree.voeg_ingredient_toe(Ingredient("roomboter", 25, "gram", 717))

    aardappelpuree.voeg_stap_toe(Stap("Schil en kook de aardappels gaar."))
    aardappelpuree.voeg_stap_toe(Stap("Stamp fijn met boter en slagroom."))
    aardappelpuree.voeg_stap_toe(Stap("Breng op smaak met peper en zout."))

    # Print recepten
    print(kip_kerrie)
    print(wentelteefjes)
    print(aardappelpuree)

if __name__ == "__main__":
    main()
