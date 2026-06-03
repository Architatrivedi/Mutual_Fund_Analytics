import pandas as pd
import os

# 1. Aapke folder ki saari 10 CSV files ke exact naam
csv_files = [
    "aum_by_fund_house.csv",
    "benchmark_indices.csv",
    "category_inflows.csv",
    "fund_master.csv",
    "industry_folio_count.csv",
    "investor_transactions.csv",
    "monthly_sip_inflows.csv",
    "nav_history.csv",
    "portfolio_holdings.csv",
    "scheme_performance.csv"
]

# Path jahan aapne files rakhi hain
data_directory = "data/raw/"

print("--- STARTING DATA INSPECTION (TASK 3) ---")

for file_name in csv_files:
    file_path = os.path.join(data_directory, file_name)
    
    if os.path.exists(file_path):
        print(f"\n==================== CHECKING: {file_name} ====================")
        df = pd.read_csv(file_path)
        
        # 1. Print Shape (Rows, Columns)
        print(f"Rows aur Columns (Shape): {df.shape}")
        
        # 2. Print Data Types
        print("\nData Types (dtypes):")
        print(df.dtypes)
        
        # 3. Print Head (First 5 Rows)
        print("\nUpar ke 5 Rows (head):")
        print(df.head(5))
    else:
        print(f"\n[ALERT] File nahi mili: {file_name} | Ise data/raw/ me check karo.")

print("\n--- DATA INSPECTION FINISHED ---")