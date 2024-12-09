import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('flights.csv')
arr = []
brr = []
crr = []
df2=pd.DataFrame(df[df['CARGO'] == "Nimble"])
n=len(df2)
print("Nimble")
print("n="+str(n))
arr.append(n)
b = df2.loc[:,'PRICE'].sum()
print("Price=" + str(b))
brr.append(b)
b = df2.loc[:,'WEIGHT'].sum()
print("Weight="+str(b))
crr.append(b)


df2 = pd.DataFrame(df[df['CARGO'] == "Jumbo"])
n = len(df2)
print("Jumbo")
print("n="+str(n))
arr.append(n)
b = df2.loc[:,'PRICE'].sum()
print("Price=" + str(b))
brr.append(b)
b = df2.loc[:,'WEIGHT'].sum()
print("Weight="+str(b))
crr.append(b)



df2 = pd.DataFrame(df[df['CARGO'] == "Medium"])
n = len(df2)
print("Medium")
print("n="+str(n))
arr.append(n)
b = df2.loc[:,'PRICE'].sum()
print("Price=" + str(b))
brr.append(b)
b = df2.loc[:,'WEIGHT'].sum()
print("Weight="+str(b))
crr.append(b)


x=['Nimble','Jumbo','Medium']
plt.plot(x,arr)
plt.title('number of flights')
plt.savefig("1.png")
plt.show()
plt.plot(x, brr)
plt.title('price')
plt.savefig("2.png")
plt.show()
plt.plot(x, crr)
plt.title('weight')
plt.savefig("3.png")
plt.show()