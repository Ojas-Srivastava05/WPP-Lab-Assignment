#Part 1(a)
numbers=[]
for i in range (0,50):
    numbers.append(i)

for i in numbers:
    print(i)

print("--------------------------------------")
#Part 1(b)
squares=[]
for i in range (1,51):
    squares.append(i**2)

for i in  squares:
    print(i)

#Part 1(c)
alpha = []
for i in range(1, 27):
    letter = chr(96 + i)  # Convert the letter index to its ASCII equivalent
    alpha.append(letter * i)  

for line in alpha:  
    print(line)

