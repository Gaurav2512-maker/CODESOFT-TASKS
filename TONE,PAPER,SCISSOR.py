# instrictions:
# chose only among three either stone ,paper or scissor 
# any other choice other than this is considered as invalid choice
# p1 keeps the track of computer points
# p2 keeps the track of user points
# p3 keeps the track of number of tie rounds
# r is number of rounds user want to play
# c1 is choice of user
# c2 is choice of computer

import random
r = int(input("enter number of rounds : "))
p1 = 0 
p2 = 0 
p3 = 0 
i = 1
while(i<=r):
    s = ["stone",'paper','scissor']
    c1 = input("enter users choice : ") 
    c2 = random.choice(s) 
    print("choice of computer : ",c2)
    if(c1 == 'stone' and c2 == 'paper'):
        print("computer wins")
        p1 = p1 + 1
    elif(c1 == 'paper' and c2 == 'paper'):
        print("its a tie")
        p3 = p3 + 1
    elif(c1 == 'scissor' and c2 == 'paper'):
        print("user wins")
        p2 = p2 + 1
    elif(c1 == 'stone' and c2=='stone'):
        print("its a tie")
        p3 = p3 + 1
    elif(c1 == 'paper' and c2 == 'stone'):
        print("user wins")
        p2 = p2 + 1
    elif(c1  == 'scissor' and c2 == 'stone'):
        print("computer wins")
        p1 = p1 + 1
    elif(c1 == 'stone' and c2 == 'scissor'):
        print("user wins")
        p2 = p2 + 1
    elif(c1 == 'paper' and  c2 =='scissor'):
        print("computer wins")
        p1 = p1 + 1
    elif(c1 == 'scissor' and c2 == 'scissor' ):
        print("its a tie")
        p3 = p3 + 1
    else:
        print("INVALID CHOICE ")
    i = i + 1
print("\n")
print("points of user : ",p2)
print("\npoints of computer : ",p1)
print("\nnumber of ties : ",p3)
print('\n')
if(p1 > p2):
    print("USER LOSES THE GAME")
elif(p2 > p3):
    print("USER WINS THE GAME")
else:
    print("GAME TIE")
print("THANK YOU FOR PLAYING FOR THE GAME ")

    









	
