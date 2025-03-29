#Q TAKE A 2D ARRAY WHICH ACTUALLY REPRESENTS 2D POINTS , FIRST PLOT INITIAL POINTS THEN USE X=X+1 AND Y=Y+2 AND THEN AGAIN PLOT IT HARD CODE NHI KARNA HAI AUR SHAPE KA USE KARKE NO. OF ROWS AUR COLUMN KI VALUE LAANI HAI 
import matplotlib.pyplot as plt
import numpy as np

points=[[1,1],[2,2],[3,3]]
points=np.array(points)
x=points[:,0]
y=points[:,1]
plt.scatter(x,y)
plt.show()
x=x+1
y=y+2
