print("Welcome to Tip calculator")

bill=int(input("What is your total bill?\n"))
num=int(input("How many people to split the bill at?\n"))
tip=int(input("What percentage of tip you want to give? like-5%, 10% \n"))

final=bill+((bill*tip)/100)
total_bill=final/num

print("Everyone has to pay Rs "+ str(round(total_bill,2)))