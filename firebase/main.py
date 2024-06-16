from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.core.window import Window
import firebase_admin
import requests
from firebase import firebase
from firebase_admin import credentials, auth
import pyrebase 
from kivy.utils import get_color_from_hex

firebaseConfig = {
  'apiKey': "AIzaSyD78VYoSnuIRMqvXnObpym7AGuPC3YzICc",
  'authDomain': "login-jhonatan.firebaseapp.com",
  'databaseURL': "https://login-jhonatan-default-rtdb.firebaseio.com",
  'projectId': "login-jhonatan",
  'storageBucket': "login-jhonatan.appspot.com",
  'messagingSenderId': "587467204708",
  'appId': "1:587467204708:web:4eded7ad8140427052d771",
  'measurementId': "G-W4V64MM0VW"};

firebas=pyrebase.initialize_app(firebaseConfig)
auth=firebas.auth()

Window.clearcolor = get_color_from_hex('e4f5f4')
class Gerenciador(ScreenManager):
   pass

class Logado (Screen):
   pass

class Cadastro(Screen):
   pass

class Login(Screen):
   pass

class Login(App):
    def build(self):
        return Builder.load_file('main.kv')
    
    def Cadastrar(self):
      email = self.root.get_screen('cadastro').ids.email.text 
      senha = self.root.get_screen('cadastro').ids.senha.text

      try:
         user = auth.create_user_with_email_and_password(email, senha)
      except:
         self.root.get_screen('cadastro').ids.erro.color = (1,0,0,1)
      else:
         self.root.current = 'login'

    def log(self):
      email = self.root.get_screen('login').ids.email.text
      senha = self.root.get_screen('login').ids.senha.text
      try:
         auth_result = auth.sign_in_with_email_and_password(email, senha)
      except:
         self.root.get_screen('login').ids.l.color = (1, 0, 0, 1)
      else:
         self.root.current = 'Logado'



if __name__ == "__main__":
 Login().run()