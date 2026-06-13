import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import correlate

df=pd.read_csv("students.csv") #for load csv file
print(df)
print(df.head())#head is used for checking only first few rows,large datasets may contain thousands of rows.
print(df.info())#it tells no.of rows,no.of columns, data types, missing values
print(df.describe())#quick statistical overview,mean, standard deviation, max, min
#calucating average
avg=df["marks"].mean()
print("avg marks:",avg)
print("max marks:",df["marks"].max())
print("min marks:",df["marks"].min())
#bar chart( compare categories likes st marks, sales population.(not suitable for relationship btw variables)
plt.bar(df["student"],df["marks"])
plt.xlabel(df["student"])
plt.ylabel(df["marks"])
plt.show()
#scatter plot(use to find relationship
plt.scatter(df["studyhours"],df["marks"])
plt.xlabel("studyhours")
plt.ylabel("marks")
plt.title("study hours vs marks")
plt.show()
#correlation matrix(how strongly 2 variables are related)+1 strong positive
correlation=df.corr(numeric_only=True)
print(correlation)
#heatmap(visually show relationships, darker color indicates stronger correlation)
sns.heatmap(correlation,
            annot=True,
            cmap="coolwarm")
plt.title("correlation Heatmap")
plt.show()