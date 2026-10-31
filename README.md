# Customer Churn - Data Cleaning

Python (pandas) वापरून customer churn dataset ची data cleaning केली.

## Files
- `customer_churn_raw.csv` - मूळ (अस्वच्छ) data
- `data_cleaning.py` - cleaning चा code
- `customer_churn_cleaned.csv` - स्वच्छ केलेला data

## Cleaning steps
1. Missing values, duplicates आणि चुकीचे values तपासले
2. Duplicate rows काढल्या
3. Monthly charges मधले चुकीचे (12 पट जास्त) आकडे दुरुस्त केले
4. TotalCharges मधले "unknown" values भरले (Monthly charges × Tenure)
5. रिकाम्या Region ला "Unknown" भरले
6. Clean file save केली

## Tools
Python, pandas
