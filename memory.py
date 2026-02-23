import os
from datetime import date, datetime
from random import randint
from configparser import RawConfigParser

FILENAME = "code.txt"
config = RawConfigParser()

config_file = "hour.cfg"
if not os.path.exists(config_file):
    with open(config_file, "w") as f:
        pass

config.read(config_file)

if not config.has_section("HOUR"):
    config.add_section("HOUR")

if not config.has_option("HOUR", "Morning"):
    config.set("HOUR", "Morning", "0")

if not config.has_option("HOUR", "Evening"):
    config.set("HOUR", "Evening", "18")

with open(config_file, "w") as f:
    config.write(f)

MORNING_HOUR = int(config["HOUR"]["Morning"])
EVENING_HOUR = int(config["HOUR"]["Evening"])


def get_today_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_current_hour():
    return datetime.now().hour


def generate_code():
    return randint(0, 10**6 - 1)


def read_last_entry():
    if not os.path.exists(FILENAME):
        return None, None

    with open(FILENAME, "r") as file:
        lines = file.readlines()
        if not lines:
            return None, None
        last_line = lines[-1].strip().split(": ")
        if len(last_line) != 2:
            return None, None
        return last_line[0], last_line[1]


def write_new_entry(code):
    with open(FILENAME, "a") as file:
        file.write(f"{get_today_date()}: {code}\n")


def morning_routine():
    today, last_code = read_last_entry()
    if today and today.startswith(date.today().strftime("%Y-%m-%d")):
        print(f"Le numéro du jour a déjà été généré")
    else:
        new_code = generate_code()
        write_new_entry(new_code)
        print(f"Numéro du jour : {new_code}")


def evening_routine():
    today, last_code = read_last_entry()
    if not today or not today.startswith(date.today().strftime("%Y-%m-%d")):
        print(
            "Aucun code généré aujourd'hui. Relancez le programme après 9h pour générer un nouveau code."
        )
        return

    while True:
        user_input = input(
            "Entrez le code du matin (ou tapez 'abandon' pour le révéler) : "
        )
        if user_input.lower() == "abandon":
            print(f"Le code était : {last_code}")
            break
        elif user_input == last_code:
            print("Bravo ! Vous avez trouvé le bon code.")
            break
        else:
            print("Incorrect, essayez encore.")


if __name__ == "__main__":
    current_hour = get_current_hour()
    if current_hour >= EVENING_HOUR:
        evening_routine()
    elif current_hour >= MORNING_HOUR:
        morning_routine()
    else:
        print(f"Il est trop tôt, relancez après {MORNING_HOUR}h pour obtenir un code.")

    input("Appuyez sur n'importe quelle touche pour quitter...")
