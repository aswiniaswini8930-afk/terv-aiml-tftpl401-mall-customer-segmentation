
# Shopping Mall Customer Segmentation

## 1. Project Overview
This project uses K-Means Clustering to divide shopping mall
customers into groups based on their age, income, spending
score, shopping visits, monthly spending, and membership tenure.

## 2. Dataset
- Original customers: 4,792
- Customers used after cleaning: 4,681
- Features used: 6

## 3. Methodology
1. Data cleaning
2. Exploratory Data Analysis (EDA)
3. Feature engineering
4. Feature scaling
5. K-Means clustering
6. Model evaluation
7. PCA visualization
8. Customer profiling

## 4. Model Results
- Algorithm: K-Means
- Selected clusters: 3
- Silhouette Score: 0.2075
- PCA variance explained: 58.67%

## 5. Customer Segments

| Cluster | Customers | Customer Type |
|---|---:|---|
| 0 | 1,010 | Premium High-Spending Customers |
| 1 | 2,100 | Young Frequent Shoppers |
| 2 | 1,571 | Budget-Conscious Occasional Shoppers |

## 6. Five Key Insights

1. Cluster 0 has the highest average monthly spending
   at approximately Rs. 36,554.

2. Cluster 1 is the largest customer group, with
   2,100 customers.

3. Cluster 1 visits the mall most frequently,
   averaging 8.08 visits per month.

4. Cluster 2 has the lowest average monthly spending,
   approximately Rs. 7,974.

5. Cluster 0 has the highest average annual income,
   approximately Rs. 16.78 lakh.

## 7. Three Business Recommendations

1. Offer VIP rewards and premium services to Cluster 0.

2. Provide loyalty points, seasonal offers, and
   shopping rewards to Cluster 1.

3. Offer discounts, combo deals, and value packages
   to Cluster 2.

## 8. Project Limitations
The Silhouette Score is approximately 0.2075,
indicating that some customer groups overlap.
The clustering results should be interpreted with care.

## 9. Project Deliverables
- Executed Jupyter/Colab notebook
- Charts in outputs/figures/
- metrics.csv and summary.json in outputs/reports/
- Trained model and scaler in models/
- README.md
