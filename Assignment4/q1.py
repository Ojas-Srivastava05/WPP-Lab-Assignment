#kisi bhi string ko palindrome banane mei minimum number of steps batane hain
def palindromemaker(sentence):
    count=0
    n=len(sentence)
    for i in range(n // 2):
        count += abs(ord(sentence[i]) - ord(sentence[n - i - 1]))
    # print(len(sentence))
    # if len(sentence)%2==1:
    #     for i in range (0,(len(sentence)//2)):
    #         temp1.append(sentence[i])
    #         temp2.append(sentence[i+(len(sentence)//2)])
    #         count=count+abs((ord(temp2[i])-ord(temp1[i])))
    # elif len(sentence)%2==0:
    #     for i in range (0,(len(sentence)//2)):
    #         temp1.append(sentence[i])
    #         temp2.append(sentence[i+(len(sentence)//2)])
    #         count=count+abs((ord(temp2[i])-ord(temp1[i])))
    # print(temp1)
    # print(temp2)
        
    return count

def main():
    test=int(input("Enter the number of test cases"))
    result=[]
    for i in range(test):
          sentence=input("Enter the sentence of which you want to know the minimum number of steps in making palindrome ")
          result.append(palindromemaker(sentence))
    
    print("\n".join(map(str,result)))
    
if __name__=='__main__':
    main()