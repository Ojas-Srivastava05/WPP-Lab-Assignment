#find the factorial of the number
number=int(input("ENTER THE NUMBER TO FIND THE FACTORIAL"))#input of the first number
fac=1
while number>0:
    fac=fac*number
    number=number-1

print(f"THE FACTORIAL OF THE NUMBER IS {fac}")