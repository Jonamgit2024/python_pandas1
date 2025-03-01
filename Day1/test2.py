def is_Palindrome():
    print('Enter the String')
    str1 =input()
    #Converted to Lower Case
    str =str1.lower()
    print(f"Given String : {str1} is convereted to lower case {str} to make it case -insensitive")
    a=0
    strlen=len(str)
    halflen=int(strlen/2)
    print('Length of string is :',strlen)
    #using range function in for loop to avoid not iterable error
    for i in range(halflen) :
        if str[i] != str[strlen-i-1]:
            #Writing Print statements in for or if will iterate still using break palindrome case will print
            a=1
            break

    if(a==0):
        print(f"Given String : {str1} is a Palindrome .")
    
    else:
        print(f"Given String : {str1} is not a Palindrome.") 



is_Palindrome()