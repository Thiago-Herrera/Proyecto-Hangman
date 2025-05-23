import flet as ft



def main(page: ft.Page):
    # Campo para ingresar edad
    edad_input = ft.TextField(label="Ingresa tu edad")
    
    page.title = "Ingresar edad"
    
    # Texto para mostrar el resultado
    resultado_texto = ft.Text(value="")
  
    def verificar_edad(e):
        try:
            edad = int(edad_input.value)
            if edad < 18:
                resultado_texto.value = "Eres menor de edad"
            else:
                resultado_texto.value = "Eres mayor de edad"
        except ValueError:
            resultado_texto.value = "Por favor ingresa un número válido"
        page.update()

    # Botón para verificar edad
    verificar_Edad = ft.ElevatedButton(text="Verificar", on_click=verificar_edad)

    # Agregar elementos a la página
    page.add(edad_input, verificar_Edad, resultado_texto)

# Ejecutar la aplicación
ft.app(main)