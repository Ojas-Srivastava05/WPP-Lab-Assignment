def isFibo(n,t):
    list=[]
    test=t
    num=n
    first=0
    second=1
    sum=0
    while True:
        sum=first+second
        second=sum
        first=second
        flag=0
        if num==0:
         flag=1
         break
            
        if num==sum:
            flag=1
            break
            
        elif num!=sum:
            flag=0
            if num<sum:
                break
        
        if len(list)==test:
                break

    if flag==1:
        list.append("IsFibo")
    elif flag==0:
        list.append("IsNotFibo")
        
    return list
        
        
def main():
    t=int(input("Enter the number of test cases"))
    for i in range(1,t+1):
        n=int(input("Enter the number you want to check is Fibo or not"))
    
    print(isFibo(n,t))

if __name__=='__main__':
    main()
    
    