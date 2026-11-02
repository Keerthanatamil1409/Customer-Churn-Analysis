import pandas as pd     
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# print("All libraries imported successfully")

df = pd.read_csv("Customer_Churn.csv")
# print(df)

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info)
# print(df.describe())
# print(df.dtypes)
# print(df.columns)

# Data Cleaning Process
# Check Null values
# print(df.isnull().sum())

# Check duplicate values
# print(df.duplicated().sum())

# Check unique values in churn
# print(df["Churn"].value_counts())                     # No-5174, Yes-1869 

# Check churn percentage
# print(df["Churn"].value_counts(normalize=True)*100)  # No-73.463013, Yes-26.536987

# Clean the dataset
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")
# print(df["TotalCharges"].dtype)
# print(df["TotalCharges"].isnull().sum())

# Handle missing values:
df = df.dropna(subset=["TotalCharges"])
# print(df.shape)

# Remove duplicate records
df = df.drop_duplicates()
df.reset_index(drop=True, inplace=True)

# Verifying cleaned dataset
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.info())
# print(df.shape)

# EDA
# print(df["Churn"].value_counts())
# print(df["Churn"].value_counts(normalize=True)*100)

# Visualization 1
# plt.figure(figsize=(6, 4))
# sns.countplot(data=df, x="Churn")
# plt.title("Customer Churn Distribution")
# plt.xlabel("Churn Status")
# plt.ylabel("Number of Customers")
# plt.show()

# Compare average tenure
# print(df.groupby("Churn")["tenure"].mean())

# Visualization 2
# plt.figure(figsize=(8,5))
# sns.boxplot(data=df, x="Churn", y="tenure")
# plt.title("Customer Churn by tenure")
# plt.xlabel("Churn Status")
# plt.ylabel("Tenure (Months)")
# plt.show()

# Calculate churn by contract
contract_churn = pd.crosstab(df["Contract"], df["Churn"])
# print(contract_churn)

# Calculate churn percentage by contract
contract_churn_percentage = pd.crosstab(df["Contract"], df["Churn"], normalize="index")*100
# print(contract_churn_percentage)


# Visualization 3
# contract_churn_percentage.plot(kind="bar",figsize=(9, 5))
# plt.title("Customer Churn by Contract Type")
# plt.xlabel("Contract Type")
# plt.ylabel("Percentage of Customers")
# plt.xticks(rotation = 0)
# plt.legend(title="Churn")
# plt.show()

# Customer churn by payment method
payment_churn = pd.crosstab(df["PaymentMethod"], df["Churn"])
# print(payment_churn)

# Calculate churn percentage by payment method
payment_churn_percentage = pd.crosstab(df["PaymentMethod"], df["Churn"], normalize="index")*100
# print(payment_churn_percentage)


# Visualization 4
# payment_churn_percentage.plot(kind="bar",figsize=(10, 5))
# plt.title("Customer Churn by Payment Method")
# plt.xlabel("Payment Method")
# plt.ylabel("Percentage of Customers")
# plt.xticks(rotation=20)
# plt.legend(title="Churn")
# plt.show()

# Customer churn by monthly charges
# Calculate average monthly charges
# print(df.groupby("Churn")["MonthlyCharges"].mean())

# Calculate median monthly charges
# print(df.groupby("Churn")["MonthlyCharges"].median())


# Visualization 5
# plt.figure(figsize=(8, 5))
# sns.boxplot(data=df, x="Churn", y="MonthlyCharges", color="Teal")
# plt.title("Customer Churn by Monthly Charges")
# plt.xlabel("Churn Status")
# plt.ylabel("Monthly Charges ($)")
# plt.show()

# Average Comparison Chart
# sns.barplot(data=df, x="Churn", y="MonthlyCharges", errorbar=None)
# plt.title("Average Monthly Charges by Churn")
# plt.xlabel("Churn Status")
# plt.ylabel("Average Monthly Charges ($)")
# plt.show()

# Correlation
numerical_df = df.select_dtypes(include=["int64", "float64"])
# print(numerical_df.head())

# Calculate correlation
correlation_matrix = numerical_df.corr()
# print(correlation_matrix)

# Heatmap
# plt.figure(figsize=(10, 6))
# sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
# plt.title("Customer Churn Analysis - Correlation Heatmap")
# plt.show()

high_risk_customers = df[(df["Contract"] == "Month-to-month") & (df["Churn"] == "Yes")]
# print(high_risk_customers.shape)
# print(high_risk_customers.head())

print("High Churn segment size:", len(high_risk_customers))
print("Percentage of all customers:", len(high_risk_customers)/len(df)*100)