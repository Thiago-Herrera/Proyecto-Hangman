import flet as ft


def main(page: ft.Page):
    page.title = "Hagman Game"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "light"
    page.window_width = 500
    page.window_min_width = 500


    def go_home(e):
        page.go("/")
        

    def go_reglas_y_mas(e):
        page.go("/reglas_y_mas")
    
    def go_juego(e):
        page.go("/juego")

    def keyboard_items():
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
    )
    # palabra a adivinar(en un inicio en blanco)
    fila_espacios = ft.Row(
        [
            ft.Text("_", size=30, color="WHITE")
            for _ in range(len(word))  # Cambia 5 por la longitud de la palabra
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    # letras adivinadas ( el teclado)
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
                    [ ft.Container(
                        content=ft.Column(
                            [
                                titulo,
                                fila_espacios,
                                
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        bgcolor=ft.colors.BLACK,
                        padding=20,
                        border_radius=ft.border_radius.all(10)
                    )
                    ]
                )
            )
        page.update()
    page.on_route_change = route_change
        
    page.go("/")

ft.app(main)