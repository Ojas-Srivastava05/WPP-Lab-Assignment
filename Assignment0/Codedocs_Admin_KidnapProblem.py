t=int(input("ENTER THE NUMBER OF TEST CASES"))
string=input("ENTER THE VALUE OF N X and S SEPARATED BY SPACES")#I am taking the input of N X AND S as a string
#number = [int(i) for i in string.split()]
string=string.replace(" ","")#I refered online to look about this function 
string=int(string)
s=string%10
string=string//10
x=string%10
string=string//10
n=string
print(f"THE VALUE OF N X AND S ARE {n} {x} {s}")
flag1=0
flag2=0
flag3=0
while s>0 :
    
    swap=input("ENTER THE BOXES TO SWAP THE CONTENTS SEPARATED BY SPACES")
    swap=swap.replace(" ","")
    swap=int(swap)
    box2=swap%10
    swap=swap//10
    box1=swap 
    if box1==x : #if the box with coin was selected it will trigger the flag of the other box after the swap
       flag1=0
       flag2=1

    if box2==x : #if the box with coin was selected it will trigger the flag of the other box after the swap
       flag2=0
       flag1=1
       
    elif flag1==0 and flag2==0: #case if the box in which the coin initially was is never selected
        flag3=1

      
    s=s-1
if flag1==1:
    print(f"THE FINAL COIN WAS IN BOX {box1}")
if flag2==1:
    print(f"THE FINAL COIN WAS IN BOX {box2}")
if flag3==1:
    print(f"THE FINAL COIN WAS IN BOX {x}")


