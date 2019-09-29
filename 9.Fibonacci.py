#This program finds fibonacci series upto n numbers
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

#This function finds fibonacci series
def fibonacci(int):
    if int==1:
        return 0
    if int==2:
        return 1
    else:
        return fibonacci(int-1)+fibonacci(int-2)

#input
n=IntegerGetter('Enter a number of members you want of the fibonacci series: ')

#process, output
for i in range(1,n+1):
    print(fibonacci(i))