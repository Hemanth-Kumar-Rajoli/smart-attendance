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
from login import Login
si = None
log = None

class stustaff(Screen):
    pass


class SignLogin(Screen):
    def get_text(self):
        print("hello")


class Signin1(Screen):
    def signup_class(self):
        global si
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
        print(self.getrole.text)
        if self.getrole.text != "Student" and self.getrole.text != "student":
            print('-------------ggcgc---------------j')
            section = self.getsection.text.split(",")
            role = 'teacher'
        else:
            section = self.getsection.text
            role = 'student'
        print(section)
        print(si.store_the_required_data(self.getid.text, self.getname.text, role, self.getyear.text,
                                         self.getsemnum.text, self.getdept.text, section))
        si.train_my_face()

    def get_text(self):
        print(self.getid.text)
        print(self.getname.text)
        print(self.getrole.text)
        print(self.getyear.text)
        print(self.getsemnum.text)
        print(self.getdept.text)
        print(self.getsection.text)
        if self.getid.text.strip() != "":
            print('yes')
            print(self.store_data())


class Staffsignlogin(Screen):
    def get_text(self):
        print("hello")


class StaffSignin1(Screen):
    def get_text(self):
        print(self.getid.text)
        print(self.getpassword.text)
        print(self.getcpassword.text)


class StaffSignin2(Screen):
    def get_text(self):
        print(self.getid.text)
        print(self.getname.text)
        print(self.getrole.text)
        print(self.getdept.text)


class MainWindow(Screen):
    pass


class StudentLogin(Screen):
    def log_me_in(self):
        global log
        log = Login(self.getstudentemail.text,self.getstudentpassword.text)
        err = log.authenticate_me()
        # for d in err.each():
        #     print(d.key())
        # print(type(err))
        if type(err)!=dict:
           self.flags = False
        else:
            self.flags = True
        # print(issubclass(err, Exception))
    def get_text(self):
        print(self.getstudentemail.text)
        print(self.getstudentpassword.text)
        self.log_me_in()


class StaffLogin(Screen):
    def log_me_in(self):
        global log
        log = Login(self.getstaffemail.text,self.getstaffpassword.text)
        err = log.authenticate_me()
        # for d in err.each():
        #     print(d.key())
        # print(type(err))
        if type(err)!=dict:
           self.flagst = False
        else:
            self.flagst = True
        # print(issubclass(err, Exception))
    def get_text(self):
        print(self.getstaffemail.text)
        print(self.getstaffpassword.text)
        self.log_me_in()

class Student(Screen):
    def give_attendence(self):
        log.give_attendence(self.getfacultyname.text,int(self.getperiod.text))
    def get_text(self):
        print(self.getfacultyname.text)
        print(self.getperiod.text)
        self.give_attendence()

class Staff(Screen):
    def initiate_attendence(self):
        log.taken_attendence(self.getsection.text,int(self.getperiod.text))
    def get_text(self):
        print(self.getsection.text)
        print(self.getperiod.text)
        self.initiate_attendence()


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.add_widget(stustaff(name='stustaff'))
        self.add_widget(SignLogin(name="SignLogin"))
        self.add_widget(Signin1(name="Signin1"))
        self.add_widget(Signin2(name="Signin2"))
        self.add_widget(Staffsignlogin(name='Staffsignlogin'))
        self.add_widget(Signin1(name="StaffSignin1"))
        self.add_widget(Signin2(name="StaffSignin2"))
        self.add_widget(MainWindow(name='MainWindow'))
        self.add_widget(StudentLogin(name="StudentLogin"))
        self.add_widget(StaffLogin(name="StaffLogin"))
        self.add_widget(Student(name="Student"))
        self.add_widget(Staff(name="Staff"))


