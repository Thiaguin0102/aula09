import flet as ft

def main(window:  ft.Page):
    window.title = 'Calculadora IMC'
    window.theme_mode = 'dark'

    # Função do calculo IMC
    def exibir_imc(event):
        altura_digitado = float(txt_altura.value)
        peso_digitado = float(txt_peso.value)
        txt_resultado.value = f'O IMC é {peso_digitado / (altura_digitado ** 2):.2f}'
        
        window.update()

    # Altura IMC
    altura = ft.Text(value='Altura',  color='blue')
    txt_altura = ft.TextField(bgcolor=ft.colors.WHITE, color='black')
    
    # Peso IMC    
    peso = ft.Text(value='Peso',  color='blue')
    txt_peso = ft.TextField(bgcolor=ft.colors.WHITE, color='black')
    
    #Resultado IMC
    txt_resultado = ft.Text(value='')
    btn_enviar = ft.ElevatedButton(
        text='enviar',
        on_click=exibir_imc)

    window.update()
    window.add(altura,
                txt_altura,
                peso,
                txt_peso,
                btn_enviar, 
                txt_resultado)

ft.app(target=main) 