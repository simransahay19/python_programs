import random
l1=list()
n1=list()
s1=list()
sim1=list()

print("WELCOME TO PASSWORD GENERATOR")
print("How many letters you want in your password")
letter=int(input())
print("How many special cahracter you want in your password")
special=int(input())
print("How many numbers you want in your password")
number=int(input())

letter_array=[ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' ,'z']

number_array=['1','0','2','3','4','5','6','7','8','9']

special_array=['!','~','@','#','$','%','^','&','*','(',')','*']

for i in range(letter):

   l=random.randint(0,len(letter_array))
   l1.append(letter_array[l])
c=''.join(map(str,l1))

for i in range(number): 
  n=random.randint(0,len(number_array))
  n1.append(number_array[number])
d=''.join(map(str,n1))


for i in range(special): 
  s=random.randint(0,len(special_array))
  s1.append(special_array[s])
e=''.join(map(str,s1))

print("Your password is",c+d+e)
