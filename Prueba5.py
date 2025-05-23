import flet as ft


def main(page: ft.Page):
    def go_home(e):
        page.go("/")
        

    def go_reglas_y_mas(e):
        page.go("/reglas_y_mas")
    
    def go_juego(e):
        page.go("/juego")

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(ft.View(
                "/",
                [   
                    ft.Text("""Proyecto Hangman""", size=30, color="WHITE"),
                    ft.ElevatedButton("ir a reglas y mas informacion",
                                      on_click=go_reglas_y_mas),
                    ft.ElevatedButton("Iniciar Juego",
                                      on_click=go_juego,)
                    
                    ]
                ))
        elif page.route == "/reglas_y_mas":
            page.views.append
            (ft.View(
                "/about", 
                [
                ft.Text("""REGLAS:
                1. Tienes de 2 a 6 vidas para adivinar la palabra.(Dependiendo la dificultad)
                2. Si adivinas una letra se añadera.
                3. Si no adivinas una letra, se te restará un intento.
                4. Si adivinas la palabra, ¡ganas!
                5. Si te quedas sin intentos, pierdes""",
                size=15
                ), 
                ft.ElevatedButton
                  (
                        "Ir al inicio", 
                        on_click=go_home
                            )
                      ]
                    )
                 )
            page.update()
        elif page.route == "/juego":
            ft.Text(""),
            page.views.append
            ft.ElevatedButton(
                "Ir al inicio",
                on_click=go_home
                                ),
    page.on_route_change = route_change
        
    page.go("/")

ft.app(main)