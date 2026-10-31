# Customer Churn - Data Cleaning
import pandas as pd

df = pd.read_csv('customer_churn_raw.csv')
print(df.shape)
print(df.head())

# 1. Data madhe kay chuka ahet te tapasne
print('Duplicate rows:', df.duplicated().sum())
print()
print('Missing values:')
print(df.isna().sum())
print()
print('TotalCharges madhe text (number nahi):',
      pd.to_numeric(df['TotalChargesINR'], errors='coerce').isna().sum())
print(df['MonthlyChargesINR'].describe())

# 2. Duplicate rows kadhne
df = df.drop_duplicates().reset_index(drop=True)
print(df.shape)

# 3. Monthly charge madhle chukiche (12 pat jast) aakde sudharne
median = df.groupby('SubscriptionType')['MonthlyChargesINR'].transform('median')
bad = df['MonthlyChargesINR'] > 3 * median
print('Chukiche rows:', bad.sum())
df.loc[bad, 'MonthlyChargesINR'] = (df.loc[bad, 'MonthlyChargesINR'] / 12).round(2)
print(df['MonthlyChargesINR'].describe())

# 4. TotalCharges madhle 'unknown' bharne
df['TotalChargesINR'] = pd.to_numeric(df['TotalChargesINR'], errors='coerce')
miss = df['TotalChargesINR'].isna()
print('Bharayche rows:', miss.sum())
df.loc[miss, 'TotalChargesINR'] = (
    df.loc[miss, 'MonthlyChargesINR'] * df.loc[miss, 'TenureMonths']).round(2)

# 5. Rikame Region bharne
df['Region'] = df['Region'].fillna('Unknown')
print(df['Region'].value_counts())

# 6. Shevtchi tapasni ani clean file save karne
print(df.shape)
print('Rikamya value:', df.isna().sum().sum())
df.to_csv('customer_churn_cleaned.csv', index=False)
print(df.head())
