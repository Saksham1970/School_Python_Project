#This program tells if a number is pallindrome or not
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
num = IntegerGetter("Enter a number you want to check is pallindrome or not: ")

#process
y = num
z=0
while y>0:
    z =z*10+ (y%10)
    y //=10
#Output
if z==num:
    print(f"The number {num} is a Pallindrome number.")
else:
    print(f"The number {num} is not a Pallindrome number.")