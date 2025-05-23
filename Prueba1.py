import flet as ft

def main(page: ft.Page):
    count = ft.Text(value="0")

    def increment(e):
        count.value = str(int(count.value) + 1)#cambiar el estado
        page.update()
    
    def decrement(e):
        count.value = str(int(count.value) - 1)#cambiar el estado
        page.update()
    
    def reset
 
    page.add(
        ft.Row([
            ft.ElevatedButton(text="+", on_click=increment),
            
             ft.ElevatedButton(text="-", on_click=decrement),
            count
        ])
    )

ft.app(main)