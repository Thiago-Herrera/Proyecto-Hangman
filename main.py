




class Ahorcado:
    def __init__(self, Dificultad = "Normal", intentos_maximos = 20): #<- parametro
        self.Nombre_Jugador = "" 
        self.Nombre_Ahocado = ""
        self.Dificultad = Dificultad
        self.intentos_maximos =  intentos_maximos
        self.Palabra_secreta = ""
        self.letras_usadas = []
        self.letras_adivinadas = []
Ahorcado()