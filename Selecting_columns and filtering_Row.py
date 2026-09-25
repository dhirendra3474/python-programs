import pandas as pd
data={
    "Name":["Kunal","Sumit","Subham","Sujeet","Aman","Nikhil","Vineet","Ayush","Akhand","Amit","Ajit"],
    "Age":[10,20,30,40,50,60,70,80,90,95,100],
    "Salary":[20000,50000,60000,4000,40000,50000,70000,80000,90000,80000,70000],
    "Performance_Score":[50,60,50,80,90,70,80,65,94,78,62]
}
df=pd.DataFrame(data)
df.to_excel("dataexcel.xlsx",index=False)
print("This is my DataFrame!")
print(df)
print("showing only one column!")
print(df["Name"])
print("showing multiple columns!")
print(df[["Name","Salary"]])
print(df[["Age","Performance_Score"]])
print("Showing the employe which salary is more than 50000")
print(df[df["Salary"]>50000])
print("Showing the employee which salary is = 80000")
print(df[df["Salary"]==80000])
print("Showing the employee which salary is less than 50000")
print(df[df["Salary"]<50000])
print("Showing the employee which salary is more than 1000000")
print(df[df["Salary"]>1000000])
print("Showing the employee which salary is more than 10000 and less than 500000")
new_data=df[(df["Salary"]>1000)& (df["Salary"]<50000)]
print(new_data)
print("Showing the employee which salary is more than 100000 and performance score is more than 80")
updated_performance=df[(df["Salary"]>510000) &(df["Performance_Score"]>0)]
print(updated_performance)
print("Showing the employee which salary is more than 50000 and the age is above to 95 years")
updated_age=df[(df["Salary"]>50000) & (df["Age"]>=95)]
print(updated_age)
print("Showing the employee which performance score is more than 50 or salary is more than 50000")
updated_data2=df[(df["Performance_Score"]>=50) |(df["Salary"]>50000)]
print(updated_data2)
print("Showing the employe which age is less than 30 and salary is more than 18000 ")
updated_salary=df[(df["Age"]<30) & (df["Salary"]>18000)]
print(updated_salary)
