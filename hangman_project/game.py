class HangmanGame:
    """Guarda el estado de una partida y su lógica."""

    def __init__(self, word):
        """Crea la partida con la palabra recibida."""
        self.word = word
        self.guessed_letters = []
        self.errors = 0
        self.max_errors = 6

    def display_progress(self):
        """Devuelve la palabra con _ en las letras no adivinadas."""
        progress = ""
        for char in self.word:
            if not char.isalpha() or char in self.guessed_letters:
                progress += char
            else:
                progress += "_"
        return progress

    def process_guess(self, letter):
        """Registra la letra. Devuelve True si está en la palabra."""
        self.guessed_letters.append(letter)
        if letter in self.word:
            return True
        self.errors += 1
        return False

    def is_won(self):
        """Devuelve True si no quedan letras ocultas."""
        return "_" not in self.display_progress()

    def is_lost(self):
        """Devuelve True si se llegó al máximo de errores."""
        return self.errors >= self.max_errors

    def correct_letters(self):
        """Devuelve la lista de letras probadas que están en la palabra."""
        correctas = []
        for letter in self.guessed_letters:
            if letter in self.word:
                correctas.append(letter)
        return correctas

    def wrong_letters(self):
        """Devuelve la lista de letras probadas que no están en la palabra."""
        incorrectas = []
        for letter in self.guessed_letters:
            if letter not in self.word:
                incorrectas.append(letter)
        return incorrectas