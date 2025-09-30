# week7.py
# Data Analysis and Visualization with Pandas and Matplotlib
# Using the Iris dataset from sklearn (no CSV needed)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Make plots look nicer
sns.set(style="whitegrid")

# -----------------------------
# Task 1: Load and Explore the Dataset
# -----------------------------

# Load Iris dataset as a Pandas DataFrame
iris = load_iris(as_frame=True)
df = iris.frame  # DataFrame with features + target
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))  # add species names

print("✅ Dataset loaded successfully!\n")

# Display first 5 rows
print("🔎 First 5 rows of the dataset:")
print(df.head())

# Dataset info (structure, datatypes, missing values)
print("\n📊 Dataset Info:")
print(df.info())

# Check for missing values
print("\n❓ Missing Values Count:")
print(df.isnull().sum())

# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------

# Statistical summary
print("\n📈 Statistical Summary:")
print(df.describe())

# Group by species and compute average petal length
grouped = df.groupby("species")["petal length (cm)"].mean()
print("\n📊 Average petal length per species:")
print(grouped)

# -----------------------------
# Task 3: Data Visualization
# -----------------------------

# 1. Line Chart (trend across index just for demo)
df["sepal length (cm)"].plot(kind="line", figsize=(8,5), title="Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# 2. Bar Chart (average petal length per species)
df.groupby("species")["petal length (cm)"].mean().plot(kind="bar", color="skyblue", figsize=(7,5))
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal length)
df["sepal length (cm)"].plot(kind="hist", bins=20, color="orange", edgecolor="black", figsize=(7,5))
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (relationship between sepal length and petal length)
plt.figure(figsize=(7,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

print("\n✅ Analysis complete! Check the visualizations above.")