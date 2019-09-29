#This program makes a triangular pattern
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
num = IntegerGetter("Enter a number till which you want the patterns: ")

#Output
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()