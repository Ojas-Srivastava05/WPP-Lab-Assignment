#kisi bhi string ko palindrome banane mei minimum number of steps batane hain
def palindromemaker(sentence):
    sentence=sentence.split()
    
    pass

def main():
    test=int(input("Enter the number of test cases"))
    result=[]
    for i in range(test):
          sentence=input("Enter the sentence of which you want to know the minimum number of steps in making palindrome ")
          result[i]=palindromemaker(sentence)
    
    print(sentence)