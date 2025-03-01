
from datetime import datetime
import Depedencies as dp
import FilePaths as FP
import os
import pandas as pd
"""
Read BL data
People with similar countries

"""

def AnalyzeDatabyCountry(DF,CountryName):
    CountryDF=DF.query('Country== @CountryName',inplace=False)
    return CountryDF

def PayeeIDwithDays(DF):
    now = datetime.now()
    print("Numof Cols: ",dp.FindNumofCol(DF))
    
    print("Numof Rows: ",dp.FindNumofRow(DF))
    date_time = now.strftime("%m/%d/%Y")
    print(date_time)
    tempV= pd.DataFrame(DF['Subscription Date'])
    print(tempV)
    #conve to string and remove index
    # tempV=tempV.to_string(index=False)
    tempV['Subscription Date']=tempV['Subscription Date'].dt.strftime("%m/%d/%Y")
    print(tempV)
    # for i in tempV:
    #     tempV[i]=tempV[i]-date_time
        
    # print(tempV)

###Fun Starts here ####
path=os.chdir(FP.S_Sourcepath)
print(os.getcwd())

SF=dp.ReadFiles(FP.S_File)

China_vals=AnalyzeDatabyCountry(SF,"China")
print(China_vals)

print(PayeeIDwithDays(China_vals))