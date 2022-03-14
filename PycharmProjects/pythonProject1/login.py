from firebaseconnection import OpenFireBaseConnection
from trainImages import FaceTrainer
class login:
    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.firebase = OpenFireBaseConnection()
        self.user = None
    def authenticate_me(self):
        try:
            status = self.firebase.authenticate_user_by_email_and_password(self.email,self.password)
            if self.firebase.current_user_id()!=None:
                self.user = self.firebase.current_user_id()
                return True
            else:
                return False
        except:
            print("may be password is wrong")
    def recognize_my_face(self):
        # storing files that are comming from the firegbase
        self.user = self.firebase.current_user_id()
        if(self.user!=None):
            try:
                self.firebase.storage.child(self.user['localId']).download("","mytrainingset.txt")
                FaceTrainer().recognize_face()
                return True
            except:
                print('erorr')
        else:
            return False


if __name__ == "__main__":
    # ---------------------------------------------
    # email = "narshima@gmail.com"
    email = "dummystudent@gmail.com"
    role="student"
    reg_no="10000"
    # --------------------------------------------
    log = login(email,"password")
    print(log.authenticate_me())
    if(role=="teacher"):
        log.firebase.need_to_take_attendence('A',1)
    else:
        if(log.recognize_my_face()==True):
            print("yess rthere aerd")
            log.firebase.give_attendence(reg_no,1)

