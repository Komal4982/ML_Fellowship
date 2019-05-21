import pandas as pd
df = pd.Series([2, 4, 6, 8, 10])
df1 = pd.Series([1, 3, 5, 7, 9])
df2 = df + df1
print("Add pandas two series:=""\n", df2)


df2 = df - df1
print("Subtract pandas two series:=""\n", df2)


df2 = df * df1
print("Multiply pandas two series:=""\n", df2)


df2 = df / df1
print("divided pandas two series:=""\n", df2)
