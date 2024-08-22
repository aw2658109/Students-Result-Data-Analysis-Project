
# STUDENT RESULTS ANALYSIS:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DATA CLEANING:

df=pd.read_csv("student_scores.csv")
print(df.head(5))
#Describe Data:
print(df.describe())
#Info Fuction:
print(df.info())
#Find Total Null Value:
print(df.isnull().sum())

# DROP UNNAMED COLUMN:
df=df.drop("Unnamed: 0",axis=1 )
print(df.head())

# CHANGE WEEKLY STUDY HOURE COLUMNS:
df["WklyStudyHours"]=df["WklyStudyHours"].str.replace("10-oct","5-10")
print(df["WklyStudyHours"].head(20))

# GENDER DISTRIBUTION:
plt.figure(figsize=(5,5))
ax=sns.countplot(x="Gender",data=df)
ax.bar_label(ax.containers[0])
plt.show()

# CONCLUSION: from the above chart we have analysed that:
# the number of female in the data is more than number of the male:
plt.figure(figsize=(12,6))
gb=df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})

sns.heatmap(gb,annot=True)
plt.show()

# CONCLUSION: from the above chart we have conclued that  the education of the parents have a have a good impact on their course:

gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})

plt.figure(figsize=(5,5))
sns.heatmap(gb1,annot=True)
plt.show()

#CONCLUSION: from the above chart we have conclued that their is no/negligible impact on the:
# student score, do to dear parents, marital status
print(df)
#BOX PLOT:
sns.boxplot(data=df, x="ReadingScore")
plt.show()
print(df)
# BOX PLOT
sns.boxplot(data=df, x="MathScore")
plt.show()
print(df)
# BOX PLOT:
sns.boxplot(data=df, x="WritingScore")
plt.show()

print(df["EthnicGroup"].unique())

# DISTRIBUTION OF ETHNICGROUPS:
groupA = df.loc[(df["EthnicGroup"] == "group A")].count()
print(groupA)

groupB = df.loc[(df["EthnicGroup"] == "group B")].count()
print(groupB)

groupC = df.loc[(df["EthnicGroup"] == "group C")].count()
print(groupC)

groupD = df.loc[(df["EthnicGroup"] == "group D")].count()
print(groupD)

groupE = df.loc[(df["EthnicGroup"] == "group E")].count()
print(groupE)

l=['group A','group B','group C','group D','group E']
mlist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]

plt.pie(mlist,labels=l,autopct="%0.1f%%")
plt.title("Distribution of Groups")
plt.show()
#CountPlot:
ax = sns.countplot(data=df, x="EthnicGroup")
ax.bar_label(ax.containers[0])
plt.show()