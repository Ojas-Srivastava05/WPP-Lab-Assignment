import numpy as np

N=int(input("Enter the value of N try to keep it over or equal to 10 "))
points=[]

print(f"Enter {N} points, each with 2 coordinates (x y): ")
for i in range(N):
    x,y=map(int,input(f"Point {i+1}: ").split())
    points.append([x,y])
    
points_array=np.array(points)
print(f"Points array:\n{points_array}")

theta=[0]*points_array.shape[0]
mag=[0]*points_array.shape[0]

for i in range(points_array.shape[0]):
    theta[i]=points_array[i][1]/points_array[i][0]
    mag[i]=(points_array[i][1]**2+points_array[i][0]**2)**0.5
    
angle_radians=np.arctan2(points_array[:,1],points_array[:,0])
angle_degree=np.degrees(angle_radians)
    
    
for i in range(points_array.shape[0]):
    points_array[i][0]=mag[i]
    points_array[i][1]=angle_degree[i]
    
print(f"Polar array:\n{points_array}")
    
    