kv = """
WindowManager:
    stustaff:
    SignLogin:
    Signin1:
    Signin2:
    Staffsignlogin:
    StaffSignin1:
    StaffSignin2:
    MainWindow:
    StudentLogin:
    StaffLogin:
    Student:
    Staff:
<stustaff>:
    MDToolbar:
        title: 'Smart Attendance Signin'
        pos_hint: {"top": 1}
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.65}
        text: "Student"  
        on_release:
            app.root.current = "SignLogin" 
            root.manager.transition.direction = "left"
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.55}
        text: "Staff"
        on_release:
            app.root.current = "Staffsignlogin" 
            root.manager.transition.direction = "left"
<SignLogin>:
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
            app.root.current = "MainWindow" 
            root.manager.transition.direction = "left"
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.45}
        text: "Back"
        on_release:
            app.root.current = "stustaff" 
            root.manager.transition.direction = "right"
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
        text: "Register for face detection "
        on_release:
            root.get_text()
            app.root.current="MainWindow"
            root.manager.transition.direction="left"
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
<Staffsignlogin>:
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.65}
        text: "StaffSignin"  
        on_release:
            app.root.current = "StaffSignin1" 
            root.manager.transition.direction = "left"
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.55}
        text: "login"
        on_release:
            app.root.current = "MainWindow" 
            root.manager.transition.direction = "left"
<StaffSignin1>:
    name: "Signin1"
    getid: Staffid
    getpassword: Staffpassword
    getcpassword:CStaffpassword
    MDToolbar:
        title: 'StaffSignin'
        pos_hint: {"top": 1}
    MDTextField:
        id: Staffid
        hint_text: "Enter ID"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint_x: None
        width: 300
    MDTextField:
        id: Staffpassword
        hint_text: "Enter Password"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
    MDTextField:
        id: CStaffpassword
        hint_text: "Confirm Password"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        size_hint_x: None
        width: 300
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.4, 'center_y': 0.2}
        text: "Submit"
        on_release: 
            root.get_text()
            app.root.current="StaffSignin2"
            root.manager.transition.direction="left"
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.6, 'center_y': 0.2}
        text: "Back"
        on_release:
            app.root.current=""
            root.manager.transition.direction="right"
<StaffSignin2>:
    name:"Signin2"
    getid: getstaffid
    getname: staffname
    getrole:role
    getdept:dept

    MDToolbar:
        title: "Signin"
        pos_hint: {"top": 1}
    MDTextField:
        id: getstaffid
        hint_text: "Enter Id"
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        size_hint_x: None
        width: 300
    MDTextField:
        id: staffname
        hint_text: "Enter Name"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint_x: None
        width: 300
    MDTextField:
        id: role
        hint_text: "Enter Role"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
    MDTextField:
        id: dept
        hint_text: "Enter Department"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
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
            app.root.current="StaffSignin1"
            root.manager.transition.direction="right"
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': -0.8, 'center_y': -0.5}
        text: "oooooo"
        on_release:
            root.get_text()
<MainWindow>:
    MDToolbar:
        title: 'LOGIN'
        pos_hint: {"top": 1}
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.65}
        text: "Student"  
        on_release:
            app.root.current = "StudentLogin" 
            root.manager.transition.direction = "left"
    MDFillRoundFlatIconButton:
        pos_hint:{'center_x': 0.5, 'center_y': 0.55}
        text: "Staff"
        on_release:
            app.root.current = "StaffLogin" 
            root.manager.transition.direction = "left"
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        text: "Back"
        on_release:
            app.root.current="stustaff"
            root.manager.transition.direction="right"
<StudentLogin>:
    getstudentemail:Email
    getstudentpassword:password
    MDToolbar:
        title: 'StudentLogin'
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
            app.root.current="Student" if root.flags==True else 'StudentLogin'
            root.manager.transition.direction = "left"
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.6, 'center_y': 0.3}
        text: "BACK"
        on_release:
            app.root.current=""
            root.manager.transition.direction="right" 
<StaffLogin>:
    getstaffemail:Email
    getstaffpassword:password
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
            app.root.current="Staff" if root.flagst == True else "StaffLogin"
            root.manager.transition.direction = "left"
    MDFillRoundFlatIconButton:
        pos_hint: {'center_x': 0.6, 'center_y': 0.3}
        text: "BACK"
        on_release:
            app.root.current=""
            root.manager.transition.direction="right"
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
            app.root.current="MainWindow"
            root.manager.transition.direction="right" 
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
            app.root.current="MainWindow"
            root.manager.transition.direction="right" 
"""


class MyMainApp(MDApp):
    def build(self):
        self.root = Builder.load_string(kv)


if __name__ == "__main__":
    MyMainApp().run()
