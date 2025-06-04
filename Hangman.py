import flet as ft

Vidas = 4

def main(page: ft.Page):
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
                    border_radius=ft
                            )
                )
    
    def new_game(e):
        global word
        global spaces
        global lives
        lose.open = False
        win.open = False
        page.update()
        lives = 6
        word = random.choice(animals)
        spaces = ["_"] * len(word)
        row_spaces.controls = generatespaces(spaces)
        row_spaces.update()
        hangman_image.src = f"assets/{hangman_pics[6-lives]}"
        hangman_image.update()
    
    def check_letter(e):
        
        global Vidas #Hago "Vidas" global
        key_pressed = e.control.text #Guarda la letra que se undio
        existe_letra = False 
        for idx, caracter in enumerate(word):
            if caracter == key_pressed:
                spaces[idx] = key_pressed
                existe_letra = True
                row_spaces.controls = generatespaces(spaces)
                row_spaces.update()
        if not existe_letra:
            lives = lives - 1
            hangman_image.src = f"assets/{hangman_pics[6-lives]}"
            page.update()
        if "_" not in spaces:
            page.dialog = win
            win.open = True
            page.update()
        if lives == 0:
            page.dialog = lose
            lose.open = True
            page.update()
    
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
                         ft.ElevatedButton("Q",
                        on_click=go_home,),
                          ft.ElevatedButton("W",
                        on_click=go_home,),
                          ft.ElevatedButton("E",
                        on_click=go_home,),
                          ft.ElevatedButton("R",
                        on_click=go_home,),
                          ft.ElevatedButton("T",
                        on_click=go_home,),
                          ft.ElevatedButton("Y",
                        on_click=go_home,),
                          ft.ElevatedButton("U",
                        on_click=go_home,),
                          ft.ElevatedButton("I",
                        on_click=go_home,),
                          ft.ElevatedButton("O",
                        on_click=go_home,),
                          ft.ElevatedButton("P",
                        on_click=go_home,),
                          ft.ElevatedButton("A",
                        on_click=go_home,),
                          ft.ElevatedButton("S",
                        on_click=go_home,),
                          ft.ElevatedButton("D",
                        on_click=go_home,),
                          ft.ElevatedButton("F",
                        on_click=go_home,),
                          ft.ElevatedButton("G",
                        on_click=go_home,),
                          ft.ElevatedButton("H",
                        on_click=go_home,),
                          ft.ElevatedButton("J",
                        on_click=go_home,),
                          ft.ElevatedButton("K",
                        on_click=go_home,),
                          ft.ElevatedButton("L",
                        on_click=go_home,),
                          ft.ElevatedButton("Ñ",
                        on_click=go_home,),
                          ft.ElevatedButton("Z",
                        on_click=go_home,),
                          ft.ElevatedButton("X",
                        on_click=go_home,),
                          ft.ElevatedButton("C",
                        on_click=go_home,),
                          ft.ElevatedButton("V",
                        on_click=go_home,),
                          ft.ElevatedButton("B",
                        on_click=go_home,),
                          ft.ElevatedButton("N",
                        on_click=go_home,),
                          ft.ElevatedButton("M",
                        on_click=go_home,),
                    ]
                )
            )
        page.update()
    page.on_route_change = route_change
        
    page.go("/")

ft.app(main)