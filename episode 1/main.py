import pandas as pd
df=pd.read_csv('transactions.csv')
df2=pd.DataFrame(df[df['STATUS'] == "OK"])
df3=pd.DataFrame(df2.sort_values(by='SUM', ascending=False))
print(df3.iloc[0:3])
df3 = pd.DataFrame(df2[df2['CONTRACTOR']=="Umbrella, Inc"])
b=(df3.iloc[:,3].sum())
print('sum of payments to Umbrella, Inc. = '+str(b))