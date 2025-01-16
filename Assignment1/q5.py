names=[]
for i in range(1 , 11):
    name=input(f"ENTER {i} NAME OUT OF 10 NAMES")
    name=list(name)
    if len(name)>15:
        print("Please re-enter the name")
        while True:
            name=input(f"ENTER THE NAME WITHIN THE LIMIT THIS TIME ")
            name=list(name)
            if len(name)>15:
                continue
            elif len(name)<15:
                break
    name=name[::-1]
    names.append(name)

for i in range(0,11):
    print(names[i])
