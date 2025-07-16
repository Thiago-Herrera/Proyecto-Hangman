import flet as ft
import random

Vidas = 4

Palabras = [
    "Python",
    "Java script",
    "Ordenador",
    "Duolingo",
    "Basicamente",
    "Agua",
    "Hola",
    "Pastel",
    "Mouse",
    
]
Palabra_a_adivinar = random.choice(Palabras)

def main(page: ft.Page):
    page.title = "Hagman"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "dark"
    page.window_width = 500
    page.window_min_width = 500


    def go_home(e):
        page.go("/")
        
    def go_reglas_y_mas(e):
        page.go("/reglas_y_mas")
    
    def go_juego(e):
        page.go("/juego")
    def check_letter(e):
        global Vidas
        # conocer la letra
        letra = e.control.text
        # verificar si la letra está en la palabra
        if letra in Palabra_a_adivinar.upper():
            # si la letra está en la palabra, se añade a las letras adivinadas
            if letra not in fila_espacios.controls:
                fila_espacios.controls.append(ft.Text(letra, size=30, color="WHITE"))
                fila_espacios.update()
        else:
            # si la letra no está en la palabra, se resta un intento

    def teclas():
        items = []
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            items.append(
                ft.Container(
                    content=ft.TextButton(
                        text=i,
                        on_click=check_letter,
                        style=ft.ButtonStyle(color=ft.colors.BLACK),
                    ),
                    width=45,
                    height=45,
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5),
                    on_hover=on_hover,
                )
            ) 

        return items
    # elementos del juego
    # titulo
    titulo = ft.Text(
        "Juego del Ahorcado",
        size=30,
        color="WHITE",
        text_align=ft.TextAlign.CENTER,
    )# cambios
    # palabra a adivinar(en un inicio en blanco)
    fila_espacios = ft.Row(
        [
            ft.Text("_", size=30, color="WHITE")
            for _ in range(len(Palabra_a_adivinar))  # Cambia 5 por la longitud de la palabra
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    # letras adivinadas ( el teclado)
    Teclado = ft.Row(
        wrap=True,
        spacing=5,
        run_spacing=6,
        controls=teclas(),
        width=page.window_width,
    )
    # vidas restantes
    # imagen del ahorcado


    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(ft.View(
                "/",
                [   
                    ft.Text("""Juego del ahorcado""", size=30, color="WHITE"),
                    ft.ElevatedButton("ir a reglas",
                                      on_click=go_reglas_y_mas),
                    ft.ElevatedButton("Jugar",
                                      on_click=go_juego,)
                    
                    ]
                ))
        elif page.route == "/reglas_y_mas":
            page.views.append(ft.View(
                "/about", 
                [
                ft.Text("""REGLAS:
                1. Tienes de 6 vidas para adivinar la palabra.
                2. Si adivinas una letra se añadera.
                3. Si no adivinas una letra, se te restará un intento.
                4. Si adivinas la palabra, ¡ganas!
                5. Si te quedas sin intentos, pierdes""",
                size=15
                ), 
                ft.ElevatedButton
                  ("Ir al inicio", 
                        on_click=go_home),
                
                ft.ElevatedButton("Jugar",
                        on_click=go_juego,)
                      ]
                    )
                 )
            
        elif page.route == "/juego":

            page.views.append(
                ft.View(
                    "/juego",
                    [
                      ft.Container(
                          width = 500,
                          height = 800,
                          padding = 10,
                          content = ft.Column(
                              [
                                  titulo,
                                  fila_espacios,
                              ]  
                            )
                          ),  
                    ]
                )
            )
        page.update()
    page.on_route_change = route_change
        
    page.go("/")

ft.app(main)