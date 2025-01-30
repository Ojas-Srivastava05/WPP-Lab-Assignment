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
        if num==sum:
            list.append("IsFibo")
            if len.list==test:
                break
        else:
            list.append("IsNotFibo")
            if len.list==test:
                break
    return list
        
        
def main():
    t=int(input("Enter the number of test cases"))
    for i in range(1,t+1):
        n=int(input("Enter the number you want to check is Fibo or not"))
        print(isFibo(n,t))

if __name__=='__main__':
    main()
    
    