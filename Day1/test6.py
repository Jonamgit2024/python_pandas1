import math
import random

def doublenumber(num):
    num1= num*2
    return num1

#Assuming 2 digit number
def reversedigits(num):
    tens=int(num/10)
    ones=num%10
    reverse = ones*10+tens
    return reverse

def raisepower(num, power):
    product = 1
    for x in range(power):
        product  = num*product
    return product
    # if(power ==1):
    #     return num
    # elif(power ==2):
    #     return num*num
    # elif(power ==3):
    #     return num*num*num
    # elif(power ==4):
    #     return num*num*num*num
    # else:
    #     print('Happens only for power of 1,2,3 and 4')        
#Assuming 2 digit number
def sumofdigits(num):
    tens=int(num/10)
    ones=num%10
    sumofdigits = ones+tens
    return sumofdigits

def firstdigittopowerofsecond(num):
    tens=int(num/10)
    ones=num%10
    power =math.pow(tens,ones)
    return power


randomnumber = random.randint(0,99)
print('Enter the Power you want to raise to')
power =int(input())
num = randomnumber

print('Random Number generated is ',num)
print('Double of the digit is ',doublenumber(num))
print('Reversing the digits',reversedigits(num))
print(f"Raising it to given Power {power} is : {raisepower(num, power)}")
print('Sum of All digits is ',sumofdigits(num))
print('Raising Power of First to Second',firstdigittopowerofsecond(num))