def utopiantree(n):
    length=1
    num=n
    for i in range (1,num+1):
        if i%2==1:
            length=length*2
        else:
            length=length+1
    return length

def main():
    test=int(input("Enter the number of test cases"))
    for i in range (1,test+1):
        n=int(input("Enter the number of cycles"))
        print(utopiantree(n))
                
if __name__=='__main__':
     main()
    