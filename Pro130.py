import pandas as pd
import csv

df = pd.read_csv("Project129.csv")
print(df.shape)
del df['Serial1']
del df['Serial2']
del df['Distance1']
del df['Mass1']
del df['Radius1']
print(df.shape)

df.to_csv("Project130.csv")