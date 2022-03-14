from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from firebaseconnection import OpenFireBaseConnection
from trainImages import FaceTrainer
import frontendLogin
# import frontendauth
class WindowManager(ScreenManager):
    pass
class MainWindowLogin(Screen):
    def get_text(self):
        print(self.getemail.text)
        print(self.getpassword.text)
class MainWindowSignup(Screen):
    def get_text(self):
        firebase = OpenFireBaseConnection()
        auth_control = firebase.createuserbyemail(self.getemail.text,self.getpassword.text,self.getconfirmpassword.text)
        print(self.getemail.text)
        print("-----",self.getpassword.text)
        print("---mafa---",self.getconfirmpassword.text)
        # print(self.getpassword.text==self.getconfirmpassword.text)
        if(auth_control==True):
            print("created")
            # frontendLogin.Login().run()
            # frontendauth.
        else:
            self.getemail.text=""
            self.getpassword.text=""
            self.getconfirmpassword.text=""
            print("not created")
# class DetaisCollector(Screen):
#     def get_text(self):
#         print(self.get_reg_no.text)
#         print(self.get_name.text)
#         print(self.get_role.text)
#         print(self.get_year.text)
#         print(self.get_sem.text)
#         print(self.get_department.text)
#         print(self.get_section.text)
kv = """
WindowManager:
    MainWindowSignup:
<MainWindowSignup>:
    getemail:Email
    getpassword:password
    getconfirmpassword:confirmpassword
    MDToolbar:
        title: 'Signup'
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
    MDTextField:
        id: confirmpassword
        hint_text: "Confirmpassword"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        text: "SignUP"
        on_release:
            root.get_text()
<MainWindowLogin>:
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
class Signup(MDApp):
    def build(self):
        self.root = Builder.load_string(kv)


if __name__ == "__main__":
    Signup().run()