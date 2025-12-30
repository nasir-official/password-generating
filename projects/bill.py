billunit = 5
name=input("Enter your Name")
mounth=input("Enter a Bill Mounth")
amount=float(input("Enter your total Units consume"))
total=amount*billunit
late=input("Your late yes/no ??")
if late=="yes":
    if amount>=0 and amount<=100:
        print("you are late fee is Rs:500")
        total=total+500
        print(f"Total Amount is {total}")
    if amount>100 and amount<=200:
        print("you are late fee is Rs:1000")
        total=total+1000
        print(f"Total amount is {total}")
    if amount>200 and amount<=300:
        print("you are late fee is Rs:2000")
        total=total+2000
        print(f"Total amount is {total}")
    if amount>300 and amount<=400:
        print("you are late fee is Rs:3000")
        total=total+3000
        print(f"Total amount is {total}")
    if amount>400 and amount<=500:
        print("you are late fee is Rs:5000")
        total=total+5000
        print(f"Total amount is {total}")
    if amount<501:
        print(f"your bill is too high warning")
elif late=="no":
    totalamount=amount*billunit
    print(f"Your Total amount is Rs:{totalamount}")
else:
    print("sntaxt error")
print(f"Name: {name}")
print(f"Mounth : {mounth}")
print(f"Total Units {amount}")
print(f" Good Luck for pay! ")