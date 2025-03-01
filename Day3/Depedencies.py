# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:08:23 2024

@author: suraj chilaka
"""

import os
import pandas as pd
import time

def PathCheck(path):
    if(os.path.exists(path)):
        return True
    else:
        return False

def IsfileValid(fileName):
    if fileName in os.listdir():
        return True
    else:
        return False

def ReadFiles(Name):
    if(IsfileValid(Name)==True):
        print("CHECKED FOR FILE")
        print(Name)
        RF=pd.read_csv(Name)
    else:
        print("File Not found")
        return 0
    return RF

def GetCurrentTime():
    K= time.time()
    readable_time = time.ctime(K)
    return readable_time


def AppendTwoDFToCSV(DF,DF1):
    DFF=pd.concat([DF,DF1])
    return DFF



def DestinationFile(DF,FileName):
    DF.to_csv(FileName,index=False)


def PrintDF(DF):
    print(DF)

def FindNumofCol(DF):
    return len(DF.columns)


def FindNumofRow(DF):
    return len(DF)

def AddNewColumnAudittoBronze(DF):
    K= time.time()
    readable_time = time.ctime(K)
    DF['timeprocessed_']= readable_time
    DF['audit_']=''
    return DF
