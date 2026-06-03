import pandas as pd

df = pd.read_csv("data/raw/scheme_performance.csv")

print("Original Shape:", df.shape)

# Numeric columns
numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

# Convert to numeric
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check missing numeric values
print("\nMissing Values:")
print(df[numeric_cols].isnull().sum())

# Expense Ratio Validation
anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:", len(anomalies))

# Remove duplicates
duplicates = df.duplicated().sum()
print("Duplicates Found:", duplicates)

df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaned Shape:", df.shape)
print("scheme_performance_cleaned.csv saved successfully!")