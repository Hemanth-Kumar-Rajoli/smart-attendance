import pyrebase
from datetime import date, datetime
import datetime as dt
# from trainImages import  FaceTrainer
from openpyxl import Workbook,load_workbook
class OpenFireBaseConnection:
    def __init__(self):
        firebaseconfig = {
            "apiKey": "AIzaSyBJstJgG6LKPivdZiFr6BKWF3r-aaoOkEc",
            "authDomain": "learnfirebaseh.firebaseapp.com",
            "projectId": "learnfirebaseh",
            "storageBucket": "learnfirebaseh.appspot.com",
            "messagingSenderId": "520440718856",
            "appId": "1:520440718856:web:95b164d577f120f24b93bd",
            "measurementId": "G-YKXSREFYFC",
            "databaseURL": "https://learnfirebaseh-default-rtdb.firebaseio.com/"
        }
        try:
            self.firebase = pyrebase.initialize_app(firebaseconfig)
            self.auth = self.firebase.auth()
            self.database = self.firebase.database()
            self.storage = self.firebase.storage()
        except Exception as e:
            pass

    def authenticate_user_by_email_and_password(self, email, password):
        try:
            return self.auth.sign_in_with_email_and_password(email, password)
        except Exception as e:
            return e

    def createuserbyemail(self, email, password, conform_password):
        try:
            if password == conform_password:
                self.auth.create_user_with_email_and_password(email, password)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def current_user_id(self):
        # print(self.auth.current_user)
        return self.auth.current_user

    def push_data_by_schema(self, reg_no=None, name=None, role=None, year=None, sem=None, department=None,
                            section=None):
        data = {"reg_no": reg_no, "name": name, "role": role, "year": year, "sem": sem, "department": department,
                "section": section if role == "student" else None}
        try:
            ok = self.database.child("User").child(role).child(self.auth.current_user['localId']).set(data)
            print("printing statemets ok", ok, "ok means ok")
            if (ok != None):
                self.push_section_data(reg_no, role, section)
        except Exception as e:
            return e

    def push_section_data(self, reg_no, role, section):
        # print(self.database.child("Section").child(section).get())
        # print("on the section table")
        # section_data = data = self.database.child("Section").child(section).get()
        if role == "student" and section != None:
            # print("inside the table section")
            data = self.database.child("Sections").child("students").child(section).get().each()
            count = 0
            # print(len(data))
            try:
                for da in data:
                    count += 1
                    if (count >= 1):
                        break
            except:
                pass
            # print("something")
            if (count == 0):
                self.database.child("Sections").child("students").child(section).set([reg_no])
            else:
                # print('hello')
                self.database.child("Sections").child("students").child(section).update({str(len(data)): reg_no})
            # print('colsoing')
        else:
            self.database.child("Sections").child("Teachers").child(reg_no).set(section)

    def need_to_take_attendence(self, to_whome, period_no):
        print("in attendence page")
        print(self.current_user_id()['localId'])
        my_data = self.database.child("User").child("teacher").child(self.current_user_id()['localId']).get()
        print(my_data)
        my_reg_no = None
        department = None
        print("data from atten", my_data)
        try:
            for data in my_data.each():
                print(data.key(), data.val())
                if data.key() == 'reg_no':
                    my_reg_no = data.val()
                elif data.key() == "department":
                    department = data.val()
        except:
            pass
        print(my_reg_no, department)
        if (my_reg_no != None):
            today = date.today().strftime("%d %m %y")
            print(today)
            t1 = dt.datetime.strptime(datetime.today().strftime("%H %M %S"), '%H %M %S')
            t2 = dt.datetime.strptime('00 05 00', '%H %M %S')
            time_zero = dt.datetime.strptime('00 00 00', '%H %M %S')
            last_time = (t1 - time_zero + t2).time().strftime("%H %M %S")
            print(last_time, type(last_time))
            # last_time = "".join(last_time.split(":"))
            try:
                self.database.child("Attendence").child(department).child(to_whome).child(my_reg_no).child(today).child(
                    period_no).set(
                    {'deadline': last_time, 'attendedList': []})
            except:
                print("error in creating attendence")
            timedelay = 5  # in minutes

    def download_attendence(self, to_whome, period_no,date):
        print(self.current_user_id())
        my_data = self.database.child("User").child("teacher").child(self.current_user_id()['localId']).get()
        print(my_data)
        my_reg_no = None
        department = None
        wb = Workbook()
        ws = wb.active
        try:
            for data in my_data.each():
                print(data.key(), data.val())
                if data.key() == 'reg_no':
                    my_reg_no = data.val()
                elif data.key() == "department":
                    department = data.val()
        except:
            pass
        print(my_reg_no, department)
        attendence_list = self.database.child("Attendence").child(department).child(to_whome).child(my_reg_no).child(date).child(period_no).child("attendedList").get()
        try:
            for student in attendence_list.each():
                print(student.val())
        except:
            print("error in reaching inside the data")


    def give_attendence(self, teacher_no, period_no):
        print("in attendence page")
        print(self.current_user_id()['localId'])
        my_data = self.database.child("User").child("student").child(self.current_user_id()['localId']).get()
        print(my_data)
        my_reg_no = None
        department = None
        section = None
        print("data from atten", my_data)
        try:
            for data in my_data.each():
                print(data.key(), data.val())
                if data.key() == 'reg_no':
                    my_reg_no = data.val()
                elif data.key() == "department":
                    department = data.val()
                elif data.key() == "section":
                    section = data.val()
        except:
            print("erro in initizi")
        print(my_reg_no, department,section)
        if my_reg_no != None:
            today = date.today().strftime("%d %m %y")
            t1 = datetime.today().strftime("%H %M %S")
            print(t1,type(t1))
            dead_line = self.database.child("Attendence").child(department).child(section).child(teacher_no).child(today).child(period_no).child('deadline').get().val()
            print(dead_line,"------")
            print(dead_line>t1)
            if(dead_line<t1):
                return False
            length=0
            try:
                print("in side the length")
                dataset = self.database.child("Attendence").child(department).child(section).child(teacher_no).child(today).child(period_no).child('attendedList').get()

                print(dataset)
                for d in dataset:
                    if(d.val()==my_reg_no):
                        return False

                    length+=1
            except:
                print("error in getting inside data")
            try:
                self.database.child("Attendence").child(department).child(section).child(teacher_no).child(today).child(period_no).child('attendedList').update({str(length):my_reg_no})
            except:
                print("error in creating attendence")


if __name__ == '__main__':
    firebase = OpenFireBaseConnection()
    '''# print(firebase.createuserbyemail("ajith@gmail.com","password","password"))
    print(firebase.authenticate_user_by_email_and_password("hello@gmail.com", "password"))
    # firebase.push_data_by_schema('505', 'ajith', 'student',3,2, 'CSE', 'A')
    # print(firebase.printdebug())
    # firebase.need_to_take_attendence('A', 1)
    firebase.give_attendence('500',1)'''
    firebase.authenticate_user_by_email_and_password("dummyteacher","password")
    firebase.download_attendence('A',1,"12 03 22")
