#solution 1 is to import the random module of python
import random
value=0
digcounter=0
while True:
    i=random.randint(0,1)
    value=value*10+i
    digcounter+=1
    if digcounter>100:
        break
    
value=list[value]

print(value)
countzero=0
countone=0
longest=0
flag=0
dummy=value
digit=0
while True:
    digit=value%10
    value=value/10
    digcounter-=1
    if digit==1:
        countone+=1

    elif digit==0:
        countzero+=1
    
    if digcounter<0:
        break

if flag==0 :
    print(f"THE LONGEST RUN OF ZEROES IN {dummy} IS {longest}")

if flag==1 :
    print(f"THE LONGEST RUN OF ONES IN {dummy} IS {longest}")
        

