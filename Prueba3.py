import flet as ft


def main(page: ft.Page):
    nombre = ft.TextField(label="Escribe tu nombre")
    apellido = ft.TextField(label="Escribe tu apellido")
    
    def saludar(e):
        saludo = ft.Text(f"Hola, {nombre.value} {apellido.value}!")
        page.add(saludo)
        page.update()

    boton = ft.ElevatedButton("Saludar", on_click=saludar)
    page.add(nombre, apellido, boton)

ft.app(main)