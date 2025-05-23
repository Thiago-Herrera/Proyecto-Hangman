import flet as ft



def main(page: ft.Page):
    
    contador = 0
    texto_contador = ft.Text(value="El botón ha sido presionado 0 veces.")
    
    def button_clicked(e):
        nonlocal contador
        contador = contador + 1
        texto_contador.value = f"El botón ha sido presionado {contador} veces."
        page.update()

    boton = ft.ElevatedButton(text="Presióname", on_click=button_clicked)
    page.add(boton, texto_contador)

ft.app(main)