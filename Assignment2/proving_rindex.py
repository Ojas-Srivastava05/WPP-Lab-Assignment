def indexfunction(sentence,letter):
    value=0
    for i in range(len(sentence),len(letter)-1,-1):
        for k in range(len(letter)):
            print(sentence(k))

            
            

def main():
    string=input("Enter the main string ")
    sub_string=input("Enter the substring")
    indexfunction(string,sub_string)

