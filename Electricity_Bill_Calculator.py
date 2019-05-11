#This program calculates the Electricity Bill of a month
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

#gets meter's reading
while True:
    pr = IntegerGetter("Electricity Meter's previous month's reading")
    cr = IntegerGetter("Electricity Meter's current month's reading")
    if pr<=cr:
        tu = cr - pr
        break
    else:
        print("Wrong Readings Entered.")

#Process

if tu<=200:
    bill = tu*4
elif tu>200 and tu<=400:
    bill = 800 + (tu-200)*6
else:
    bill = 800 + 1200 + (tu-400)*8

#Output

print(f"""
            Electricity Bill            
----------------------------------------
Name:-                   {name}
Phone Number:-           {ph}
Address:-                {add}

Current Meter Reading:-  {cr}
Previous Month Reading:- {pr}
Total Units:-            {tu}

Bill Amount Payable:-    Rs {bill}
----------------------------------------
""")