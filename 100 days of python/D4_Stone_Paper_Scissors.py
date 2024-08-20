import random
print("What do you choose-- Type 0-paper 1-Scissors and 2-rock")
try:
   user=int(input())
   if user not in [0,1,2]:
    print("Invalid choice")
   else:
     print("user's choice",user)
except:
    print("Enter within limits")
computer=random.randint(0,2)
print("computer's choice",computer)

if user==computer:
   print("DRAW")

if user==0:
   if computer==1:
      print("Computer wins")
   elif computer==2:
      print("User Wins")
    

if user==1:
   if computer==0:
      print("user wins")
   elif computer==2:
      print("Computer Wins")
    

if user==2:
   if computer==0:
      print("Computer wins")
   elif computer==1:
      print("User Wins")
    