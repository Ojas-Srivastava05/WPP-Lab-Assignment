pointx=[]#list to store the x coordinates of the points
pointy=[]#list to store the y coordinates of the points
pointz=[]#list to store the z coordinates of the points
points=[pointx,pointy,pointz]#making a list to store the points
for i in range(10):
    x=int(input("ENTER THE X COORDINATE OF THE POINT"))
    y=int(input("ENTER THE Y COORDINATE OF THE POINT"))
    z=int(input("ENTER THE Z COORDINATE OF THE POINT"))
    pointx.append(x)
    pointy.append(y)
    pointz.append(z)
    points=[pointx,pointy,pointz]
    print(points)
   
    

