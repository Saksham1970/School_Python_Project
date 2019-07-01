#This program calculates product upto n positive numbers
#This program is made by Saksham Gupta

#This function makes sure input is a positive integer
def IntegerGetter(str):
    while True:
        try:
            num = int(input(f"\nEnter your {str}: "))
        except ValueError:
            print("That's not an Integer. Please Enter Details again.")
        else:
            if num>=0:
                return num
            else:
                print("Please enter a correct number.")
#Input

n = IntegerGetter("Please Enter the 'n'th positive number you want product upto")

#Process
product = 1
for num in range(1,n+1):
    product *= num

#Output
print(f'The product upto n positive numbers is {product}')