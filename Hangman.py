import os
import flet as ft
import random

imagen_0 = os.path.join(os.path.dirname(__file__), "Images", "pixil-frame-0.png")
imagen_1 = os.path.join(os.path.dirname(__file__), "Images", "pixil-frame-1.png")
imagen_2 = os.path.join(os.path.dirname(__file__), "Images", "pixil-frame-2.png")
imagen_3 = os.path.join(os.path.dirname(__file__), "Images", "pixil-frame-3.png")
imagen_4 = os.path.join(os.path.dirname(__file__), "Images", "pixil-frame-4.png")
imagen_5 = os.path.join(os.path.dirname(__file__), "Images", "pixil-frame-5.png")
imagen_6 = os.path.join(os.path.dirname(__file__), "Images", "pixil-frame-6.png")

Vidas = 6

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
espacios = ["_" for _ in Palabra_a_adivinar]  # Inicializa los espacios con guiones bajos

def main(page: ft.Page):
    page.title = "Hagman"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "dark"
    page.window_width = 1000
    page.window_min_width = 1000
    
    imagen_actual = imagen_0

    def go_home(e):
        page.go("/")
        
    def go_reglas_y_mas(e):
        page.go("/reglas_y_mas")
    
    def go_juego(e):
        page.go("/juego")
        
    def new_game_win(e):
        # Reinicia el juego
        global Vidas, Palabra_a_adivinar, espacios
        Vidas = 6
        Palabra_a_adivinar = random.choice(Palabras)
        espacios = ["_" for _ in Palabra_a_adivinar]
        fila_espacios.controls = llenar_fila_espacios(espacios)
        page.close(win)
        page.update()
        
    def new_game_lose(e):
        # Reinicia el juego
        global Vidas, Palabra_a_adivinar, espacios
        Vidas = 6
        vidas_restantes.value = f"Vidas Restantes = {Vidas}"
        vidas_restantes.update()
        Palabra_a_adivinar = random.choice(Palabras)
        espacios = ["_" for _ in Palabra_a_adivinar]
        fila_espacios.controls = llenar_fila_espacios(espacios)
        page.close(lose)
        page.update()
        
    def close_dgl_win(e):
        page.close(win)
        page.window.destroy()
    
    def close_dgl_lose(e):
        page.close(lose)
        page.window.destroy()

    def on_hover(e):
        """Cambia el color de fondo del botón al pasar el mouse sobre él."""
        e.control.bgcolor = ft.colors.BACKGROUND if e.data == "true" else ft.colors.BACKGROUND
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
                bgcolor=ft.colors.BLACK54,
                border_radius=ft.border_radius.all(5),
            )
            for letra in espacios
        ]

    def check_letter(e):
        global Vidas
        global imagen_actual
        letra_seleccionada = e.control.text
        if letra_seleccionada in Palabra_a_adivinar.upper():
            # Actualiza los espacios con la letra adivinada
            for i,letra_palabra in enumerate(Palabra_a_adivinar.upper()):
                if letra_palabra == letra_seleccionada:
                    espacios[i] = letra_palabra
            # Actualiza la fila de espacios
            fila_espacios.controls = llenar_fila_espacios(espacios)
        else:
            Vidas=(Vidas)-1
            vidas_restantes.value = f"Vidas Restantes = {Vidas}"
            vidas_restantes.update()
            if Vidas == 6:
                imagen_actual = imagen_0
        
            elif Vidas == 5:
                imagen_actual = imagen_1
        
            elif Vidas == 4:
                imagen_actual = imagen_2
        
            elif Vidas == 3:
                imagen_actual = imagen_3
    
            elif Vidas == 2:
                imagen_actual = imagen_4
    
            elif Vidas == 1:
                imagen_actual = imagen_5
    
            elif Vidas == 0:
                imagen_actual = imagen_6
            imagen.src = imagen_actual
            imagen.src = f"images/pixil-frame-{6-Vidas}.png"
            imagen.update()
            
        #si se gana el juego
        if  "_" not in espacios:
            #print("You, Win!")
            page.open(win)
            page.update()

        #si se pierde el juego
        if Vidas == 0:
            page.open(lose)
            page.update()
            
            
        
    def teclas():
        items = []
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            items.append(
                ft.Container(
                    content=ft.TextButton(
                        text=i,
                        on_click=check_letter,
                        style=ft.ButtonStyle(color=ft.colors.WHITE),
                    ),
                    width=45,
                    height=45,
                    bgcolor=ft.colors.BLACK,
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
    vidas_restantes = (
        ft.Text(
           f"Vidas Restantes = {Vidas}"
        )
    )

     
    
    # imagen del ahorcado
    imagen = ft.Image(
        src=imagen_actual,
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )
    
    
    
    #Ganar
    win = ft.AlertDialog(       
        modal=True,
        title=ft.Text("Ganaste"),
        content=ft.Text("¿Quieres jugar de nuevo?"),
        actions=[
            ft.TextButton("Si", on_click=new_game_win),
            ft.TextButton("No", on_click=close_dgl_win),
        ],
    )
    #perder
    lose = ft.AlertDialog(
        modal=True,
        title=ft.Text("Perdiste"),
        content=ft.Text("¿Quieres jugar de nuevo?"),
        actions=[
            ft.TextButton("Si", on_click=new_game_lose),
            ft.TextButton("No", on_click=close_dgl_lose),
        ],)
        
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
                                  imagen,
                                  fila_espacios,
                                  Teclado,
                                  ft.ElevatedButton
                                            ("Terminar Juego", 
                                    on_click=go_home),
                                  vidas_restantes
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