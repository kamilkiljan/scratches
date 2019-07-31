import pandas as pd

# 1. Load csv file and view first records


# 2. Create new df with columns City and Sales


# 3. Build summary for each city with avg sales


# 4. Select rows for Gdansk from the df


# 5. Join table from previous exercise with the new_df
data1 = [
    ['Gdansk', 'tom', 2, '7/23/2019'],
    ['Gdansk', 'nick', 3, '7/23/2019'],
    ['Gdansk', 'juli', 5, '7/20/2019']
]
new_df = pd.DataFrame(data1, columns=['City', 'Name', 'Products_bought', 'Date'])

# 6. Create a function called "codes_sales" with two arguments "codes_list" and "data" as input. Function
# should return "report.csv" file containing two columns ('Code' and 'Sales') from "data" only for codes
# specified in the "codes_list". Call "codes_list" function for "codes_list" = "codes.csv" and "data" =
# "data_python_test2.csv" to generate the report. Load csv file (report.csv) and view the records.
