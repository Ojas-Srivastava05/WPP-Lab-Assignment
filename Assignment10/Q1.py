#Queen's problem
import random
def Queen(x,y):
    count=0
    if count==0:
        x=0
        y=random.randint(0,7)
        count+=1
    print(x)
    print(y)
    invalid=[[x+1,y+1],[x+1,y],[x+1,y-1],[x-1,y+1],[x-1,y],[x-1,y+1]]
    for i in range(0,x+1):
        for j in range(0,y+1):
            
            
            
            
            
    
if __name__ == "__main__":
    Queen(0,0)

