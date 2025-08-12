""" 
✅ *Exercício 3*

Crie um app que leia a largura e altura de uma parede (em metros), 
calcule a área e informe quantos litros de tinta são necessários para pintá-la 
(cada litro cobre 2m²).
"""
import flet as ft

def main(page: ft.Page):
    def calcular_area(e):
        valor01 = campo_largura.value
        valor02 = campo_altura.value
        
        if valor01 and valor01.isdigit() and valor02 and valor02.isdigit():
            largura = float(valor01)
            altura = float(valor02)
            area = largura * altura
            resultado.value = f"A área da parede é {area}m²"
            page.update()
        else:
            resultado.value = "Por favor, digite um número válido."
            page.update() 

    campo_largura = ft.TextField(
        label="Largura",
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    
    campo_altura = ft.TextField(
        label="Altura",
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    
    botao = ft.ElevatedButton("Calcular área", on_click=calcular_area)
    
    resultado = ft.Text()

    page.add(campo_largura, campo_altura, botao, resultado)

ft.app(target=main)

