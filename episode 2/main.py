import matplotlib.pyplot as plt
import pandas as pd
with open ("flights.csv",'r') as f:
    s=f.read().split('\n')
    a=[]
    for i in range(len(s)-1):
        a.append(str(s[i+1]).split(','))
    df=pd.DataFrame(a,columns=list('ABCD'))
    arr = []
    brr = []
    crr = []
    n=len(df[df['B'] == "Nimble"])
    print("Nimble")
    print("n="+str(len(df[df['B'] == "Nimble"])))
    df2=pd.DataFrame(df[df['B'] == "Nimble"])
    arr.append(n)
    b = 0
    for i in range(len(df2)):
        b += int(df2.loc[i, 'C'])
    print("Price=" + str(b))
    brr.append(b)
    b=0
    for i in range(len(df2)):
        b+=int(df2.loc[i,'D'])
    print("Weight="+str(b))
    crr.append(b)

    n = len(df[df['B'] == "Jumbo"])
    print("Jumbo")
    print("n=" + str(len(df[df['B'] == "Jumbo"])))
    df2 = pd.DataFrame(df[df['B'] == "Jumbo"])
    arr.append(n)
    b = 0
    for i in range(len(df2)):
        b += int(df2.loc[i+arr[0], 'C'])
    print("Price=" + str(b))
    brr.append(b)
    b = 0
    for i in range(len(df2)):
        b += int(df2.loc[i+arr[0], 'D'])
    print("Weight=" + str(b))
    crr.append(b)


    n = len(df[df['B'] == "Medium"])
    print("Medium")
    print("n=" + str(len(df[df['B'] == "Medium"])))
    df2 = pd.DataFrame(df[df['B'] == "Medium"])
    arr.append(n)
    b = 0
    for i in range(len(df2)):
        b += int(df2.loc[i+arr[0]+arr[1], 'C'])
    print("Price=" + str(b))
    brr.append(b)
    b = 0
    for i in range(len(df2)):
        b += int(df2.loc[i+arr[0]+arr[1], 'D'])
    print("Weight=" + str(b))
    crr.append(b)


    x=[1,2,3]
    plt.plot(x,arr,label='number of flights')
    plt.plot(x, brr, label='price')
    plt.plot(x, crr, label='weight')
    plt.title("Comparison of Nimble, Jumbo and Medium airlines")
    plt.legend()
    plt.savefig("1.png")
    plt.show()