#This program tells if a number is armstrong or not
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
num = IntegerGetter("Enter a number you want to check is armstrong or not: ")

#process
y = num
z=0
while y>0:
    z += (y%10)**3
    y //=10
#Output
if z==num:
    print(f"The number {num} is an Armstrong Number.")
else:
    print(f"The number {num} is not an Armstrong number.")