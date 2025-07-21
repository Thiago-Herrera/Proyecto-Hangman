import flet as ft
import random

Vidas = 4

Palabras = [
    "Python",
    "Ordenador",
    "Duolingo",
    "Basicamente",
    "Agua",
    "Hola",
    "Pastel",
    "Mouse",
    
]
Palabra_a_adivinar = random.choice(Palabras)
espacios = ["_" for _ in Palabra_a_adivinar]  # Inicializa los espacios con guiones bajos

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

    def on_hover(e):
        """Cambia el color de fondo del botón al pasar el mouse sobre él."""
        e.control.bgcolor = ft.colors.GREEN if e.data == "true" else ft.colors.RED
        page.update()

    def llenar_fila_espacios(espacios):
        """Llena la fila de espacios con los caracteres de la palabra a adivinar."""
        return [
            ft.Container(
                content=ft.Text(
                    letra,
                    size=30,
                    color=ft.colors.WHITE,
                ),
                width=50,
                height=50,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER,
                border_radius=ft.border_radius.all(5),
            )
            for letra in espacios
        ]

    def check_letter(e):
        global Vidas
        letra_seleccionada = e.control.text
        if letra_seleccionada in Palabra_a_adivinar.upper():
            # Actualiza los espacios con la letra adivinada
            for i,letra_palabra in enumerate(Palabra_a_adivinar.upper()):
                if letra_palabra == letra_seleccionada:
                    espacios[i] = letra_palabra
            # Actualiza la fila de espacios
            fila_espacios.controls = llenar_fila_espacios(espacios)
            fila_espacios.update()
            
        else:
            Vidas=(Vidas)-1
            
            
        
    def teclas():
        items = []
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            items.append(
                ft.Container(
                    content=ft.TextButton(
                        text=i,
                        on_click=check_letter,
                        style=ft.ButtonStyle(color=ft.colors.WHITE),
                    ),
                    width=45,
                    height=45,
                    bgcolor=ft.colors.AMBER,
                    border_radius=ft.border_radius.all(5),
                    on_hover = on_hover,
                )
            ) 

        return items
    # elementos de la interfaz del juego
    # titulo
    titulo = ft.Text(
        "Juego del Ahorcado",
        size=30,
        color="WHITE",
        text_align=ft.TextAlign.CENTER,
    )# cambios
    # palabra a adivinar(en un inicio en blanco)
    fila_espacios = ft.Row(
        controls=llenar_fila_espacios(espacios),
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
                                  Teclado,
                                  ft.ElevatedButton
                                     ("Terminar juego", 
                                     on_click=go_home),
                                  
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