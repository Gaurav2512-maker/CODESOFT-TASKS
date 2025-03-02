#PASSWORD GENERATOR 
# INSTRUCTION
# l refers to length of password between 5 to 10
# s refers to the strength of password 
# strength 1 contain numbers and lowercase 
# strength 2 password contain numbers lowercase and uppercase
# strength 3 password conatin lowercase and uppercase and atleast one special character


import random
a = "qwertyuiopasdfghjklzxcvbnm"
b = "QWERTYUIOPASDFGHJKLZXCVBNM"
c = "1234567890"
d = "~!@#$%^&*/*-+?_';"
l = int(input("enter the length of password (5 - 10): "))
if(l<5 or l>10):
    print("PLEASE PROVIDE APPROPRIATE LENGTH OF PASSWORD")
elif(l>=5 or l<=10):
    s = int(input("enter strength of password (1-3) : "))
    if(s<0 or s>3):
        print("PLEASE PROVIDE SPECIFIED STRENGTH OF PASSWORD : ")
    elif(s>=1 or s<=3):
        if(l==5 and s==1):
            
            a1,a2=random.choice(c),random.choice(c)
            a3,a4=random.choice(a),random.choice(a)
            a5=random.choice(c)
            p = a1+a2+a3+a4+a5
            print("\nthe generated password = ",p)
        elif(l==5 and s==2):
            
            a1,a2=random.choice(b),random.choice(c)
            a3,a4,a5=random.choice(a),random.choice(a),random.choice(c)
            p=a1+a2+a3+a4+a5
            print("\nthe generated password is = ",p)
        elif(l==5 and s==3):
            
            a1,a2,a3=random.choice(b),random.choice(c),random.choice(d)
            a4,a5=random.choice(a),random.choice(c)
            p = a1+a2+a3+a4+a5
            print("\nthe generated passwoed = ",p)
        elif(l==6 and s==1):
            
            a1,a2,a3 = random.choice(c),random.choice(c),random.choice(c)
            a4,a5,a6= random.choice(a),random.choice(a),random.choice(a)
            p = a1+a2+a3+a4+a5+a6
            print("the generated password = ",p)
        elif(l==6 and s==2):
            a1,a2,a3=random.choice(b),random.choice(a),random.choice(c)
            a4,a5,a6=random.choice(b),random.choice(a),random.choice(c)
            p=a1+a2+a3+a4+a5+a6
            print("the generated password = ",p)
        elif(l==6 and s==3):
            a1,a2,a3 = random.choice(b),random.choice(a),random.choice(c)
            a4,a5,a6 = random.choice(d),random.choice(b),random.choice(c)
            p = a1+a2+a3+a4+a5+a6
            print("the generate password = ",p)
        elif(l==7 and s==1):
            a1,a2,a3 = random.choice(c),random.choice(c),random.choice(a)
            a4,a5,a6,a7 = random.choice(a),random.choice(c),random.choice(c),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7
            print("the generated password = ",p)
        elif(l==7 and s==2):
            a1,a2,a3,a4 = random.choice(b),random.choice(a),random.choice(c),random.choice(a)
            a5,a6,a7 = random.choice(b),random.choice(c),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7
            print("the generated password = ",p)
        elif(l==7 and s==3):
            a1,a2,a3,a4 = random.choice(b),random.choice(a),random.choice(c),random.choice(d)
            a5,a6,a7 = random.choice(b),random.choice(a),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7
            print("the generated password = ",p)
        elif(l==8 and s==1):
            a1,a2,a3,a4 = random.choice(c),random.choice(c),random.choice(c),random.choice(a)
            a5,a6,a7,a8 = random.choice(a),random.choice(a),random.choice(a),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7+a8
            print("the generated password = ",p)
        elif(l==8 and s==2):
            a1,a2,a3,a4= random.choice(b),random.choice(b),random.choice(a),random.choice(a)
            a5,a6,a7,a8 = random.choice(c),random.choice(c),random.choice(a),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7+a8
            print("the generated password = ",p)
        elif(l==8 and s==3):
            a1,a2,a3,a4 = random.choice(b),random.choice(b),random.choice(a),random.choice(d)
            a5,a6,a7,a8 = random.choice(c),random.choice(c),random.choice(a),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7+a8
            print("the generated passwor = ",p)
        elif(l==9 and s== 1):
            a1,a2,a3,a4,a5 = random.choice(c),random.choice(c),random.choice(c),random.choice(a),random.choice(a)
            a6,a7,a8,a9 = random.choice(a),random.choice(a),random.choice(c),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7+a8+a9
            print("the generated password = ",p)
        elif(l==9 and s==2):
            a1,a2,a3,a4,a5 = random.choice(b),random.choice(b),random.choice(a),random.choice(a),random.choice(a)
            a6,a7,a8,a9 = random.choice(c),random.choice(c),random.choice(c),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7+a8+a9
            print("the generated password = ",p)
        elif(l==9 and s==3):
            a1,a2,a3,a4,a5 = random.choice(b),random.choice(b),random.choice(a),random.choice(a),random.choice(d)
            a6,a7,a8,a9 = random.choice(c),random.choice(c),random.choice(c),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7+a8+a9
            print("the generated password = ",p)
        elif(l==10 and s==1):
            a1,a2,a3,a4,a5 = random.choice(c),random.choice(c),random.choice(c),random.choice(c),random.choice(a)
            a6,a7,a8,a9,a10 = random.choice(a),random.choice(a),random.choice(a),random.choice(a),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10
            print("the generated password = ",p)
        elif(l==10 and s==2):
            a1,a2,a3,a4,a5= random.choice(b),random.choice(b),random.choice(a),random.choice(a),random.choice(a)
            a6,a7,a8,a9,a10 = random.choice(c),random.choice(c),random.choice(c),random.choice(c),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10
            print("the generated password = ",p)
        elif(l==10 and s==3):
            a1,a2,a3,a4,a5 = random.choice(b),random.choice(b),random.choice(a),random.choice(a),random.choice(a)
            a6,a7,a8,a9,a10 = random.choice(d),random.choice(c),random.choice(c),random.choice(c),random.choice(c)
            p = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10
            print("the generated password = ",p)




        


        