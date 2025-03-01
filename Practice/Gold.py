import pandas as pd


df=pd.read_csv('Audit_Bronze_updated_timestamp_column.csv')

#Renaming column phone 1 to phone1 to round out an problem while defininf the function
df = df.rename(columns={df.columns[7]: 'Phone1'})
print(df)
#Removing Incorrect phone numbers having alphabets and having digits less than 10 and more than 17
def validate_phone_number_format_and_size(phone_number):
    noofdigits=len(phone_number)
    if(phone_number.isalpha() == False):
        if(noofdigits>=10):
            if(noofdigits<=17):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def Checking_and_Sorting_data_for_phonenumber(DT,Phone1):
    #Applying Lamda to Pandas Data frame for multi verification
    DT['Phone_number_1_Verified']=DT['Phone1'].apply(lambda x: validate_phone_number_format_and_size(str(x)))
    sorted_DT=DT.sort_values(by=['Phone_number_1_Verified'], ascending=False)
    sorted_DT.to_csv('Audit_Gold_verified_phone_number.csv', index=True)



file_path = 'Audit_Bronze_updated_timestamp_column.csv' 
column_name = 'Phone1' 
df =Checking_and_Sorting_data_for_phonenumber(df,column_name)