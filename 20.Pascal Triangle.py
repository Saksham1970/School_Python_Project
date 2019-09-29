#This program makes a pascal triangle
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

def pascalrow(int):
    if int==1:
        return [1]
    row=[1,1]
    for i in range(0,len(pascalrow(int-1))):
        try:
            n=pascalrow(int-1)[i]+pascalrow(int-1)[i+1]
        except:
            pass
        else:

            n = pascalrow(int - 1)[i] + pascalrow(int - 1)[i + 1]

            row.insert(i+1,n)
    return row

#Input
num = IntegerGetter("Enter a number till which you want the patterns: ")

#Output
for i in range(1,num+1):
    leng= len(pascalrow(num))

    print(((leng-len(pascalrow(i))))*" ",end="")

    for k in pascalrow(i):
        print(k,end=" ")
    print()