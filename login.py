from kivy.app import App
import subprocess
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import client 

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(400, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        self.username_input = TextInput(hint_text='Username', size_hint=(None, None), size=(300, 40))
        self.password_input = TextInput(hint_text='Password', password=True, size_hint=(None, None), size=(300, 40))
        login_button = Button(text='Login', size_hint=(None, None), size=(300, 50))
        login_button.bind(on_press=self.login)

        layout.add_widget(Label(text='Login', font_size=20, size_hint_y=None, height=50))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # Check if username and password are correct
        reply = client.sendmessage(0,username,password)
        #if username == "sruj" and password == "sruj":
        if reply:
            print([0, username, password])
            self.proceed_to_client(username)  # Call proceed_to_client after successful login
        else:
            print("Login failed. Invalid username or password.")

    def proceed_to_client(self, username):
        subprocess.Popen(["python", "main.py", username])  # Open clientthree.py using subprocess

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super(SignupScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(400, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        self.username_input = TextInput(hint_text='Username', size_hint=(None, None), size=(300, 40))
        self.password_input = TextInput(hint_text='Password', password=True, size_hint=(None, None), size=(300, 40))
        signup_button = Button(text='Signup', size_hint=(None, None), size=(300, 50))
        signup_button.bind(on_press=self.signup)

        layout.add_widget(Label(text='Signup', font_size=20, size_hint_y=None, height=50))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(signup_button)
        self.add_widget(layout)
        

    def signup(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        # Implement signup functionality
        print(f"Signup: Username - {username}, Password - {password}")
        self.proceed_to_client(username)
    def proceed_to_client(self, username):
        subprocess.Popen(["python", "main.py", username])  # Open clientthree.py using subprocess

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(400, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        login_button = Button(text='Login', size_hint=(None, None), size=(300, 50))
        login_button.bind(on_press=self.switch_to_login)
        signup_button = Button(text='Signup', size_hint=(None, None), size=(300, 50))
        signup_button.bind(on_press=self.switch_to_signup)

        layout.add_widget(login_button)
        layout.add_widget(signup_button)
        self.add_widget(layout)

    def switch_to_login(self, instance):
        self.manager.current = 'login'

    def switch_to_signup(self, instance):
        self.manager.current = 'signup'

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        return sm

if __name__ == '__main__':
    TestApp().run()