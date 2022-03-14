from firebaseconnection import OpenFireBaseConnection
from trainImages import FaceTrainer


class SignUp:
    def __init__(self, email, password, password_conform, ):
        self.email = email
        self.password = password
        self.password_conform = password_conform
        self.firebase = OpenFireBaseConnection()

    def create_user_with_email_password(self):
        try:
            self.firebase.createuserbyemail(self.email, self.password, self.password_conform)
        except:
            return False

    def store_the_required_data(self, reg_no=None, name=None, role=None, year=None, sem=None, department=None,
                                section=None):
        try:
            self.firebase.push_data_by_schema(reg_no, name, role, year, sem, department, section)
            # self.firebase.
            return True
        except:
            print('eroor')
            return False

    def train_my_face(self, ref_loc):
        try:
            FaceTrainer().collect_images().train_the_set().train_the_set(ref_loc)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    # -------------------------------------------------------------------------
    email = "dummydummy@gmail.com"
    reg_no = "10000"
    name = "me"
    role = "teacher"
    # --------------------------------------------------------------------------
    if role == "teacher":
        # teacher data
        si = SignUp(email, "password", "password")
        si.create_user_with_email_password()
        print("\nby authentiaceiton ---------\n",
              si.firebase.authenticate_user_by_email_and_password(email, "password"), "\n")
        si.store_the_required_data(reg_no, name, "teacher", None, None, "CSE", ['A', 'B'])
        print("by normal print", si.firebase.current_user_id()['localId'])
        si.train_my_face(si.firebase.current_user_id()['localId'])
    # student
    else:
        si = SignUp(email, "password", "password")
        si.create_user_with_email_password()
        print("\nby authentiaceiton ---------\n", si.firebase.authenticate_user_by_email_and_password(email, "password"),"\n")
        si.store_the_required_data(reg_no, name, "student", 3, 2, "CSE", 'A')
        print("by normal print", si.firebase.current_user_id()['localId'])
        si.train_my_face(si.firebase.current_user_id()['localId'])
