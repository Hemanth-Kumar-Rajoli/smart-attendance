from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
class WindowManager(ScreenManager):
    pass
class MainWindow(Screen):
    def get_text(self):
        print(self.getemail.text)
        print(self.getpassword.text)
kv = """
WindowManager:
    MainWindow:
<MainWindow>:
    getemail:Email
    getpassword:password
    MDToolbar:
        title: 'Login'
        pos_hint: {"top": 1}
    MDTextField:
        id: Email
        hint_text: "Email"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
    MDTextField:
        id: password
        hint_text: "Password"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.4, 'center_y': 0.3}
        text: "LOGIN"
        on_release:
            root.get_text()
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.6, 'center_y': 0.3}
        text: "BACK"
        on_release:
            app.root.current="MainWindow"
"""
class Login(MDApp):
    def build(self):
        self.root = Builder.load_string(kv)


if __name__ == "__main__":
    Login().run()