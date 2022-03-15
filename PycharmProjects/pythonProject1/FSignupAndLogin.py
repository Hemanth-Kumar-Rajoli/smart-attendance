from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from signup import SignUp

si = None

class MainWindow(Screen):
    def get_text(self):
        print("hello")


class Signin1(Screen):
    def signup_class(self):
        global si,email,password
        si = SignUp(self.getid.text, self.getpassword.text, self.getcpassword.text)
        self.flag = si.create_user_with_email_password()
        si.authenticate_me()

    def get_text(self):
        print(self.getid.text)
        print(self.getpassword.text)
        print(self.getcpassword.text)
        self.signup_class()


class Signin2(Screen):
    def store_data(self):
        global si
        print(si.store_the_required_data(self.getid.text,self.getname.text,"student",self.getyear.text,self.getsemnum.text,self.getdept.text,self.getsection.text))
        si.train_my_face()
    def get_text(self):
        print(self.getid.text)
        print(self.getname.text)
        print(self.getrole.text)
        print(self.getyear.text)
        print(self.getsemnum.text)
        print(self.getdept.text)
        print(self.getsection.text)
        if(self.getid.text.strip()!=""):
            print('yes')
            print(self.store_data())

class WindowManager(ScreenManager):
    pass


kv = """
WindowManager:
    MainWindow:
    Signin1:
    Signin2:
<MainWindow>:
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.65}
        text: "Signin"  
        on_release:
            app.root.current = "Signin1" 
            root.manager.transition.direction = "left"
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.55}
        text: "login"
        on_release:
            app.root.current = "Login" 
            root.manager.transition.direction = "left"
<Signin1>:
    name: "Signin1"
    getid: Sid
    getpassword: Spassword
    getcpassword:CSpassword
    MDToolbar:
        title: 'Signin'
        pos_hint: {"top": 1}
    MDTextField:
        id: Sid
        hint_text: "Enter ID"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint_x: None
        width: 300
    MDTextField:
        id: Spassword
        hint_text: "Enter Password"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
    MDTextField:
        id: CSpassword
        hint_text: "Confirm Password"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.4, 'center_y': 0.2}
        text: "Submit"
        on_release: 
            root.get_text()
            app.root.current="Signin2" if root.flag==True else "Signin1"
            root.manager.transition.direction="left"
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.6, 'center_y': 0.2}
        text: "Back"
        on_release:
            app.root.current=""
            root.manager.transition.direction="right"
<Signin2>:
    name:"Signin2"
    getid: getid
    getname: name
    getrole:role
    getyear:year
    getsemnum:semnum
    getdept:dept
    getsection:section

    MDToolbar:
        title: "Signin"
        pos_hint: {"top": 1}
    MDTextField:
        id: getid
        hint_text: "Enter Id"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        size_hint_x: None
        width: 300
    MDTextField:
        id: name
        hint_text: "Enter Name"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint_x: None
        width: 300
    MDTextField:
        id: role
        hint_text: "Enter Role"
        text:"Student"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
    MDTextField:
        id: year
        hint_text: "Enter Year"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDTextField:
        id: semnum
        hint_text: "Enter Semester number"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
    MDTextField:
        id: dept
        hint_text: "Enter Department"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        size_hint_x: None
        width: 300
    MDTextField:
        id:section
        hint_text: "Enter Section"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        size_hint_x: None
        width: 300
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.4, 'center_y': 0.1}
        text: "Submit"
        on_release:
            root.get_text()
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.6, 'center_y': 0.1}
        text: "Back"
        on_release:
            root.get_text()
            app.root.current="Signin1"
            root.manager.transition.direction="right"
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': -0.8, 'center_y': -0.5}
        text: "oooooo"
        on_release:
            root.get_text()
"""


class MyMainApp(MDApp):
    def build(self):
        self.root = Builder.load_string(kv)


if __name__ == "__main__":
    MyMainApp().run()
