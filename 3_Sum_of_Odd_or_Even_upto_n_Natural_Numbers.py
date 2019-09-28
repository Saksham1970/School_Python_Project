#This program calculates sum upto n positive numbers
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

n = IntegerGetter("Please Enter the 'n'th positive number you want sum upto")

#Process
odd_sum = 0
even_sum = 0
for num in range(1,n+1):
    if num%2==1:
        odd_sum+=num
    else:
        even_sum+=num

#Output
print(f'''
The sum of odd numbers upto n positive numbers is {odd_sum}

The sum of even numbers upto n positive numbers is {even_sum}
''')