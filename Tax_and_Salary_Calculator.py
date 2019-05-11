#This program calculates the Tax and Salary of a month
#This program is made by Saksham Gupta

#This function makes sure input is an integer
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

#gets user details
name = input("\nEnter Your Name:")
ph = IntegerGetter("Phone Number")
add = input("\nEnter Your Address:")

#gets income of user per month
inc = IntegerGetter("Income p/m")

#Process
ginc = inc*12
if ginc<=250000:
    tax = 0
elif ginc>250000 and ginc<=500000:
    tax = (ginc-250000)*0.05
elif ginc>500000 and ginc<=1000000:
    tax = 12500 + (ginc-500000)*0.2
else:
    tax = 112500 + (ginc-1000000)*0.3
Salary = ginc-tax

#Output

print(f"""
            Tax And Salary Cut                                          
------------------------------------------
Name:-                   {name}
Phone Number:-           {ph}
Address:-                {add}

Income p/m:-             Rs {inc}
Income p/a:-             Rs {ginc}

Total Tax:-              Rs {tax}
Salary p/a:-             Rs {Salary}
Salary p/m:-             Rs {round(Salary/12, 2)}
------------------------------------------
""")