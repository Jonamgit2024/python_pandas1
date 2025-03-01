
from test3 import isVowel
# def isVowel(ch):
#     ch=ch.lower()
#     if(ch =='a'or ch =='e'or ch =='i'or ch =='o'or ch=='u'):
#         print(f"Given Character is an Vowel: {ch}")
#         return True 
#     else:
#         return False

print('Enter the String')
#Sequence of Characters I assume he meant a string else I can use for loop for char
Sentence=input()
length=len(Sentence)
noofvowels=0
for i in range(length) :
        if(isVowel(Sentence[i])==True):
            noofvowels=noofvowels+1

print(f"Total No of Vowels in given sentence{Sentence} is : {noofvowels}")
