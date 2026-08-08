from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.9, 0.9, 0.9, 1)

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        
        titulo = Label(
            text="[b]Lickercorporation Calculator[/b]\n[i]Inovação nunca antes vista[/i]\n[size=14]Versão Beta v0.1[/size]",
            markup=True,
            color=(0, 0, 0, 1)
        )
        
        self.campo1 = TextInput(hint_text="Primeiro número", input_filter='float', multiline=False)
        self.campo2 = TextInput(hint_text="Segundo número", input_filter='float', multiline=False)
        
        botao = Button(text="Somar", background_color=(0, 0.7, 0.3, 1))
        botao.bind(on_press=self.calcular)
        
        self.resultado = Label(text="Resultado: ", color=(0, 0, 1, 1), bold=True)
        
        rodape = Label(text="Lickercorporation LTDA - 2026", color=(0.5, 0.5, 0.5, 1), font_size=12)
        
        layout.add_widget(titulo)
        layout.add_widget(self.campo1)
        layout.add_widget(self.campo2)
        layout.add_widget(botao)
        layout.add_widget(self.resultado)
        layout.add_widget(rodape)
        
        return layout

    def calcular(self, instance):
        try:
            n1 = float(self.campo1.text)
            n2 = float(self.campo2.text)
            self.resultado.text = f"O resultado é: {n1 + n2}"
        except ValueError:
            self.resultado.text = "Oxe, números inválidos!"

if __name__ == '__main__':
    MinhaApp().run()
