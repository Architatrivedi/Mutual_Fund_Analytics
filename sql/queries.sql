-- Top 5 funds by AUM
SELECT scheme_name,aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Transactions by state
SELECT state,COUNT(*)
FROM fact_transactions
GROUP BY state;

-- SIP Count
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- Expense Ratio <1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Fund Count by Risk
SELECT risk_grade,COUNT(*)
FROM dim_fund
GROUP BY risk_grade;

-- Average 1 Year Return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- Top Alpha Funds
SELECT amfi_code,alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

-- Top Sharpe Ratio
SELECT amfi_code,sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- Transaction Type Distribution
SELECT transaction_type,COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;