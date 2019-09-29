#This program calculates grade by percentage
#This program is made by Saksham Gupta

#This function makes sure input is a positive integer
def IntegerGetter(str):
    while True:
        try:
            num = int(input(str))
        except ValueError:
            print("That's not an Integer. Please Enter Details again.")
        else:
            if num>=0 and num <= 100:
                return num
            else:
                print("Please enter a correct number.")
#Input
per = IntegerGetter("Please enter your percentage: ")
if per >85:
    print('A')
elif per>70 and per <=85:
    print('B')
elif per>60 and per <=70:
    print('C')
elif per>45 and per <=60:
    print('D')
else:
    print('E')