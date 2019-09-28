#This program calculates the Simple Interest
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
amt = IntegerGetter("Amount: ")
no = IntegerGetter('No. of Years: ')
rate = IntegerGetter('Rate of Interest: ')

#Process
int = (amt*no*rate)/100
#Output

print(f"""
           Simple Interest                                          
------------------------------------------
Amount:-                     {amt}
Rate of Interest:-           {rate}
No of years:-                {no}

Interest:-                   {int}
------------------------------------------
""")