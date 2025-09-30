import sqlite3
from ingredient import Ingredient
from stap import Stap
from recept import Recept

DB_NAME = "recepten.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS recepten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT NOT NULL,
            omschrijving TEXT,
            aantal_personen INTEGER NOT NULL
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS ingredienten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recept_id INTEGER NOT NULL,
            naam TEXT NOT NULL,
            hoeveelheid REAL NOT NULL,
            eenheid TEXT NOT NULL,
            kcal_per_eenheid REAL NOT NULL,
            plantaardig_alternatief TEXT,
            FOREIGN KEY (recept_id) REFERENCES recepten(id) ON DELETE CASCADE
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS stappen (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recept_id INTEGER NOT NULL,
            beschrijving TEXT NOT NULL,
            tip TEXT,
            FOREIGN KEY (recept_id) REFERENCES recepten(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()

def sla_op_in_db(recept: Recept):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Recept
    c.execute(
        "INSERT INTO recepten (naam, omschrijving, aantal_personen) VALUES (?, ?, ?)",
        (recept.get_naam(), recept.get_omschrijving(), recept.get_aantal_personen())
    )
    recept_id = c.lastrowid

    # Ingrediënten
    for ing in recept.get_ingredienten():
        c.execute(
            """INSERT INTO ingredienten
               (recept_id, naam, hoeveelheid, eenheid, kcal_per_eenheid, plantaardig_alternatief)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (recept_id, ing.get_naam(), ing.get_hoeveelheid(), ing.get_eenheid(),
             ing.get_kcal_per_eenheid(), ing.get_plantaardig())
        )

    # Stappen
    for st in recept.get_stappen():
        c.execute(
            "INSERT INTO stappen (recept_id, beschrijving, tip) VALUES (?, ?, ?)",
            (recept_id, st.get_beschrijving(), st.get_tip())
        )

    conn.commit()
    conn.close()
    print(f"Recept '{recept.get_naam()}' opgeslagen in database (id {recept_id}).")

def laad_recepten_uit_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT id, naam, omschrijving, aantal_personen FROM recepten ORDER BY id")
    recepten_rows = c.fetchall()

    recepten = []
    for rid, naam, oms, personen in recepten_rows:
        r = Recept(naam, oms, personen)

        # Ingrediënten voor dit recept
        c.execute("""SELECT naam, hoeveelheid, eenheid, kcal_per_eenheid, plantaardig_alternatief
                     FROM ingredienten WHERE recept_id = ? ORDER BY id""", (rid,))
        for (ing_naam, hvh, eenheid, kcal_e, alt) in c.fetchall():
            r.voeg_ingredient_toe(Ingredient(ing_naam, hvh, eenheid, kcal_e, alt))

        # Stappen voor dit recept
        c.execute("""SELECT beschrijving, tip
                     FROM stappen WHERE recept_id = ? ORDER BY id""", (rid,))
        for (beschrijving, tip) in c.fetchall():
            r.voeg_stap_toe(Stap(beschrijving, tip))

        recepten.append(r)

    conn.close()
    return recepten
