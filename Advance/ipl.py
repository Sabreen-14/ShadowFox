import pandas as pd

file_path = input("Enter your IPL Excel file path: ").strip().strip('"')

# load file
data = pd.read_excel(file_path, skiprows=3)

# set correct header
data.columns = data.iloc[0]
data = data[1:]
data.reset_index(drop=True, inplace=True)

# ❌ DROP EMPTY COLUMN (first NaN column)
data = data.loc[:, data.columns.notna()]

# clean column names
data.columns = data.columns.str.strip()

# remove rows where Teams is invalid
data = data[data['Teams'].str.contains("Capitals|Mumbai|Chennai|Kolkata|Punjab|Bangalore|Hyderabad|Rajasthan", na=False)]

print("\nCleaned Data:\n")
print(data.head())

print("\nTotal Rows:", len(data))


# 🔥 FINAL ANALYSIS

print("\nTop Teams:\n")
print(data['Teams'].value_counts().head())

print("\nTop Players:\n")
print(data['Player Name'].value_counts().head())

print("\nTop Venues:\n")
print(data['Venue'].value_counts().head())

