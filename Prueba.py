import flet as ft

def main(page: ft.Page):
    
    page.title = "Elementos básicos"

    Inicio = ft.Text("""Proyecto Hangman""", size=30, color="WHITE")
    fila = ft.Row([
        ft.Icon(ft.icons.PLAY_ARROW_SHARP, color="WHITE"),
        ft.Text("Jugar ", size=20),
        ft.Icon(ft.icons.EXIT_TO_APP, color="WHITE"),
        ft.Text("Salir "),
    ])

    reglas = ft.Column([
        ft.Text("""REGLAS:
      1. Tienes de 2 a 6 vidas para adivinar la palabra.(Dependiendo la dificultad)
      2. Si adivinas una letra se añadera.
      3. Si no adivinas una letra, se te restará un intento.
      4. Si adivinas la palabra, ¡ganas!
      5. Si te quedas sin intentos, pierdes""", size=15),
        fila,
    ])
    page.add(inicio, reglas)
    
ft.app(main)