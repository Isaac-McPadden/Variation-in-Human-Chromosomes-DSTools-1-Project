import csv
import pandas as pd
import numpy as np
import os
import pickle

directory='F:\\Genetics Data\\Chromosome CSVs\\'
chromosomeNums=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y']
chrDict={}
for file in os.listdir(directory):
    valcounts=[]
    if file.endswith('.csv'):
        fileDir=(directory+file)
        chrDF=pd.read_csv(fileDir,index_col=0,low_memory=False)
        chrDF=chrDF.drop(['ID'], axis=1)
        keyName=str(file)
        simpChrDF=chrDF.drop(['POS','REF','ALT','ALLELE'], axis=1)
        #print(chrDF.head())
        for col in simpChrDF:
            a=pd.Series(simpChrDF[col]).value_counts()
            valcounts.append(a)
        chrDict[keyName]=valcounts
#print(chrDict)

pickle.dump(chrDict, open("simpickle.pkl", "wb"))

