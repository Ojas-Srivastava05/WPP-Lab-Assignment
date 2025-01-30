def digitalroot(number):
    num=number
    rem=0
    sum=0
    while num!=0:
        rem=num%10
        num=num//10
        sum=sum+rem
        if sum>=10:
            rem=sum%10
            sum=sum//10
            sum=sum+rem
    return sum

def main():
    number=int(input("Enter a number"))
    print(digitalroot(number))
    

if __name__=='__main__':
    main()
    
    