print("________Password__Hacking_____")
def length_4(password):
    comb=0
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    print(d,c,b,a)
                    comb+=1
                    all=[d,c,b,a]
                    if all==password:
                        your=all
                        print("Your Password is: ",all)
                        
    print("password Combination:  ",comb)
    print("Your Password is:  ",your)

def length_5(pas_5):
    comb=0
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    for e in range(0,10):
                        print(e,d,c,b,a)
                        comb+=1
                        all=[e,d,c,b,a]
                        if all==pas_5:
                          your=all
                          print("Your Password is: ",your)
    print("password Combination:  ",comb)
    print("Your Password is:  ",your)

def length_6(pas_6):
    comb=0
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    for e in range(0,10):
                        for f in range(0,10):
                            print(f,e,d,c,b,a,)
                            comb+=1
                            all=[f,e,d,c,b,a]
                            if all==pas_6:
                                your=all
                                print("Your Password is: ",your)
    print("password Combination:  ",comb)
    print("Your Password is:  ",your)

def length_7(pas_7):
    comb=0
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    for e in range(0,10):
                        for f in range(0,10):
                            for g in range(0,10):
                               print(g,f,e,d,c,b,a,)
                               comb+=1
                               all=[g,f,e,d,c,b,a]
                               if all==pas_7:
                                  your=all
                                  print("Your Password is: ",your)
    print("password Combination:  ",comb)
    print("Your Password is:  ",your)

def length_8(pas_8):
    comb=0
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    for e in range(0,10):
                        for f in range(0,10):
                            for g in range(0,10):
                               for h in range(0,10):
                                   print(h,g,f,e,d,c,b,a,)
                                   comb+=1
                                   all=[h,g,f,e,d,c,b,a]
                                   if all==pas_8:
                                      your=all
                                      print("Your Password is: ",your)
    print("password Combination:  ",comb)
    print("Your Password is:  ",your)

def length_9(pas_9):
    comb=0
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    for e in range(0,10):
                        for f in range(0,10):
                            for g in range(0,10):
                               for h in range(0,10):
                                   for i in range(0,10):
                                       print(i,h,g,f,e,d,c,b,a,)
                                       comb+=1
                                       all=[i,h,g,f,e,d,c,b,a]
                                       if all==pas_9:
                                           your=all
                                           print("Your Password is: ",your)
    print("password Combination:  ",comb)
    print("Your Password is:  ",your)
def q():
    user=int(input("Enter length of PIN / 4-9"))
    option(user)

def option(user):
    if user==4:
       password=[3,2,3,4]
       length_4(password)
    elif user==5:
       pas_5=[1,2,3,4,5]
       length_5(pas_5)
    elif user==6:
       pas_6=[1,2,3,4,5,6]
       length_6(pas_6)
    elif user==7:
       pas_7=[1,2,3,4,5,6,7]
       length_7(pas_7)
    elif user==8:
       pas_8=[1,2,3,4,5,6,7,8]
       length_8(pas_8)
    elif user==9:
       pas_9=[1,2,3,4,5,6,7,8,9]
       length_9(pas_9)
    else:
      q()
q()
