#kisi bhi string ko palindrome banane mei minimum number of steps batane hain
def palindromemaker(sentence):
    count=0
    n=len(sentence)
    for i in range(n // 2):
        count += abs(ord(sentence[i]) - ord(sentence[n - i - 1]))
        
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