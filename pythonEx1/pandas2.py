'''
Created on 2020. 8. 14.

@author: GDJ24
'''
import pandas as pd

infile = "kuro.csv"
outfile = "pandasKuro.csv"
df = pd.read_csv(infile)
print(df)

print(df["경도"])