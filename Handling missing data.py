import pandas as pd
data={
    "Name":["kunal",None,"Sumit","Rajan","sujeet","Pranav","Rajeev"],
    "Age":[20,None,40,50,60,65,40],
    "Salary":[10000,None,20000,10000,30000,500000,30000]
}
df=pd.DataFrame(data)
print(df)

# finding the null values
print(df.isnull())

# counting the null values
print(df.isnull().sum())

# Removing missing values using dropna method
print(df.dropna(axis=0))

# Replace missing values with another value
df["Salary"]=df["Salary"].fillna(50000)
df["Name"]=df["Name"].fillna("Saurabh")
df["Age"]=df["Age"].fillna(65)
print(df)




