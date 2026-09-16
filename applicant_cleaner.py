import pandas as pd
## 1. Load Dataset

df = pd.read_csv("applicant_data.csv")
print("---- Raw Applicant Data ----")
print(df.head())

## 2. Handle Duplicates

df = df.drop_duplicates()

## 3. Handle Outliers

df.loc[(df["Age"] < 0) | (df["Age"] > 100), "Age"] = 23

## 4. Standardize Text

df["Name"] = df["Name"].str.title()
df["Skills"] = df["Skills"].str.lower()

print("\n---- Cleaned & Standardize Applicant Data ----")
print(df.head())

## 5. Save cleaned Data
df.to_csv("Cleaned_applicant_data.csv", index=False)
print("\n Success: Data cleaned successfully!")
