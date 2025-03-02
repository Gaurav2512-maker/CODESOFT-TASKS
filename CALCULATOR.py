#  ARITHMETIC CALCULATOR
# instructions
# a is first operand 
# b is second operand
# o is operator 
# s refers to sum of two operand
# d refers difference of two operand 
# p refers product of two number
# div refers to divison of two number

a = input("enter first number : ")
b = input("enter second numbeer : ")
o = input("enter the operator  : ")
if(o == '+'):
    s = int(a) + int(b)
    print("sum of two  number = ",s)
elif(o == '-'):
    d = int(a) - int(b)
    print("difference of two number : ",d)
elif(o == '*'):
    p = int(a) * int(b)
    print("product of two numbwer : ",p)
elif(o == '/' and b != '0'):
    div = int(a)/int(b)
    print("divison of two number = %.2f"%div)
elif(o == '/' and b == '0'):
    print("ERROR : DIVISON BY ZERO")




    


