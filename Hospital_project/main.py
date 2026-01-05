##==================  HOSPITAL MANAGIMENT SYSTEM   ==============

class User:
    def __init__(self,name,age,token_no):
        self.name=name
        self.age=age
        self.__token_no=token_no
        self.role()
    def role(self):
        print("What is your Role..")
        role=int(input("1=Patient    2= Doctor  "))
        if role==1:
           Patients()
        elif role==2:
           Doctor()
        else:
           print("Some error")

class Patients:
    def __init__(self):
        super().__init__(name,age,self.__token_no)



class Doctor:
    def __init__(self):
        id_info=[1234,1122,2233,4321,4567,7890]
        while True:
            id=int(input("Enter Valid ID numbre.  "))
            if id in id_info:
              Doctor.time()
            else:
               print("Invalid ID number ")
               add=int(input("Add new ID number..? yes=1  /   no=2   /  Back=9"))
               if add==1:
                  new_id=int(input("Enter new ID numbre.."))
                  new_id.append(id_info)
               elif add==2:
                  continue
               elif add==9:
                  User.role()
                  True
               else:
                  print("Proram Exit")
    def time():
        print("====timing of Hospital====")



class Apponiment:
    def __init__(self):
        pass


class Bill_system:
    def __init__(self):
        pass


class Hospital:
    def __init__(self):
        pass


print("======  HOSPITAL MANAGEMENT SYSTEM  =========")
name=input("Enter Your Full Name..  ")
age=int(input("Enter your Age..  "))
token_no=[x for x in range(1,100)]
user1=User(name,age,token_no)
user2=User(name,age,token_no)
doct=Doctor()