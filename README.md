Customer Churn and Retention Analysis
Tools: Python | Pandas | NumPy | Matplotlib | Seaborn
Project Overview
This project analyses customer churn in a telecommunications company using Python. The objective is to understand customer churn patterns, identify customer segments associated with higher churn, and propose data-driven retention strategies.
Business Objectives
•	Understand the overall customer churn rate.
•	Explore churn patterns across tenure, contract type, payment method, and monthly charges.
•	Examine relationships among numerical customer attributes using a correlation heatmap.
•	Identify customer segments with high observed churn.
•	Recommend potential customer retention strategies.
Dataset
The project uses the IBM Telco Customer Churn dataset, which contains customer demographics, services, contract information, billing details, tenure, and churn status.
The original dataset contains 7,043 records and 21 columns.
Dataset source: Telco Customer Churn on Kaggle
Tools and Libraries
•	Python — analysis and scripting
•	Pandas — data manipulation and cleaning
•	NumPy — numerical operations
•	Matplotlib — data visualization
•	Seaborn — statistical visualization
Project Workflow
1.	Loaded and inspected the dataset.
2.	Checked data types, missing values, and duplicate records.
3.	Converted TotalCharges to numeric using pd.to_numeric().
4.	Removed 11 rows with missing TotalCharges.
5.	Checked and removed duplicate records.
6.	Performed exploratory data analysis (EDA).
7.	Analysed churn by tenure, contract type, payment method, and monthly charges.
8.	Created charts and a correlation heatmap.
9.	Identified a high-churn customer segment.
10.	Developed potential business recommendations.
Data Cleaning
•	Converted TotalCharges to a numeric data type.
•	Coerced invalid or blank values to missing values.
•	Removed rows with missing TotalCharges.
•	Removed duplicate records.
•	Reset the DataFrame index.
Final cleaned dataset: 7,032 rows and 21 columns.
Key Findings
Overall Churn
Metric	Result
Total customers after cleaning	7,032
Churned customers	1,869
Retained customers	5,163
Overall churn rate	26.57%
Tenure
Customer group	Average tenure
Retained customers	37.57 months
Churned customers	17.98 months
Churned customers had substantially shorter average tenure than retained customers, suggesting that early customer engagement and onboarding deserve further investigation.
Contract Type
Contract type	Churn rate
Month-to-month	42.71%
One year	11.27%
Two years	2.83%
Month-to-month customers had the highest observed churn rate.
Payment Method
Payment method	Churn rate
Electronic check	45.29%
Mailed check	19.11%
Bank transfer (automatic)	16.71%
Credit card (automatic)	15.24%
Electronic check customers had the highest observed churn rate. Further investigation is needed to understand whether billing experience, customer characteristics, or other factors are associated with this pattern.
Monthly Charges
Customer group	Average monthly charges
Retained customers	           $61.27
Churned customers	           $74.44
Churned customers had higher average monthly charges. This association does not establish that higher charges cause churn.
Correlation Analysis
Variables	   Correlation
Tenure and TotalCharges	      0.83
MonthlyCharges and TotalCharges	      0.65
Tenure and MonthlyCharges	      0.25
Tenure and TotalCharges had a strong positive correlation. Customers who stay longer generally accumulate higher total charges.
High-Churn Segment
Identified 1,655 churned month-to-month customers, representing 23.54% of all customers in the cleaned dataset.
This is a segment of customers who already churned, not a prediction of future churn.
Visualizations
The analysis includes:
•	Customer churn distribution
•	Customer churn by tenure (boxplot)
•	Customer churn by contract type
•	Customer churn by payment method
•	Customer churn by monthly charges (boxplot and average comparison)
•	Numerical feature correlation heatmap
Business Recommendations
Based on the observed patterns:
1.	Improve early customer engagement: Churned customers had shorter average tenure. Consider onboarding support and early check-ins.
2.	Review month-to-month customer retention: Explore loyalty benefits or long-term contract offers while preserving customer choice.
3.	Investigate electronic check churn: Review billing experience and customer characteristics before changing payment policies.
4.	Review pricing and service bundles: Churned customers had higher average monthly charges. Explore customer feedback and value perceptions.
5.	Monitor churn regularly: Track churn rates by tenure, contract, payment method, and monthly charges over time.
These findings are associations from exploratory analysis, not proof of causation.
Limitations
•	This project uses exploratory analysis and does not build a predictive churn model.
•	Correlation does not imply causation.
•	The high-churn segment contains customers who already churned; it is not a future-risk prediction.
•	Further statistical analysis and customer feedback would be needed to validate potential churn drivers.

