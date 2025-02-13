#bigger is greater
def bigisgreater(sentence):
    count=1
    result=[]
    for i in range(0,len(sentence)):#list index
        for j in range(len(sentence[i]),-1.-1):#selection loop
            for k in range(len(sentence[i])-1,-1,count):#comparison loop
                if sentence[j]>sentence[k]:
                    temp=sentence[i]
                    sentence[i]=sentence[j]
                    sentence[j]=temp
                    result.append(sentence[i])
                else:
                    count+=1
                    
                    
                

def main():
    t=int(input("Enter the number of test cases"))
    sentence=[]
    for i in range(0,t):
        sen=input("Enter the sentence")
        sentence.append(sen)
        
    print(bigisgreater(sentence))
    
if __name__=='__main__':
    main()
        