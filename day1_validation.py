import pandas as pd

fund_master = pd.read_csv("data/raw/fund_master.csv")
nav_history = pd.read_csv("data/raw/nav_history.csv")

print("=" * 50)
print("FUND MASTER EXPLORATION")
print("=" * 50)

print("\nFund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())

print("\n" + "=" * 50)
print("AMFI CODE VALIDATION")
print("=" * 50)

fm_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = fm_codes - nav_codes

print("\nMissing AMFI Codes:")
print(missing)

if len(missing) == 0:
    print("\nValidation Passed ✓")
else:
    print("\nValidation Failed ✗")