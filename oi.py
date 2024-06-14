import kivy
from kivy.lang import Builder
from kivy.uix.scrollview import  ScrollView
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import firebase_admin
from firebase_admin import credentials
import pyrebase



cred = credentials.Certificate("oi.json")
firebase_admin.initialize_app(cred)



class logapp(App):
    def build(self):
        self.layout = FloatLayout()

        Window.clearcolor = (get_color_from_hex('d9fcfb'))

        



        self.img = AsyncImage(source = 'gu.png',
                              size_hint = (0.25, 0.25),
                              pos_hint = ({'center_x':0.5, 'center_y': 0.7}))

        self.nome = TextInput(hint_text = 'nome',
                         hint_text_color = get_color_from_hex('183837'),
                         background_color = get_color_from_hex('8df0ec'),
                         size_hint = (0.5, 0.05),
                         pos_hint = ({'center_x':0.5, 'center_y':0.435}))

        self.email = TextInput(hint_text = 'email',
                         hint_text_color = get_color_from_hex('183837'),
                         background_color = get_color_from_hex('8df0ec'),
                         size_hint = (0.5, 0.05),
                         pos_hint = ({'center_x':0.5, 'center_y':0.387}))
        
        self.senha = TextInput(hint_text = 'senha',
                         hint_text_color = get_color_from_hex('183837'),
                         background_color = get_color_from_hex('8df0ec'),
                         size_hint = (0.5, 0.05),
                         pos_hint = ({'center_x':0.5, 'center_y':0.340}))
        
        self.logi = Button(text = 'login',
                           color = get_color_from_hex('8df0ec'),
                           background_normal = 'None',
                           background_color = get_color_from_hex('183837'),
                           size_hint = (0.15, 0.05),
                           pos_hint = ({'center_x':0.3245, 'center_y': 0.25}))
        
        self.logi.bind(on_press=lambda x: self.escrever(self.nome.text, self.email.text, self.senha.text))

        self.reg = Button(text = 'registrar',
                           color = get_color_from_hex('8df0ec'),
                           background_normal = 'None',
                           background_color = get_color_from_hex('183837'),
                           size_hint = (0.15, 0.05),
                           pos_hint = ({'center_x':0.675, 'center_y': 0.25}))

        self.reg.bind (on_press=lambda x: self.ler())
        

        self.layout.add_widget(self.img)
        self.layout.add_widget(self.nome)
        self.layout.add_widget(self.email)
        self.layout.add_widget(self.senha)
        self.layout.add_widget(self.logi)
        self.layout.add_widget(self.reg)
        return self.layout

    def escrever(self, nome, email, senha):
        data = {"nome": nome, "email": email, "senha": senha}
        self.database.child("users").push(data)

    def ler(self):
        users = self.database.child("users").get()
        for user in users.each():
            print(user.val())


        

if __name__ == '__main__':
    logapp().run()