import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("raw_data.csv")

print("Original Data:")
print(df)

# Handle missing values
df.fillna(df.median(numeric_only=True), inplace=True)

print("\nCleaned Data:")
print(df)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Create folder for plots
if not os.path.exists("plots"):
    os.makedirs("plots")

# Plot 1: Applicant Income Distribution
plt.figure()
df["ApplicantIncome"].hist()
plt.title("Applicant Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.savefig("plots/income_distribution.png")
plt.close()

# Plot 2: Loan Amount vs Credit History
plt.figure()
plt.scatter(df["LoanAmount"], df["Credit_History"])
plt.title("Loan Amount vs Credit History")
plt.xlabel("Loan Amount")
plt.ylabel("Credit History")
plt.savefig("plots/loan_vs_credit.png")
plt.close()

print("\nCleaning and visualization completed successfully.")
