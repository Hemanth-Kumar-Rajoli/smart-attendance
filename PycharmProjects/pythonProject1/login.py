from firebaseconnection import OpenFireBaseConnection
from trainImages import FaceTrainer


class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.firebase = OpenFireBaseConnection()
        self.user = None

    def authenticate_me(self):
        try:
            status = self.firebase.authenticate_user_by_email_and_password(self.email, self.password)
            print("!!!!!!!!!!!!!!stutus : ",status,"!!!!!!!!!!!!!!!!!!")

            if self.firebase.current_user_id() != None:
                self.user = self.firebase.current_user_id()
                return status
            else:
                return status
            return status
        except:
            print("may be password is wrong")

    def recognize_my_face(self):
        # storing files that are comming from the firegbase
        self.user = self.firebase.current_user_id()
        if (self.user != None):
            try:
                self.firebase.storage.child(self.user['localId']).download("", "mytrainingset.txt")
                FaceTrainer().recognize_face()
                return True
            except:
                print('erorr')
        else:
            return False
    def taken_attendence(self,to_whome,period):
        period = int(period)
        self.firebase.need_to_take_attendence(to_whome, period)
    def give_attendence(self,to_whome,period):
        if (self.recognize_my_face() == True):
            print("yess rthere aerd")
            self.firebase.give_attendence(to_whome, period)


if __name__ == "__main__":
    # ---------------------------------------------
    # email = "narshima@gmail.com"
    email = "dummystudent@gmail.com"
    role = "student"
    reg_no = "10000"
    # --------------------------------------------
    log = Login(email, "password")
    print(log.authenticate_me())
    if (role == "teacher"):
        log.firebase.need_to_take_attendence('A', 1)
    else:
        if (log.recognize_my_face() == True):
            print("yess rthere aerd")
            log.firebase.give_attendence(reg_no, 1)
