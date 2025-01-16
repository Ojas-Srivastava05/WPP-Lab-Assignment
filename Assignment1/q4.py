l0=[]
l1=[]
l2=[]
l3=[]
l4=[]
for i in range(1,10001):
    rem=i%5
    if rem==0:
        l0.append(i)
    if rem==1:
        l1.append(i)
    if rem==2:
        l2.append(i)
    if rem==3:
        l3.append(i)
    if rem==4:
        l4.append(i)
ltotal=l0+l1+l2+l3+l4
ltotal.sort()
compare=[]
for i in range(1,10001):
    compare.append(i)
if ltotal==compare:
    print("EQUIVALENCE RELATION IS VALID")
else:
    print("EQUIVALENCE RELATION IS NOT VALID")


    


