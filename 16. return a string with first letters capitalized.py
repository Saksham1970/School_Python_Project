#This program returns a string with first letter capitalized
#This program is made by Saksham Gupta

#input
string=input("Enter a string: ")

#process
final=""
x=string.split()
for i in x:
    final+=i.capitalize() +" "

#Output
print(final)