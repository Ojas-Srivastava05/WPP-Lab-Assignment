pointx = []
pointy = []
pointz = []
points = [pointx, pointy, pointz]

for i in range(10):
    x = int(input("ENTER THE X COORDINATE OF THE POINT: "))
    y = int(input("ENTER THE Y COORDINATE OF THE POINT: "))
    z = int(input("ENTER THE Z COORDINATE OF THE POINT: "))
    pointx.append(x)
    pointy.append(y)
    pointz.append(z)

shortest_distance = float('inf')
shortest_points = (None, None)

for i in range(10):
    for j in range(i + 1, 10):
        distance = ((points[0][i] - points[0][j]) ** 2 +
                     (points[1][i] - points[1][j]) ** 2 +
                     (points[2][i] - points[2][j]) ** 2) ** 0.5
        
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_points = (i, j)

if shortest_points[0] is not None:
    print(f"The shortest distance is {shortest_distance:.2f} between points {shortest_points[0]} and {shortest_points[1]}")
else:
    print("No points were provided.")



