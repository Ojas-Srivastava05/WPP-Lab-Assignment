#halloween party
def halloweenparty(k):
    if k%2==0:
        return (k//2)**2
    else:
        return (k//2)*((k//2)+1)

def main():
     t=int(input("Enter the number of test cases"))
     list=input("Enter the values separated by spaces")
     list=list.split(" ")
     if len(list)>t:
         print("Invalid input")
         return 0
     for k in range(0,t):
         val=halloweenparty(int(list[k]))
         print(val)
         
if __name__=='__main__':
    main()
    