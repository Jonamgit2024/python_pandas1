# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:08:23 2024

@author: suraj chilaka
"""

import Depedencies as dp
import FilePaths as FP
import os

path=os.chdir(FP.B_SourceDir)

print(os.getcwd())

###Show Starts here #####

DataF=dp.ReadFiles(FP.B_File1)
DataF1=dp.ReadFiles(FP.B_File2)

DataF=dp.AddNewColumnAudittoBronze(DataF)
DataF1=dp.AddNewColumnAudittoBronze(DataF1)
DFF=dp.AppendTwoDFToCSV(DataF,DataF1)


DestPath=os.chdir(FP.B_DestDir)
print(os.getcwd())
DFF=dp.DestinationFile(DFF,'Silver_Data.csv')


