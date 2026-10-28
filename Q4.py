import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd
import seaborn as sns


#Question 4
df = pd.read_csv("student_performance.csv")

#diamensions
diamensions = df.shape
print('Dimensions of the dataset:', diamensions)

#data types
data_types = df.dtypes
print('Data types of the dataset:', data_types)

#first 5 rows of table
first_five_rows = df.head()
print('First five rows of the dataset:\n', first_five_rows)

#basic summary statistics
basic_summary_statistics = df.describe()
print('Basic summary statistics of the dataset:\n', basic_summary_statistics)


#mean
mean_exam_score = df['Exam'].mean()
print('Mean of exam scores:', mean_exam_score)

#median
median_exam_score  = df['Exam'].median()
print('Median of exam scores:', median_exam_score)

#standard deviation
sd = df["Exam"].std()
print("Standard deviation:", sd)

#identifiyng the student with thw higest exam marks
highest_exam_score = df['Exam'].max()
student = df[df["Exam"] == highest_exam_score]
print("Student : ", student)


#pearson corelation
r = df["Study Hours"].corr(df["Exam"], method="pearson")
print("Pearson correlation:", r)

#categorizing
# # Remove duplicate rows and missing values
df = df.drop_duplicates()
df = df.dropna(subset=["Study Hours", "Exam", "Assignment"])

# Group Exam marks into categories
def categorize_marks(mark):
    if mark < 60:
        return "Low"
    elif mark < 80:
        return "Medium"
    else:
        return "High"

df["Category"] = df["Exam"].apply(categorize_marks)

# Export cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Calculate summary statistics
summary = df.describe(include="all")

# Export summary statistics
summary.to_csv("summary_statistics.csv")

print("Cleaned data and summary statistics exported successfully.")



#plots
df = pd.read_csv("cleaned_data.csv")
#scatter plot study hours vs exam marks
plt.figure(figsize=(8, 5))
plt.scatter(df["Study Hours"], df["Exam"])
plt.xlabel("Study Hours")
plt.ylabel("Exam marks")
plt.title("Study Hours vs Exam Marks")
plt.show()
#histogram of exam marks
plt.figure(figsize=(8, 5))
plt.hist(df["Exam"], bins=10, edgecolor="black")
plt.xlabel("Exam marks")
plt.ylabel("Frequency")
plt.title("Distribution of Exam Marks")
plt.show()
#box plot of exam marks 
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Exam"])
plt.ylabel("Exam marks")
plt.title("Box Plot of Exam Marks")
plt.show()
#heatmap of study hours vs assignment marks
plt.figure(figsize=(8, 5))

heatmap_data = df[["Study Hours", "Assignment"]].corr()

sns.heatmap(
    heatmap_data,
    annot=True,
    vmin=-1,
    vmax=1
)

plt.title("Correlation Heatmap: Study Hours vs Assignment Marks")
plt.show()


