#Using same reminder variable for all - Just to check value over riding
print('Enter the Money')
moneyindollars =int(input())
print('Entered Money is :',moneyindollars)
hundreds =int(moneyindollars/100)
reminder=moneyindollars%100
print(f"No.of hunders in {moneyindollars} is : {hundreds}.")
fifties = int(reminder/50);
reminder=reminder%50;
print(f"No.of fifties in {moneyindollars} is : {fifties}.")
tens=int(reminder/10);
reminder=reminder%10;
print(f"No.of Tens in {moneyindollars} is : {tens}.")
#Verification
totalamount=(hundreds*100)+(fifties*50)+(tens*10)+reminder

if (moneyindollars==totalamount):
    print('verified')
    print(f"Money Entered {moneyindollars} is equal to :{hundreds}*100+{fifties}*50+{tens}*10+{reminder}")
else:
    print('Program is Faulty')