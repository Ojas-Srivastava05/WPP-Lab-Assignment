#program to capitalize alternate letters of the word
word=input("ENTER THE WORD TO CAPITALIZE")
new_word=""


for i in range(len(word)):
    if i%2!=0:
        new_word+=word[i].upper()
    else:
        new_word+=word[i].lower()
        

    
print(new_word)
    
