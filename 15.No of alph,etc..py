#This program counts alphabet,digits,uppercase,lower case,spaces,other
#This program is made by Saksham Gupta

#input
string=input("Enter a string: ")

#process
a=d=u=l=s=o=0

for i in string:
    if i.isalpha():
        a+=1
        if i.upper():
            u+=1
        else:
            l+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        s+=1
    else:
        o+=1
print(f'''
No of char which were alphabet were {a}
No of char which were digit were {d}
No of char which were upper case alphabet were {u}
No of char which were lower case alphabet were {l}
No of char which were space were {s}
No of char which were special char were {o}''')


