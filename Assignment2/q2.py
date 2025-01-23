menu={}#as a dictionary initialize karega
while True:
    key=input("Enter the product name enter q to exit")
    if key=='q' or key=='Q' :
        break
    value=input("Enter the product price")
    menu[key]=value

print(menu)

while True: 
    
    for key,value in menu.items():
        check=input("enter the item you want to find in the dictionary enter q to quit")
        if key==check:
            print(key,value)
        if check=='q' or check== 'Q':
            break
        else:
            print("ITEM NOT FOUND")
        

