import pandas as pd
data={
    "Name":["Kunal","Sumit","Sujeet","Aman","Shubham","Ramesh","Sanjay","Vijay","Suresh","Rajeev"],
    "Age":[20,30,40,50,60,20,45,56,52,25],
}
df=pd.DataFrame(data)
print(df)

df["Grade"]=[1,2,3,4,6,7,5,6,8,5]
print(df)
df["Salary"]=[20000,10000,40000,50000,60000,20000,50000,6000,4000,5000,]
df["Bonuses"]=df["Salary"]*0.10
df["Updated_salary"]=df["Salary"]+df["Bonuses"]
print(df)

df.insert(2,"City",["Ayodhya","Noida","Gurgram","Delhi","Punjab","New Delhi","Haryana","Lucknow","Mumbai","Panipat"])
print(df)


