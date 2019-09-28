#This program calculates number raised to a power
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
x = IntegerGetter("Enter a number: ")
n = IntegerGetter("Enter power: ")

#Output
print(f"The number raised to the power is {x**n}.")