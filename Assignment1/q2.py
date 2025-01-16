import random
digcount=0
value=[]
while digcount<100:
    value.append(random.randint(0,1))
    digcount+=1


countzero=0
countone=0
longest=0
flag=0
for i in range (100):
    if value[i]==0:
        countzero+=1
        countone=0
        if countzero>longest:
            longest=countzero
            flag=0

    if value[i]==1:
        countone+=1
        countzero=0
        if countone>=longest:
            longest=countone
            flag=1

print(f"THE GENERATED BINARY NUMBER IS {value}",sep="")

if flag==0:
    print(f"THE LONGEST CONSECUTIVE OCCURENCE OF ZERO IS {longest}")
if flag==1:
    print(f"THE LONGEST CONSECUTIVE OCCURENCE OF ONE IS {longest}")