
# AtliQo 5G Impact Analysis

## Overview
This project analyzes the impact of the **5G launch** on AtliQo's key performance indicators (KPIs) by comparing metrics before and after the launch. The analysis focuses on revenue, average revenue per user (ARPU), active users, and churn rates, providing insights for informed decision-making.

## Table of Contents
- [Key Outcomes](#key-outcomes)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Visualizations](#visualizations)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Key Outcomes
- **Data Acquisition and Preparation**: 
  - Loaded and cleaned multiple datasets from various CSV files.
  - Merged datasets to create a comprehensive view of AtliQo's performance.

- **Comparative Analysis**: 
  - Segmented data into pre-5G and post-5G periods.
  - Aggregated metrics to create a comparison report.

- **Key Performance Indicators**:
  - **Revenue Change**: Analyzed revenue growth trends post-5G launch.
  - **ARPU Analysis**: Investigated changes in ARPU.
  - **Active User Trends**: Compared the number of active users before and after the launch.
  - **Churn Rate Examination**: Evaluated the increase in unsubscribed users.

- **Insights and Recommendations**:
  - Identified factors leading to the decline in active users and revenue post-5G.
  - Suggested optimizing internet plans based on user feedback.

## Data Sources
The datasets used in this analysis include:
- `dim_cities.csv`: Contains information about cities.
- `dim_date.csv`: Contains information about the dates.
- `dim_plan.csv`: Contains details about the various internet plans.
- `fact_atliqo_metrics.csv`: Contains monthly metrics for AtliQo.
- `fact_market_share.csv`: Contains market share data.
- `fact_plan_revenue.csv`: Contains revenue data from different plans.

## Methodology
1. **Data Loading**: Used Python's `pandas` library to load datasets from CSV files.
2. **Data Merging**: Combined datasets from different dimensions to enrich the analysis.
3. **Segmentation**: Filtered data into pre-5G and post-5G segments for comparison.
4. **Aggregation**: Calculated mean values for key metrics (revenue, ARPU, active users) using `groupby()`.
5. **Visualization**: Created visualizations using `Matplotlib` and `Seaborn` to illustrate findings.

## Visualizations
The following visualizations were created to support the analysis:
- **Revenue Comparison**: Bar charts comparing revenue changes before and after the 5G launch.
- **ARPU Analysis**: Line charts showing ARPU trends over time.
- **Active Users Change**: Bar charts visualizing changes in active user counts.
- **Churn Rate Analysis**: Charts illustrating the changes in unsubscribed users.



## Installation
To run this project, ensure you have Python installed along with the required libraries. You can install the necessary packages using:

```bash
pip install -r requirements.txt
