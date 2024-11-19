import pandas as pd
with open ("transactions.csv",'r') as f:
    s=f.read().split('\n')
    a=[]
    for i in range(len(s)-2):
        a.append(str(s[i+1]).split(','))
        a[i][4]=int(a[i][4])
        c=''
        for j in range(len(a[i][1])-1):
            c+=a[i][1][j+1]
        a[i][1]=c
    df=pd.DataFrame(a,columns=list('ABCDE'))
    df2=pd.DataFrame(df[df['D'] == "OK"])
    df3=pd.DataFrame(df2.sort_values(by='E', ascending=False))
    print(df3.iloc[0:3])
    df3 = pd.DataFrame(df2[df2['B']=="Umbrella"])
    b=0
    for i in range(len(df3)):
        b+=df3.iat[i,4]
    print('sum of payments to Umbrella, Inc. = '+str(b))