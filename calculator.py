#calculator
print("____WELL__COME____")
print("tHIS IS Basic Calculator // +  -  *  /  **  %")
def add(user_1,user_2):
    user_sum=user_1+user_2
    print(user_sum)
def sub(user_1,user_2):
    user_sub=user_1-user_2
    print(user_sub)
def mult(user_1,user_2):
    user_sub=user_1*user_2
    print(user_sub)
def div(user_1,user_2):
    user_sub=user_1/user_2
    print(user_sub)
def power(user_1,user_2):
    user_sub=user_1**user_2
    print(user_sub)
def mod(user_1,user_2):
    user_sub=user_1%user_2
    print(user_sub)
def r_up(user_1,user_2):
    user_sub=user_1//user_2
    print(user_sub)

user_1=int(input("Enter First Number"))
user_op=input("Enter Operator")
if user_op=="+":
    user_2=int(input("Enter Second Number"))
    add(user_1,user_2)
elif user_op=="-":
    user_2=int(input("Enter Second Number"))
    sub(user_1,user_2)
elif user_op=="*":
    user_2=int(input("Enter Second Number"))
    mult(user_1,user_2)
elif user_op=="/":
    user_2=int(input("Enter Second Number"))
    div(user_1,user_2)
elif user_op=="**":
    user_2=int(input("Enter Second Number"))
    power(user_1,user_2)  
elif user_op=="%":
    user_2=int(input("Enter Second Number"))
    mod(user_1,user_2)  
elif user_op=="//":
    user_2=int(input("Enter Second Number"))
    r_up(user_1,user_2) 
