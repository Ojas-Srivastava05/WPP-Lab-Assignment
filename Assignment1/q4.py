
number=int(input("ENTER A NUMBER BETWEEN 1 TO 10000"))
if number<1 or number>10000:
    print("ENTER THE NUMBER WITHIN THE SPECIFIED RANGE")
    number=int(input("ENTER A NUMBER BETWEEN 1 TO 10000"))

# print(number)
rel=[]
dig=0
while True:
    dig=number%5
    number=number/10
    rel.append(dig)


