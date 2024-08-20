c="TRUE LOVE"
l=list(c)
name=(input("Enter your full name\n")).lower()
lname=(input("Enter your lover's name\n")).lower()
main1="true"
main2="love"
sum=0
sum2=0
final=(name.replace(" ",""))+(lname.replace(" ",""))

for i in range(0,len(main1)):
    if main1[i] in final:
        sum=sum+final.count(main1[i])

for i in range(0,len(main2)):
    if main2[i] in final:
        sum2=sum2+final.count(main2[i])

print("Your love percentage is",str(sum)+str(sum2),"%")

