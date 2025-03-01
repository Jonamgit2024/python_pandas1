from datetime import datetime
import pandas as pd


df=pd.read_csv('Audit_Bronze_updated_timestamp_column.csv')

# Cleaning empty cells 

def CheckforNan(DF) :
    noofrowsbeforeCleanofNan=len(DF)
    new_DF=DF.dropna()
    noofrowsafterCleanofNan=len(new_DF)
    noofrowsremovedCleanofNan=(noofrowsbeforeCleanofNan - noofrowsafterCleanofNan)
    if(noofrowsremovedCleanofNan == 0):
        print(f"No of Rows in CSV file after removing empty cells is same as before {noofrowsbeforeCleanofNan}")
    else:
        print(f"Empty cells are present in the csv file which are removed now")

def AnalyzeDatabyCountry(DF,CountryName):
    CountryDF=DF.query('Country== @CountryName',inplace=False)
    return CountryDF

def NoofUniquecountries(DF):
    #To get unique data providing countries
    uniquecountries =DF['Country'].unique()
    noofuniquecountires =uniquecountries.size
    print(f"No of Unique Countries is{noofuniquecountires}")
    #Print China vals
    # China_vals=AnalyzeDatabyCountry(df,"China")
    # print(China_vals)

def checkforcustomerids(DF):
    uniquecustomerids=DF['Customer Id'].unique()
    noofuniquecustomers=uniquecustomerids.size
    print(f"No of Unique Customers is{noofuniquecustomers}")
    noofrows=len(df)
    if(noofrows == noofuniquecustomers):
        print(f"No of Users is {noofrows} and Unique Customers is {noofuniquecustomers} both are same")
    else:
        print(f"No of Users is {noofrows} and Unique Customers is {noofuniquecustomers} both are not same")

#Printing Coutnries after sorted out by Name
def CountriesPrintedbyName(DF):

    sorted_df = DF.sort_values(by=['Country'], ascending=True)
    sorted_df.to_csv('Audit_Silver_countries_sorted.csv', index=False)

# Subscription time
def Subscriptiontime(DF):
    #First Correct the Data for wrong data formats - since, Empty cells is not there
    DF['Subscription Date'] = pd.to_datetime(DF['Subscription Date'], format='mixed')
    # Now, we ensure all dates are formatted in the desired format, for example, MM/DD/YYYY
    DF['Subscription Date'] = DF['Subscription Date'].dt.strftime('%m/%d/%Y')
    # Converting String to Time Stamp for checking the difference
    DF['Subscription Date'] = pd.to_datetime(DF['Subscription Date'], format='%m/%d/%Y', errors='coerce')
    current_date = datetime.now().strftime('%m/%d/%Y')
    # Convert current date to datetime format to enable comparison
    current_date_obj = pd.to_datetime(current_date, format='%m/%d/%Y')
    DF['Current Data'] =current_date
    # Calculate the difference in days between the current date and the 'OldDate'
    DF['SubscriptionTime'] = (current_date_obj -DF['Subscription Date']).dt.days

def UserssortedbyTime(DF):

    sorted_df = DF.sort_values(by=['Subscription Date'], ascending=True)
    sorted_df.to_csv('users_sorted_based_on_length_of_subscription.csv', index=False)

Subscriptiontime(df)
CheckforNan(df)
checkforcustomerids(df)
UserssortedbyTime(df)
CountriesPrintedbyName(df)

