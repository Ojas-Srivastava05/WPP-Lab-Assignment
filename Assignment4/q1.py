#kisi bhi string ko palindrome banane mei minimum number of steps batane hain
def palindromemaker(sentence):
    
    temp1=[]
    temp2=[]
    print(len(sentence))
    if len(sentence)%2==1:
        for i in range (0,(len(sentence)//2)):
            temp1.append(sentence[i])
            temp2.append(sentence[i+(len(sentence)//2)])
    elif len(sentence)%2==0:
        for i in range (0,(len(sentence)//2)):
            temp1.append(sentence[i])
            temp2.append(sentence[i+(len(sentence)//2)])
    print(temp1)
    print(temp2)
        
    return 0

def main():
    test=int(input("Enter the number of test cases"))
    result=[]
    for i in range(test):
          sentence=input("Enter the sentence of which you want to know the minimum number of steps in making palindrome ")
          result[i]=palindromemaker(sentence)
    
    print(sentence)
    
if __name__=='__main__':
    main()