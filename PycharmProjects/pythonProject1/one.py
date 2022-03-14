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
class MainWindow(Screen):
    pass
class Student(Screen):
    def get_text(self):
        print(self.getfacultyname.text)
        print(self.getperiod.text)
class Staff(Screen):
    def get_text(self):
        print(self.getsection.text)
        print(self.getperiod.text)
class WindowManager(ScreenManager):
    pass

kv = """
WindowManager:
    MainWindow:
    Student:
    Staff:
<MainWindow>:
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.65}
        text: "Student"  
        on_release:
            app.root.current = "Student" 
            root.manager.transition.direction = "left"
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.55}
        text: "Staff"
        on_release:
            app.root.current = "Staff" 
            root.manager.transition.direction = "left"
<Student>:
    name: "Student"
    getfacultyname: facultyname
    getperiod: periodd
    MDToolbar:
        title: 'Get Attendance'
        pos_hint: {"top": 1}
    MDTextField:
        id: facultyname
        hint_text: "Enter Faculty Name"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
    MDTextField:
        id: periodd
        hint_text: "Enter period"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        text: "ok"
        on_release:
            root.get_text()
<Staff>:
    name:"Staff"
    getsection: section
    getperiod:  period
    MDToolbar:
        title: "Take Attendance"
        pos_hint: {"top": 1}
    MDTextField:
        id: section
        hint_text: "Enter Section"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDTextField:
        id: period
        hint_text: "Enter period"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        size_hint_x: None
        width: 300
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        text: "ok"
        on_release:
            root.get_text()
"""
class MyMainApp(MDApp):
    def build(self):
        self.root=Builder.load_string(kv)
if __name__ == "__main__":
    MyMainApp().run()