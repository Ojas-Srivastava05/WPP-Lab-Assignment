#find the reverse of any number
number=int(input("ENTER THE NUMBER YOU WANT TO REVERSE"))
reverse=0
while number!=0 :
    rem=number%10
    reverse=reverse*10+rem
    number=number//10

print(f"THE REVERSED NUMBER IS {reverse}")