print("WELCOME TO FIR")
print("\n")
x=input("Enter your Name:")
a=0
print("\n")
print("Are you vaccinated?")
n=input("write YES or NO:")
if(n=='YES'):
  a=a+1
else:
  a=a+0
print("\n Do you have fever?")
n=input("write YES or NO:")
if(n=='YES'):
  a=a+1
else:
  a=a+0
print("\n Do you have cold or dry cough?")
n=input("write YES or NO:")
if(n=='YES'):
  a=a+1
else:
  a=a+0
print("\n Are you experiencing a loss of taste or smell?")
n=input("write YES or NO:")
if(n=='YES'):
  a=a+1
else:
  a=a+0
print("\n Do you have any issues in breathing?")
n=input("write YES or NO:")
if(n=='YES'):
  a=a+1
else:
  a=a+0
print("\nDo you have chest pain?")
n=input("write YES or NO:")
if(n=='YES'):
  a=a+1
else:
  a=a+0
print("\n")
print("HEY",x)
print("Your total score is:", a)
if(a==1):
   print("No need to worry,you are safe")
elif(a==2):
   print("Nothing to worry about,you are alright")
elif(a==3):
   print("You can take some normal medications and take rest at home")
elif(a==4):
   print("You have some symptoms,try to keep yourself quarantine for 2-3 days with some regular medications")
elif(a==5):
   print("You are at high risk,take a test as soon as possible")
elif(a==6):
   print("You need to get tested immediately")
else:
   print("Be happy, you are totally safe")
print("\n")
print("THANK YOU FOR USING FIR")