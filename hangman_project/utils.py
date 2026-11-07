import random


def get_random_word(archivo="wordlist.txt"):
    """Lee wordlist.txt y devuelve una palabra al azar en minúsculas."""
    with open(archivo, "r", encoding="utf-8") as f:
        palabras = [linea.strip() for linea in f if linea.strip()]
    return random.choice(palabras).lower()


def show_status(juego):
    """Muestra el progreso, las letras probadas y los intentos restantes."""
    print(juego.display_progress())
    print(f"Correctas: {', '.join(juego.correct_letters())}")
    print(f"Incorrectas: {', '.join(juego.wrong_letters())}")
    print(f"Intentos restantes: {juego.max_errors - juego.errors}")

    