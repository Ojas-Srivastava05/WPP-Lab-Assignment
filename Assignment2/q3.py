T=int(input("Enter the number of test cases"))
i=0
l1=[]
while True:
    counter=0
    number=int(input("Enter the number "))
    ori=number
    while number!=0:
        rem=number%10
        if ori%rem==0:
            counter+=1
        number=number//10
    l1.append(counter)
    if i>=T-1:
        break
    i+=1
    

print(*l1,sep="\n")
           
    
    
    

