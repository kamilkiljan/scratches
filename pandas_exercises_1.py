import pandas as pd

# 1. Load csv file and view first records
df = pd.read_csv('data_python_test.csv')
print(df.head())

# 2. Create new df with columns City and Sales
cs_df = df.loc[:, ['City', 'Sales']]

# 3. Build summary for each city and get avg sales
summary_df = df.groupby('City').sum()
summary_df['Avg_sale'] = summary_df['Sales'] / summary_df['No_products_sold']

# 4. Select rows for Gdansk from the df
df_gdansk = df.loc[df['City'] == 'Gdansk']

# 5. Join table from previous exercise with the new_df
data1 = [
    ['Gdansk', 'tom', 2, '7/23/2019'],
    ['Gdansk', 'nick', 3, '7/23/2019'],
    ['Gdansk', 'juli', 5, '7/20/2019']
]
new_df = pd.DataFrame(data1, columns=['City', 'Name', 'Products_bought', 'Date'])
joined_df = pd.merge(df_gdansk, new_df, on=['Date', 'City'], how='outer')


# 6. Create a function called "codes_sales" with two arguments "codes_list" and "data" as input. Function
# should return "report.csv" file containing two columns ('Code' and 'Sales') from "data" only for codes
# specified in the "codes_list". Call "codes_list" function for "codes_list" = "codes.csv" and "data" =
# "data_python_test2.csv" to generate the report. Load csv file (report.csv) and view the records.
def codes_sales(codes_list, data):
    codes_series, data_df = pd.read_csv(codes_list).iloc[:, 0], pd.read_csv(data)
    new_df = data_df.loc[data_df['Code'].isin(codes_series)].loc[:, ['Country', 'Sales']]
    new_df.to_csv('report.csv', index=False)
    return


codes_sales(codes_list='codes.csv', data='data_python_test2.csv')
codes_sales_df = pd.read_csv('report.csv')
print(codes_sales_df.to_string())
