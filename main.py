from recept import Recept
from ingredient import Ingredient
from stap import Stap

def main():
    # Recept 1: Kip Kerrie
    kip_kerrie = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    kip_kerrie.voeg_ingredient_toe(Ingredient("Kipdijfilet", 250, "gram"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("gesneden ui", 75, "gram"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("gehakte knoflook", 20, "gram"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("kerrie masala", 0.75, "eetlepels"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("gehakte tomatenblik", 0.25, "blik"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("zonnebloemolie", 25, "milliliter"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("gemalen komijn", 0.5, "theelepels"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("zout", 0.5, "theelepels"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("maggiblokje", 0.25, "blokje"))
    kip_kerrie.voeg_ingredient_toe(Ingredient("water", 31.25, "milliliter"))

    kip_kerrie.voeg_stap_toe(Stap("Doe de zonnebloemolie in de pan en verhit dit."))
    kip_kerrie.voeg_stap_toe(Stap("Bak de ui en knoflook totdat deze bruin worden."))
    kip_kerrie.voeg_stap_toe(Stap("Voeg de kerrie masala toe en snijd ondertussen de kip."))
    kip_kerrie.voeg_stap_toe(Stap("Blus af met tomaten uit blik."))
    kip_kerrie.voeg_stap_toe(Stap("Voeg de kip toe en laat sudderen."))
    kip_kerrie.voeg_stap_toe(Stap("Na 10 minuten water, zout en maggiblokje toevoegen."))
    kip_kerrie.voeg_stap_toe(Stap("Kook door totdat de kip gaar is en serveer met rijst."))

    # Recept 2: Wentelteefjes
    wentelteefjes = Recept("Wentelteefjes", "Zoete ontbijt van oud brood met ei en melk")
    wentelteefjes.voeg_ingredient_toe(Ingredient("brood", 3, "sneetjes"))
    wentelteefjes.voeg_ingredient_toe(Ingredient("ei", 2, "stuks"))
    wentelteefjes.voeg_ingredient_toe(Ingredient("melk", 250, "milliliter"))
    wentelteefjes.voeg_ingredient_toe(Ingredient("gemalen kaneel", 2, "gram"))
    wentelteefjes.voeg_ingredient_toe(Ingredient("suiker", 50, "gram"))

    wentelteefjes.voeg_stap_toe(Stap("Kluts de eieren in een bord."))
    wentelteefjes.voeg_stap_toe(Stap("Meng melk, kaneel en suiker."))
    wentelteefjes.voeg_stap_toe(Stap("Wentel brood in het melkmengsel en daarna door het ei."))
    wentelteefjes.voeg_stap_toe(Stap("Bak de sneetjes in boter tot ze krokant zijn."))

    # Recept 3: Aardappelpuree
    aardappelpuree = Recept("Aardappelpuree", "Romige aardappelpuree")
    aardappelpuree.voeg_ingredient_toe(Ingredient("aardappels", 500, "gram"))
    aardappelpuree.voeg_ingredient_toe(Ingredient("water", 1, "liter"))
    aardappelpuree.voeg_ingredient_toe(Ingredient("zout", 1, "theelepel"))
    aardappelpuree.voeg_ingredient_toe(Ingredient("zwarte peper", 0.5, "theelepel"))
    aardappelpuree.voeg_ingredient_toe(Ingredient("nootmuskaat", 0.5, "theelepel"))
    aardappelpuree.voeg_ingredient_toe(Ingredient("slagroom", 50, "milliliter"))
    aardappelpuree.voeg_ingredient_toe(Ingredient("roomboter", 25, "gram"))

    aardappelpuree.voeg_stap_toe(Stap("Schil en snijd de aardappels in stukken."))
    aardappelpuree.voeg_stap_toe(Stap("Kook de aardappels gaar in water met zout."))
    aardappelpuree.voeg_stap_toe(Stap("Giet af en pureer de aardappels."))
    aardappelpuree.voeg_stap_toe(Stap("Voeg slagroom en boter toe en roer tot puree."))
    aardappelpuree.voeg_stap_toe(Stap("Breng op smaak met peper en nootmuskaat."))

    # Print alle recepten
    print(kip_kerrie)
    print(wentelteefjes)
    print(aardappelpuree)

if __name__ == "__main__":
    main()

