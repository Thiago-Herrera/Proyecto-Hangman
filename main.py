


Dificultad = "dificil" # variable global

class Ahorcado:
    """
    Clase Ahorcado que representa el juego del ahorcado."""
    def __init__(self, intentos_maximos = 20): #<- parametro
        Dificultad = "facil"
        self.Nombre_Jugador = "" 
        self.Nombre_Ahocado = ""
        self.Dificultad = Dificultad # variable local
        self.intentos_maximos =  intentos_maximos
        self.Palabra_secreta = ""
        self.letras_usadas = []
        self.letras_adivinadas = []

ahorcado = Ahorcado() # Instancia de la clase Ahorcado
print(ahorcado.Dificultad) # Imprime la dificultad por defecto
print(Dificultad) # Imprime la dificultad global
print(ahorcado.__doc__)