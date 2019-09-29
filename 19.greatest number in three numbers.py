#This program arranges the numbers in descending order
#This program is made by Saksham Gupta

#This function makes sure input is a positive integer
def IntegerGetter(str):
    while True:
        try:
            num = int(input(str))
        except ValueError:
            print("That's not an Integer. Please Enter Details again.")
        else:
            if num>=0:
                return num
            else:
                print("Please enter a correct number.")
#Input
x = IntegerGetter("Enter first number : ")
y = IntegerGetter("Enter second number : ")
z = IntegerGetter("Enter third number : ")

#process and output
if x>y and x>z:
    if y>z:
        print(f"The numbers in descending order are {x},{y},{z}")
    else:
        print(f"The numbers in descending order are {x},{z},{y}")
elif y>z:
    if z>x:
        print(f"The numbers in descending order are {y},{z},{x}")
    else:
        print(f"The numbers in descending order are {y},{x},{z}")
else:
    if y>x:
        print(f"The numbers in descending order are {z},{y},{x}")
    else:
        print(f"The numbers in descending order are {z},{x},{y}")