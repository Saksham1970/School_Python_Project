#This program tells if a number is perfect or not
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
num = IntegerGetter("Enter a number you want to check is perfect or not: ")

#process
i=1
s=0
while i<num:
    if num%i==0:
        s += i
    i+=1
#Output
if s==num:
    print(f"The number {num} is a perfect Number.")
else:
    print(f"The number {num} is not a perfect number.")