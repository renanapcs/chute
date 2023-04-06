import random
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class ChuteCerto(App):
    def build(self):
        self.numero_aleatorio = random.randint(1, 100)
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Chute um número entre 1 e 100:', font_size=30)
        self.text_input = TextInput(font_size=30)
        self.button = Button(text='Chute!', font_size=30)
        self.button.bind(on_press=self.chuteNumero)
        self.novo_jogo_button = Button(text='Jogar de Novo', font_size=30, opacity=0)
        self.novo_jogo_button.bind(on_press=self.novoJogo)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.novo_jogo_button)
        return self.layout


    def chuteNumero(self, button):
        numero_input = self.text_input.text.strip()
        if not numero_input:
            self.label.text = "Você precisa digitar um numero valido."
        else:
            numero_input = int(self.text_input.text)
            if self.numero_aleatorio == numero_input:
                self.label.text = "Parabéns, você acertou!"
                self.novo_jogo_button.opacity = 1
            
            elif numero_input > self.numero_aleatorio:
                self.label.text = "Um pouco menor"
            else:
                self.label.text = "Um pouco maior"


    def novoJogo(self, button):
        self.numero_aleatorio = random.randint(1, 100)
        self.label.text = 'Chute um numero'
        self.text_input.text = ''
        self.novo_jogo_button.opacity = 0



chute = ChuteCerto()
chute.run()
