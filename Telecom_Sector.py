

import pandas as pd
import numpy as np
import os
import scipy
import  seaborn as sns
import matplotlib.pyplot as plt


#defining a function to load multiple .csv files
def load_datasets_from_directory(diretory_path):

    dataset = {}

    for filename in os.listdir(diretory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(diretory_path, filename)
            dataset[filename[:-4]] = pd.read_csv(file_path)  #to remove '.csv' used string slicing
    return dataset
diretory_path = 'B:\\Project_Telecom_Industry\\C3 Input_for_Participants'

# to load dataset

dataframe = load_datasets_from_directory(diretory_path)

#merging plan data
merged_plan_data = (dataframe['fact_plan_revenue']
                    .merge(dataframe['dim_plan'],on='plans'))
# Merge fact_atliqo_metrics with dim_date and dim_cities
merged_metrics = (dataframe['fact_atliqo_metrics']
                  .merge(dataframe['dim_date'], on='date')
                  .merge(dataframe['dim_cities'], on='city_code'))
# Merge with fact_market_share and fact_plan_revenue
merged_data = (merged_metrics.merge(dataframe['fact_market_share'], on=['date', 'city_code'])
               .merge(dataframe['fact_plan_revenue'], on=['date', 'city_code']))

final_merged_data = merged_data.merge(merged_plan_data, on=['date', 'city_code', 'plans'])
# Display the merged DataFrame
print("Final merged data", '\n', final_merged_data)

#filtering the data for pre 5G and Post 5G application
# Filter data for pre- and post-5G periods
pre_5g_data = final_merged_data[final_merged_data['before/after_5g'] == 'Before 5G']
post_5g_data = final_merged_data[final_merged_data['before/after_5g'] == 'After 5G']

# Aggregate data for comparison
pre_5g_agg = pre_5g_data.groupby('time_period').agg({
    'atliqo_revenue_crores': 'mean',
    'arpu': 'mean',
    'active_users_lakhs': 'mean',
    'unsubscribed_users_lakhs': 'mean'
}).reset_index()

post_5g_agg = post_5g_data.groupby('time_period').agg({
    'atliqo_revenue_crores': 'mean',
    'arpu': 'mean',
    'active_users_lakhs': 'mean',
    'unsubscribed_users_lakhs': 'mean'
}).reset_index()

# Merge pre- and post-5G aggregated data
comparison_report = pd.merge(pre_5g_agg, post_5g_agg, on='time_period', suffixes=('_pre', '_post'))
print("Comparison report on Average of Pre_5G and Post_5G application data ", '\n', comparison_report)

print(comparison_report.to_string())

# Calculate percentage change in KPIs
comparison_report['Revenue_change_pct'] = ((comparison_report['atliqo_revenue_crores_post'] - comparison_report['atliqo_revenue_crores_pre']) / comparison_report['atliqo_revenue_crores_pre']) * 100
comparison_report['ARPU_change_pct'] = ((comparison_report['arpu_post'] - comparison_report['arpu_pre']) / comparison_report['arpu_pre']) * 100

comparison_report['Active_users_change_pct'] = ((comparison_report['active_users_lakhs_post'] - comparison_report['active_users_lakhs_pre']) / comparison_report['active_users_lakhs_pre']) * 100
comparison_report['Unsubscribed_users_change_pct'] = ((comparison_report['unsubscribed_users_lakhs_post'] - comparison_report['unsubscribed_users_lakhs_pre']) / comparison_report['unsubscribed_users_lakhs_pre']) * 100

# Display the report with percentage changes
print("Report with percentage changes in Metrics","\n", comparison_report[['time_period', 'Revenue_change_pct', 'ARPU_change_pct', 'Active_users_change_pct', 'Unsubscribed_users_change_pct']].to_string())



#for plotting charts
sns.set_theme(style='whitegrid')

### Visualization 1: Revenue Percentage Change ###

plt.figure(figsize=(10, 6))
sns.barplot(x='time_period', y='Revenue_change_pct', hue='time_period', data=comparison_report, palette='Blues', legend=False)
plt.title('Revenue Percentage Change: Pre-5G vs Post-5G', fontsize=16)
plt.xlabel('Time Period', fontsize=12)
plt.ylabel('Percentage Change (%)', fontsize=12)
plt.axhline(0, color='black', linewidth=1, linestyle='--')  # Add a baseline at 0%
plt.show()

### Visualization 2: ARPU Percentage Change (pie chart)###


plt.pie(comparison_report['ARPU_change_pct'], labels=comparison_report['time_period'], autopct='%1.1f%%', startangle=120)
plt.title('ARPU Percentage Change: Pre-5G vs Post-5G', fontsize=16)
plt.xlabel('Time Period', fontsize=12)
plt.ylabel('Percentage Change (%)', fontsize=12)
plt.axhline(0, color='black', linewidth=1, linestyle='')  # Add a baseline at 0% change
plt.show()
### Visualization 3: Active Users Percentage Change ###

plt.figure(figsize=(10, 6))
sns.barplot(x='time_period', y='Active_users_change_pct', hue='time_period', data=comparison_report, palette='Oranges', legend=False)
plt.title('Active Users Percentage Change: Pre-5G vs Post-5G', fontsize=16)
plt.xlabel('Time Period', fontsize=12)
plt.ylabel('Percentage Change (%)', fontsize=12)
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.show()

### Visualization 4: Unsubscribed Users (Churn) Percentage Change ###

plt.figure(figsize=(10, 6))
sns.barplot(x='time_period', y='Unsubscribed_users_change_pct', hue='time_period', data=comparison_report, palette='Reds', legend=False)
plt.title('Unsubscribed Users (Churn) Percentage Change: Pre-5G vs Post-5G', fontsize=16)
plt.xlabel('Time Period', fontsize=12)
plt.ylabel('Percentage Change (%)', fontsize=12)
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.show()

#to import data to excel for performing visuals in power bi
comparison_report.to_excel('comparison_report.xlsx', index=False)


