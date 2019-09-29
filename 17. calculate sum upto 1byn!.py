#This program sum of the series 1 + x/1! + x^2/2! ... + x^n/n!
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
x= IntegerGetter("Enter  value of x: ")
lim = IntegerGetter("Enter a limit till which you want the prime numbers to be: ")

#process
s=0
for num in range(0,lim+1):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    s+=(x**num)/fact
#Output
print(s)