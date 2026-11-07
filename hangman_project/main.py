#!/usr/bin/python3
from game import HangmanGame
from utils import get_random_word, show_status


def main():
    print("¡Bienvenido al Ahorcado!")
    palabra = get_random_word()
    juego = HangmanGame(palabra)
    show_status(juego)

    while True:
        letter = input("Ingresa una letra: ").strip().lower()

        if not letter.isalpha():
            print("Error: Solo se permiten letras.")
            continue
        elif len(letter) != 1:
            print("Error: Debes ingresar exactamente una letra.")
            continue
        elif letter in juego.guessed_letters:
            print(f"Error: Ya intentaste la letra '{letter}'.")
            continue

        if juego.process_guess(letter):
            print("¡Acertaste!")
        else:
            print("Letra incorrecta.")

        show_status(juego)

        if juego.is_won():
            print("¡Ganaste!")
            break
        if juego.is_lost():
            print(f"Perdiste. La palabra era: {juego.word}")
            break


if __name__ == "__main__":
    main()