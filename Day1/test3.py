
def isVowel(ch):
    ch=ch.lower()
    print(f"Given Character in lower cases is {ch}")
    if(ch =='a'or ch =='e'or ch =='i'or ch =='o'or ch=='u'):
        return True     
    else:
        return False

print('Enter the Character')
#ignore warning is added to surpress the warnings of string to character
#character =chr(input()) 
#Such cases didn't work ..So, I took a different approach and took it as string
character=input()
length=len(character)
if(length==1):
    if(isVowel(character)==True):
        print('Given Character is an Vowel')
    else:
        print('Given Statement is not an Vowel')
else:
    print('Invalid Entry - Please Enter a "Character" not a String')