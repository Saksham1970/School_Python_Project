#This program tells all the prime numbers upto a limit
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
lim = IntegerGetter("Enter a limit till which you want the prime numbers to be: ")

#process
for num in range(2,lim+1):
    i=2
    while i<num:
        if num%i==0:
            break
        i+=1
    else:
        print(f"{num} is a prime number")