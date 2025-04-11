"""After accidentally leaving an ice chest of fish and shrimp in your car for a week while you were
 on vacation, you’re now in the market for a new vehicle. Your insurance didn’t cover the loss, so 
 you want to make sure you get a good deal on your new car.Given a Series of car asking_prices and
   another Series of car fair_prices, determine which cars for sale are a good deal. In other words,
 identify cars whose asking price is less than their fair price.The result should be a list of
   integer indices corresponding to the good deals in asking_prices."""

import pandas as pd

data1=[]
n=int(input("enter no. of cars:"))
for car in range(n):
    item=int(input("enter asking price:"))
    data1.append(item)

data2=[]
for car in range(n):
    item=int(input("enter fair price:"))
    data2.append(item)
asking_price=pd.Series(data1)
fair_price=pd.Series(data2)
result=[]
for i  in range(n):
    if(asking_price[i]<fair_price[i]):
        result.append(i)
print("following are the indices corresponding to good deals")
print(result)