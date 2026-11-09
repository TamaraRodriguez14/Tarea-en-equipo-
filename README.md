Juego del Ahorcado en Python

Integrantes: 
* Guillermo Borges
* Victoria Amaro
* Tamara Rodriguez

---

**¿De qué trata?**
Es el clásico juego del ahorcado ejecutado desde la consola. El juego selecciona una palabra o frase al azar desde un archivo `.txt` y el jugador tiene un límite de **6 errores** para adivinarla.

**Reglas**
* Solo se permite ingresar letras.
* Si el texto tiene caracteres especiales o espacios, se muestran automáticamente.
* Si te equivocas de letra, restas un intento.
* Ganas si completas la palabra antes de llegar a 6 errores.

---

**Estructura del proyecto**

* `main.py`: Punto de entrada del programa (bucle principal).
* `game.py`: Contiene la clase `HangmanGame` con la lógica del juego.
* `utils.py`: Funciones auxiliares para validar inputs y mostrar pantalla.
* `wordlist.txt`: Lista de palabras o frases para el juego.
* `README.md`: Documentación e instrucciones.

---

## Cómo ejecutarlo

1. Asegúrate de tener instalado Python 3.
2. Abre la terminal en la carpeta del proyecto.
3. Corre el siguiente comando:

```bash
python main.py
