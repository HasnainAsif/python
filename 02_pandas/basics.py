# # Numpy array only allows rows with same data types but pandas dataframe allow different data types.
# # Pandas help us to work with tabular data
# # pandas is built on top on numpy and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from data_variables import avocados, cars_df, test_df, cars, sales, taxi_owners, taxi_vehicle, jpm, wells, tracks_master, tracks_ride, tracks_st, inflation
############################## --> Creating DataFrame and Series
# ### Create a Series
# s = pd.Series([1, 2, 3, 4, 5])
# print(s) 

# ### Create a Series with custom index
# s = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
# print(s)
# print(s['a'])

# ### Create index of dates (DateTimeIndex)
# dates = pd.date_range("2013-01-01", periods=6) # Create a date range with 6 dates starting from 2013-01-01
# # dates = pd.date_range("20130101", periods=6) # same result as above
# print(dates)

# ### Create dataframe of random numbers
# dates = pd.date_range("2013-01-01", periods=6) # Create a date range with 6 dates starting from 2013-01-01
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["A", "B", "C", "D"]) # Create a DataFrame with 6 rows and 4 columns with random numbers
# # df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD")) # same result as above
# print(df)

# ### Create dataframe from List of dictionaries
# print(avocados)

# ### Create dataframe from dictionary of lists
# print(cars_df) 
# row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG'] # Definition of row_labels
# cars_df.index = row_labels # Specify row labels of cars
# print(cars_df)

# # another example
# print(test_df) # Create a DataFrame from a dictionary of lists

# ### Importing Data from a CSV
# cars = pd.read_csv('/home/tk-lpt-648/my-work/Personal/Projects/python/00_datasets/cars.csv')
# print(cars)

# cars = pd.read_csv('/home/tk-lpt-648/my-work/Personal/Projects/python/00_datasets/cars.csv', index_col=0) # set 1st column as index column
# print(cars)

# updated_dtypes = { "who": "category", "class": "category", "sex": "category" } # dictionary to change data types
# titanic = pd.read_csv('/home/tk-lpt-648/my-work/Personal/Projects/python/00_datasets/titanic.csv', dtype=updated_dtypes) # Update dtypes while importing csv
# print(titanic.dtypes)

# ### Create a CSV from DataFrame
# avocados.to_csv("./pandas/test_avocados.csv")

############################## --> DataFrame methods and attributes
# ## Inspecting a dataframe
# print("HEAD 5: \n", cars.head()) # returns the first few rows (the “head” of the DataFrame).
# print("HEAD 10: \n", cars.head(10)) # returns the first 10 rows
# print("TAIL 5: \n", cars.tail()) # returns the last few rows (the “tail” of the DataFrame).
# cars.info() # shows information on each of the columns, such as the data type and number of missing values.
# print("SHAPE: ", cars.shape) # returns the number of rows and columns of the DataFrame.
# print("DESCRIBE: \n", cars.describe()) # calculates a few summary statistics on numeric columns for each column.
# print("Data Type: \n", cars.dtypes) # returns the data type of each column in the DataFrame.
# print("Numpy Conversion: \n", cars.to_numpy()) # returns a NumPy array representation of the DataFrame.
# print("transpose: \n", cars.T) # returns the transpose of the DataFrame, swapping rows and columns.
# print(cars.rename(columns=({"drives_right": "is_drives_right"}))) # rename column names
# copied_cars = cars.copy() # returns a copy of the DataFrame. This is useful if you want to modify the DataFrame without changing the original one.

## Components of a dataframe
# print(cars.values) # A two-dimensional NumPy array of values.
# print(cars.columns) # An index of columns: the column names.
# print(cars.index) # An index for the rows: either row numbers or row names/labels.

############# Shuffle rows of complete dataset
# shuffled_cars = cars.sample(frac=1) # frac is percentage of data to pick. frac=1 means 100%
# print(shuffled_cars)

############# Sort by column values
### Sorting on a dataframe
# cars_sorted = cars.sort_values("cars_per_cap") # Sort cars by cars_per_cap in ascending order
# print(cars_sorted.head()) # Print the top few rows

# cars_sorted_by_country = cars.sort_values(by="country", ascending=False) # sort by descending order
# print(cars_sorted_by_country)

# cars_multi_columns_sorting = cars.sort_values(["cars_per_cap", "country"], ascending=[True, False])
# print(cars_multi_columns_sorting.head()) # Print the top few rows

# ### Sorting series
# descSorted = cars['cars_per_cap'].sort_values(ascending=False)
# print(descSorted)
# print(descSorted.index)
# print(cars.loc[descSorted.index]) # Reorder the cars DataFrame based on 'cars_per_cap' column in descending order

############# Sort by index
# print(cars.sort_index(axis=0, ascending=True)) # Sort by index in descending order for rows
# print(cars.sort_index(axis=1, ascending=False)) # Sort by index in descending order for columns

############################## --> MISSING VALUES
### Check Missing Values
# print(avocados.isna()) # returns true in dataframe where value is NAN otherwise it returns false
# print(avocados.isnull()) # return same result as above
# print(avocados.isna().any()) # returns true for column, if any value is missing in that column; otherwise it returns false
# print(avocados.isna().sum()) # returns count of missing values for each column
# avocados.isna().sum().plot(kind='bar')
# plt.show() # # Show plot

# ### Remove Missing Values
# avocados_complete = avocados.dropna() # remove row from data frame, if any value in that row is missing
# print(avocados_complete.isna().any()) # check if any column contains missing values
# avocados.info()

# ### Fill 0 into Missing values
# cols_with_missing_values = ["avg_price", "nb_sold"]
# print(avocados[cols_with_missing_values])
# avocados[cols_with_missing_values].hist()
# plt.show()

# avocados_filled = avocados.fillna(0) # fill missing values with 0
# avocados_filled[cols_with_missing_values].hist()
# plt.show()


############################## --> Subsetting rows and columns - Selecting rows and columns
# print(cars['country']) # returns pandas series
# print(cars[['country']]) # return country column. Double array returns pandas dataframe
# print(cars[['country', 'drives_right']]) # returns country and drives_right columns

# print(cars[1:3]) # return rows at index 1 and 2

##### Selecting Data with "loc and iloc"
# loc is label-based - it checks index column
# iloc is integer index based

# returns series.
# print(cars.loc['JPN']) # return "JPN" labeled rows - where cars' index is JPN
# print(cars.iloc[2]) # return row at index 2

# returns dataframe.
# print(cars.loc[['JPN', 'AUS']]) # return "JPN" and "AUS" labeled rows
# print(cars.iloc[[2, 1]]) # return rows at index 2 and 1
# print(cars.iloc[0:3]) # return rows at 0,1,2 index

# return series
# print(cars.loc[['JPN'], 'drives_right']) # return row of "JPN" label with only drives_right column
# print(cars.iloc[[2], 2]) # return row of index 2 and only column at index 2

# returns dataframe
# print(cars.loc[['JPN', 'AUS'], ['country', 'drives_right']]) # returns "JPN" and "AUS" labeled rows with country and drives_right column
# print(cars.iloc[[2, 1], [1, 2]]) # return rows at index 2 and 1 and columns at index 1 and 2

# returns drives_right column as Series
# print(cars.loc[:, 'drives_right']) # return series. return all rows with column drives_right
# print(cars.iloc[:, 1]) # return series. return all rows with column at index 1

# returns drives_right column as DataFrame
# print(cars.loc[:, ['cars_per_cap','drives_right']]) # return all rows with column cars_per_cap and drives_right
# print(cars.iloc[:, [2, 1]]) # return all rows with column at index 1 and 2

# returns only single value
# print(cars.loc['JPN', 'drives_right']) # Print only, the value of the "drives_right" column for the row labeled "JPN"
# print(cars.iloc[2, 1]) # Print only, the value of the "drives_right" column for the row at index 2
# print(cars.at['JPN', 'drives_right']) # Print only, the value of the "drives_right" column for the row labeled "JPN" - at is faster than loc

# Select data at a specific row and column
# print(cars.iloc[2, 1]) # return value at row index 2 and column index 1


################ SUBSETTING ROWS - Select Data based on boolean conditions
# dr = cars['drives_right'] # Extract drives_right column as Series
# print(dr)
# sel = cars[dr] # return only those cars where drives_right is true
# # sel = cars[dr == True] # same as above
# print(sel)

###
# cpc = cars['cars_per_cap'] # Extract cars_per_cap column as Series
# cpc_gt_50 = cars[cpc > 50] # return cars where cpc > 50
# print(cpc_gt_50)

###
# cpc = cars['cars_per_cap'] # Extract cars_per_cap column as Series
# cpc_eq_18 = cars[cpc == 18] # return cars where cpc == 18
# print(cpc_eq_18)

### 
# inflationNew = inflation.loc[:, [2017, 2018, 2019]]
# print(inflationNew[inflationNew > 2]) # return inflation where inflation is greater than 2 - Note: all cells data should be numeric

# #### and operator
# cpc = cars['cars_per_cap'] # Extract cars_per_cap column as Series
# drives_right = cars['drives_right'] # Extract drives_right column as Series
# condition = (cpc > 50) & (drives_right == True)
# result = cars[condition]
# print(result)

# cpc = cars['cars_per_cap'] # Extract cars_per_cap column as Series
# between = np.logical_and(cpc >= 50, cpc <= 500) # return true where cpc >= 50 and cpc <= 500
# medium = cars[between]
# print(medium)

# #### or operator
###
# cars_country = cars['country'] # Extract country column as Series
# cars_condition = (cars_country == 'India') | (cars_country == 'Egypt') | (cars_country == 'Japan')
# print(cars[cars_condition])

### return same result as above
# checkable_countries = ['India', 'Egypt', 'Japan']
# cars_country = cars['country'] # Extract country column as Series
# cars_condition = cars_country.isin(checkable_countries)
# print(cars[cars_condition])

# ######## SELECTING ROWS WITH QUERY
# # its similar to sql queries -- query arguments are similar to sql after where clause
# print(avocados.query('nb_sold < 1000 & avg_price <= 1 & (type == "organic" | type == "conventional")'))


############################## --> LOOPS
# # Iterate over rows of cars
# for label, row in cars.iterrows():
#     print(label, "\n", row, "\n") # row is a series
#     # print(f"{label}: {row['cars_per_cap']}") # get only cars_per_cap

############################## --> Add new column to dataframe
# # Add a new column to cars table
# for label, row in cars.iterrows() :
#     cars.loc[label, "COUNTRY"] = row["country"].upper() # adds COUNTRY column
#     cars.loc[label, "country_length"] = len(row["country"])# adds country length column
# print(cars)

# # It will return same result as above but more efficient
# cars["COUNTRY"] = cars["country"].apply(str.upper) # applying a method
# cars["countries_concatenated"] = cars["country"] + cars["COUNTRY"]
# cars["country_length"] = cars["country"].apply(len) # applying a function
# print(cars)

# # Performed Arithematic operation
# # cars["cars_per_cap_divided"] = cars["cars_per_cap"] / 100 # operators could be applied same as numpy array on a series
# cars["cars_per_cap_arithmatic_op"] = cars["cars_per_cap"] / cars['fuel_price'] * 2
# print(cars)

# # Concatenated Column
# cars["COUNTRY"] = cars["country"].apply(str.upper) # applying a method
# cars["concatenated_column"] = cars["country"] + ' ' + cars["COUNTRY"]
# print(cars)

##################################################################################

############################## --> Summary Statistics
# print(cars["cars_per_cap"].mean()) # Mean of cars_per_cap
# print(cars['cars_per_cap'].median()) # Median of cars_per_cap

# print(cars['date'].max()) # Print the maximum of the date column
# print(cars['date'].min()) # Print the minimum of the date column

# ### The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions to more than one column of a DataFrame at once, making your aggregations super-efficient.
# # A custom IQR(Inter quantile range) function
# def iqr(column):
#     # If total no. of values are 8. (0+8)/2=4.5th value is 50th percentile(50% quantile)(median), (0+4.5)/2=2.25th value is 25% quantile and (4.5+8)/2=6.25th value is 75th quantile
#     return column.quantile(0.75) - column.quantile(0.25) # IQR is the difference between 75th percentile and 25th percentile
# # Print IQR of the cars_per_cap column

# # print(cars['cars_per_cap'].sort_values(ascending=True).values) # Sort cars_per_cap in ASC order
# print("1 column: ",cars['cars_per_cap'].agg(iqr)) # Find iqr of one column
# print("2 columns: \n", cars[['cars_per_cap', 'fuel_price']].agg(iqr)) # Find iqr of 2 columns
# print("2 columns, 2 functions: \n", cars[['cars_per_cap', 'fuel_price']].agg([iqr, np.median])) # Find iqr and median of 2 columns

## Cummulative Statistics
# # Cummulative Sum -- Each incoming row value, will add previous row value. 1st row value will be same, last row value will be sum of all values
# cars["cum_sum"] = cars["fuel_price"].cumsum()
# print(cars)

# # Cummulative Maximum - The cummax() method goes through the values in the DataFrame, from the top, row by row, replacing the values with the highest value yet for each column, ending up with a DataFrame where the last row contains only the highest value from each column.
# cars["cum_max"] = cars["fuel_price"].cummax()
# print(cars)

# Other cummulative methods are cummin(), cumprod()

## drop_duplicates
# cars_unique_per_date = cars.drop_duplicates(subset="date")
# print(cars_unique_per_date)

## Remove duplicate pairs of date and cars_per_cap
# cars_unique_per_cap_and_date = cars.drop_duplicates(subset=["date", "cars_per_cap"]) # Let's say we have a person table. Multi values can be used to get unique values with combination of first name and last name columns
# print(cars_unique_per_cap_and_date.head())

## Count
# cars_count_as_per_date = cars['date'].value_counts() # its like grouping with date and count values (SQL)
# # cars_count_as_per_date = cars['date'].value_counts(sort=True) # Sort count in descending
# print(cars_count_as_per_date)

## Get Proportion
# cars_count_as_per_date_proportion = cars['date'].value_counts(normalize=True) # it like grouping with date. And how much percentage each date contains from 100%. In other words, how much proportion each value contains
# # cars_count_as_per_date_proportion = cars['date'].value_counts(sort=True, normalize=True) # Sort proportion on descending
# print(cars_count_as_per_date_proportion)


########################### --> Group Statistics
# print(sales)

# ### Start
# sales_all = sales["weekly_sales"].sum() # Calc total weekly sales
# # print(sales_all)
# type_A_store_sales = sales[sales["type"] == "A"] # Subset for type A stores
# sales_A = type_A_store_sales["weekly_sales"].sum() # Calc total weekly sale of type a store
# # print(sales_A)
# sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum() # Subset for type B stores, calc total weekly sales
# sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum() # Subset for type C stores, calc total weekly sales
# sales_D = sales[sales["type"] == "D"]["weekly_sales"].sum() # Subset for type D stores, calc total weekly sales

# ## Get proportion for each type - how much sales portion each type contains
# sales_propn_by_type = [sales_A, sales_B, sales_C, sales_D] / sales_all
# print(sales_propn_by_type)

################## Groupby -- it return series -- Shorter form of above solution
##### Group by type; calc total weekly sales
# sales_by_type = sales.groupby("type")["weekly_sales"].sum() # it works same as sql groupby
# # sales_by_type = sales.groupby("type")["weekly_sales"].agg('sum') # same result as above
# print(sales_by_type) # return series
# print(sales_by_type.sort_values(ascending=False)) # sorting on sales_by_type series
# total_sales = sum(sales_by_type)
# # sales["weekly_sales"].sum() # it will return same result as above

# # Get proportion for each type
# sales_propn_by_type = sales_by_type / total_sales
# print("PROPORTION: \n",sales_propn_by_type)

### Another way to groupby
# sales_by_type = sales.groupby("type").agg({'weekly_sales': 'sum'}) # group sales by type, and sum all weekly_sales
# print(sales_by_type) # return DF
# print(sales_by_type.sort_values('weekly_sales', ascending=True)) # apply sorting on weekly_sales column

### End

# # Group by type and is_holiday; calc total weekly sales
# sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
# print(sales_by_type_is_holiday)

# # For each store type, aggregate weekly_sales: get min, max, mean, and median
# sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median]) # mix,max,mean,median methods could also be applied separately like "sales.groupby('type')['weekly_sales'].min()"
# print(sales_stats)

# # For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
# unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg([np.min, np.max, np.mean, np.median])
# print(unemp_fuel_stats)

###### PIVOT TABLE - the .pivot_table() method is an alternative to .groupby()
# # Pivot for mean weekly_sales for each store type - groupby sales data with type and take mean of weekly_sales column
# mean_median_sales_by_type = sales.pivot_table(index='type', values='weekly_sales') # by default pivot_table method calculate mean
# print(mean_median_sales_by_type)

# # Pivot for mean and median weekly_sales for each store type
# mean_sales_by_type = sales.pivot_table(index='type', values='weekly_sales', aggfunc=['mean', 'median'])
# print(mean_sales_by_type)

# # Pivot for mean weekly_sales and is_holiday for each store type
# mean_sales_by_type_holiday = sales.pivot_table(index='type', columns='is_holiday', values='weekly_sales', aggfunc=['mean', 'median']) # groupby type and is_holiday -- if we wanna group by two variables, 2nd variable will be passed into columns argument. index is represented as row and columns is represented as column
# print(mean_sales_by_type_holiday)

# # Print mean weekly_sales by department and type; fill missing values with 0
# print(sales.pivot_table(index='department', columns='type', values='weekly_sales', fill_value=0)) # by default pivot_table method calculate mean
# # print(sales.groupby(["department", "type"])["weekly_sales"].mean()) # above result with groupby which return series instead of pivot table

# # Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
# print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True)) # margins argument is used to sum all rows and columns

################################### INDEXING and SUBSETTING on a Data Frame - index have no need to be unique
# sales_indexed = sales.set_index('store') # set index of sales to store
# # print(sales_indexed)
# # print(sales_indexed.reset_index()) # Reset the sales_indexed index, keeping its contents - store index is shifted to column
# # print(sales_indexed.reset_index(drop=True)) # Reset the sales_indexed index, dropping its contents - store index is removed

# print(sales[sales['store'].isin([1, 2])]) # return sales, where store is 1 or 2
# print(sales_indexed.loc[[1, 2]]) # loc checks index column. it will return sales_indexed where store is 1 or 2 -- same result as above, only difference is that; here store column is an index column

# ## Multi level or hierarchical index
# sales_indexed = sales.set_index(['type', 'store']) # set index of sales to type and store
# print(sales_indexed)
# print(sales_indexed.loc[['B', 'A']]) # Subset the outer level i.e; as per type
# print(sales_indexed.loc[[('B', 1), ('A', 3)]]) # Subset the inner level i.e; as per type and store

# ## Sorting with index
# print(sales_indexed.sort_index()) # Sort by index values - by default it sort as per outer level. In our case, its "type"
# print(sales_indexed.sort_index(level='store', ascending=True)) # Sort by index values at the type level - default value of ascending is True(means no need to pass it here)
# print(sales_indexed.sort_index(level=['store', 'type'], ascending=[True, False])) # Sort by store ascending and type descending

# ## Slicing with index values - for slicing on index, index must be sorted
# sales_sorted = sales_indexed.sort_index()
# print(sales_sorted.loc['B' : 'D']) # Slice rows from B to D as per outer level(type)
# print(sales_sorted.loc[('B', 2) : ('D', 2)]) # Slice rows from "type B and store 2" to "type D and store 2" as per outer and inner level

# print(sales_sorted.loc[:, "date" : "is_holiday"]) # return all rows and slice columns from date to is_holiday
# print(sales_sorted.loc[('B', 2) : ('D', 2), "date" : "is_holiday"]) # slicing by rows and columns at once

# sales_ind = sales.set_index('date').sort_index()
# print(sales_ind.loc['2010': '2011']) # subset sales for rows in 2010 and 2011 -- If date is in ISO-8601 format(YYYY-MM-DD), we can filter result with only YYYY or YYYY-MM or YYYY-MM-DD
# print(sales[(sales['date'] >= '2010-01-01') & (sales['date'] <= '2011-12-31')]) # -- above result can also be achieved withour indexes

# print(sales.iloc[1, 4]) # return row at index 1 and col at index 2
# print(sales.iloc[:5]) # return 1st 5 rows
# print(sales.iloc[: ,2:5]) # return all rows and colmns 3rd to 5th, means index from 2 to 4
# print(sales.iloc[0:5 ,2:5]) # return 1st 5 rows and colmns 3rd to 5th, means index from 2 to 4

##### Subsetting on pivot table
# # Add a year column to temperatures
# sales['year'] = sales['date'].dt.year

# # Pivot weekly_sales by store and type vs year. # instead of passing values argument, weekly_sales can be passed directly as 1st argument
# # default aggregate function is mean
# weeklysales_by_store_type_vs_year = sales.pivot_table("weekly_sales", index=["type", "store"], columns="year") # it will make type and store as index and years will be column
# # weeklysales_by_store_type_vs_year = sales.pivot_table(values="weekly_sales", index=["type", "store"], columns="year") # same result as above
# print(weeklysales_by_store_type_vs_year)

# print(weeklysales_by_store_type_vs_year.loc['B' : 'D']) # return subset from type  B to D
# print(weeklysales_by_store_type_vs_year.loc[('B', 1) : ('D', 2)]) # return subset from "type B, store 1" to "type D, store 2"
# print(weeklysales_by_store_type_vs_year.loc[('B', 1) : ('D', 2), "2011": "2012"]) # return subset from "type B, store 1" to "type D, store 2" and year columns from 2011 to 2012

### Some Questions:
# # Get the mean sales by year column
# mean_sales_by_year = weeklysales_by_store_type_vs_year.mean() # Sum all the row values from each column and take average
# # mean_sales_by_year = weeklysales_by_store_type_vs_year.mean(axis='rows') 
# print(mean_sales_by_year)
# print(mean_sales_by_year[mean_sales_by_year == mean_sales_by_year.max()]) # Filter for the year that had the highest mean sale

# # Get the mean sales by type and store index
# mean_sales_by_type_store = weeklysales_by_store_type_vs_year.mean(axis='columns') # mean is calculated across columns. means; sum all the column values from each row and take average
# # print(weeklysales_by_store_type_vs_year)
# print(mean_sales_by_type_store)
# # # Filter for the "type and store" that had the lowest mean sales
# print(mean_sales_by_type_store[mean_sales_by_type_store == mean_sales_by_type_store.min()])

###################################### --> MERGING TABLES HORIZONTALLY
# Merge the taxi_owners and taxi_vehicle tables setting a suffix

########### INNER JOIN - only return matched rows
# # taxi_own_veh = taxi_owners.merge(taxi_vehicle, on='vid') # join on column vid, which is same on both tables # columns with same name will get suffix "x" for taxi_owners table and "y" for taxi_vehicle table
# # taxi_own_veh = taxi_owners.merge(taxi_vehicle, left_on='vid', right_on='vid') # For joining data pick vid from left table and also vid from 2nd table - for same column names we could also use on="vid"
# taxi_own_veh = taxi_owners.merge(taxi_vehicle, on='vid', suffixes=('_own','_veh')) # columns with same name will get suffix "_own" for taxi_owners table and "_veh" for taxi_vehicle table?
# print(taxi_own_veh)
# print(taxi_own_veh.columns)
# print(taxi_own_veh.shape)

### Validate inner join
# duplicate_first_row=taxi_vehicle.iloc[0] # get first row as series
# taxi_vehicle.loc[len(taxi_vehicle)] = duplicate_first_row # inserting taxi_vehicle first row again at the end, to get duplicated vid
# # validate a merge if one_to_one relation is applicable or not. means, check if there is any duplicated row in taxi_vehicle. If there is, then it means inner join is not applicable here. Either remove duplicated row or use one_to_many relation
# taxi_own_veh = taxi_owners.merge(taxi_vehicle, on='vid', how='left', validate='one_to_one') # default value of validate is None
# print(taxi_own_veh)

###
# # Print the value_counts to find the most popular fuel_type
# print(taxi_own_veh['fuel_type'].value_counts()) # groupby fuel and count values
# # print(taxi_own_veh['fuel_type'].value_counts().sort_values()) # sort above data by ascending

# ## Filter result
# filter_criteris = (taxi_own_veh['make'].isin(['TOYOTA', 'NISSAN'])) & (taxi_own_veh['fuel_type'] == 'GASOLINE')
# print(taxi_own_veh[filter_criteris][['owner_own', 'address', 'make', 'fuel_type']]) # Getting random result for practice
# print(taxi_own_veh[filter_criteris].value_counts('make')) # Getting random result for practice
# print(taxi_own_veh.loc[filter_criteris].value_counts('make')) # same result as above

# ### Merging Multiple tables
# taxi_own_veh = taxi_owners.merge(taxi_vehicle, on='vid').merge(another_table, on='aid', suffixes=('_taxiown','_ano')) # Merging multiple tables
# # taxi_own_veh = taxi_owners.merge(taxi_vehicle, on='vid') \
# #                         .merge(another_table, on='aid', suffixes=('_taxiown','_ano')) # above could also be written as this way

########### LEFT JOIN / RIGHT JOIN / OUTER JOIN
# #### LEFT JOIN - return all rows from left table, and only those rows from right table which matched with left table
# taxi_own_veh = taxi_owners.merge(taxi_vehicle, on='vid', how='left') # how mentions join type.
# print(taxi_own_veh.head())
# print(taxi_own_veh.shape)
# print(taxi_own_veh['make'].isna().sum()) # count taxi_own_veh where make is null

# taxi_own_veh_with_indicator = taxi_owners.merge(taxi_vehicle, on='vid', how='left', indicator=True) # indicator add a new column(_merge) and return value if a row is merged of both tables or is only exist in left table
# print(taxi_own_veh_with_indicator)

# #### Right JOIN - return all rows from right table, and only those rows from left table which matched with right table
# taxi_own_veh = taxi_owners.merge(taxi_vehicle, on='vid', how='right') #
# print(taxi_own_veh.shape)

# #### OUTER JOIN - return all rows from left and right table even if they match or not
# taxi_own_veh = taxi_owners.merge(taxi_vehicle, on='vid', how='outer', suffixes=('_1', '_2')) #
# print(taxi_own_veh.shape)

# # All rows from left and right tables except whose vid is matched
# print(taxi_own_veh)
# m = ((taxi_own_veh['owner_1'].isnull()) | 
#      (taxi_own_veh['owner_2'].isnull())) # Create a filter that returns true if owner_1 or owner_2 are null
# print(taxi_own_veh[m].head())

#### SELF JOIN
# # Merge the taxi_owners table to itself using inner/left/right/outer joins
# taxi_owners_self_merged = taxi_owners.merge(taxi_owners, on='vid', how='inner',
#                                 suffixes=('_1','_2'))
# print(taxi_owners_self_merged)

#### JOINS USING INDEX
# # Joins with single Index
# taxi_owners_indexed = taxi_owners.set_index('zip')
# taxi_vehicle_indexed = taxi_vehicle.set_index('zip')
# self_joined_indexed_single = taxi_owners_indexed.merge(taxi_vehicle_indexed, on='zip', how='inner')
# print(self_joined_indexed_single)

# # MultiIndex merge
# taxi_owners_multi_indexed = taxi_owners.set_index(['vid', 'zip'])
# taxi_vehicle_multi_indexed = taxi_vehicle.set_index(['vid', 'zip'])
# merged = taxi_owners_multi_indexed.merge(taxi_vehicle_multi_indexed, on=['vid','zip']) # it will match both columns vid and zip
# # merged = taxi_owners_multi_indexed.merge(taxi_vehicle_multi_indexed, left_index=True, right_index=True) # same result as above. - Use left indexed column and right indexed column
# print(merged)
# print(merged.shape)

# # Index merge another example - use index column from left table and zipp column from right table
# taxi_owners_indexed = taxi_owners.set_index(['zip']) 
# merged = taxi_owners_indexed.merge(taxi_vehicle, how='inner', left_index=True, right_on='zipp')
# print(merged)

########## MERGE ORDERED
# # it merges and order data ascendingly as per vid
# ordered_merge = pd.merge_ordered(taxi_owners, taxi_vehicle, left_on='vid', right_on='vid', how='left') # default value of how is outer
# ordered_merge_filled = pd.merge_ordered(taxi_owners, taxi_vehicle, left_on='vid', right_on='vid', how='left', fill_method='ffill') # fill_method -> forward fill missing values - means if a value in a row is NaN, get value from previous row and put it into next row which is NaN.
# print(ordered_merge)
# print(ordered_merge_filled)


########## MERGE asof
# Match on the nearest key column and not exact matches.
# Merged "on" columns must be sorted.
# its mostly used for timestamps where time do not exactly match in left and right table. but there is slight difference of minutes or seconds 
# it provides us left join

# jpm_wells = pd.merge_asof(jpm, wells, on='date_time', suffixes=('', '_wells')) # by default direction is backward; which matches date_time value from left table, where right table date_time value is equal to or less than to left table date_time value
# # jpm_wells = pd.merge_asof(jpm, wells, on='date_time', suffixes=('', '_wells'), direction='forward') # which matches date_time value from left table, where right table date_time value is equal to or greater than to left table date_time value
# # jpm_wells = pd.merge_asof(jpm, wells, on='date_time', suffixes=('', '_wells'), direction='nearest') # which matches date_time value from left table, where right table date_time value is equal to or less than or greater than to left table date_time value
# print(jpm_wells)

###################################### --> MERGING TABLES VERTICALLY
# ### Concatenate the tracks so the index goes from 0 to n-1
# tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
#                                ignore_index=True, # ignore_index will ignore columns separate indexes and will start index from 0 to n-1
#                                sort=True) # it sort columns in ascending order
# print(tracks_from_albums)

# # Concatenate the tracks, show only columns names that are in all tables
# tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
#                                join='inner', # by default join is outer, which shows all columns. join "inner", only shows matched columns from all tables
#                                )
# print(tracks_from_albums)

# ### Verify Concatination - if there is no duplicated row as per index. Means index from all dataframes should be unique
# tracks_master_indexed=tracks_master.set_index('tid')
# tracks_ride_indexed=tracks_ride.set_index('tid')
# tracks_st_indexed=tracks_st.set_index('tid')

# tracks_ride_indexed_first_row = tracks_ride_indexed.iloc[0] # get 1st row as series
# tracks_st_indexed.loc[1874] = tracks_ride_indexed_first_row # 1st row from tracks_ride_indexed is added into tracks_st_indexed with index 1874. This index is now same in both data frames. (We are doing this, So that we could have a same index on both data frames)

# tracks_from_albums = pd.concat([tracks_master_indexed, tracks_ride_indexed, tracks_st_indexed], verify_integrity=True) # it will throw error, because one index from tracks_ride_indexed and tracks_st_indexed is same. To allow same index, verify_integrity should be false
# print(tracks_from_albums)

# ### Adding keys to grouped rows. Then, Group data based on rows and plot a bar chart
# tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],join='inner',keys=['master', 'ride', 'st'])
# print(tracks_from_albums)
# sum = tracks_from_albums.groupby(level=0).agg({'u_price':'sum'})
# print(sum)
# sum.plot(kind='bar')
# plt.show()

###################################### --> MELT TABLE
# #  In general, data is often provided in a format that is easily read by people but not by machines. The .melt() method is a handy tool for reshaping data into a useful form

# # In above column, in each column year is mentioned separately. We will use melt here to create only one column for year, this table will be called as tall table
# # Unpivoting all other columns except country and indicator
# # id_vars is used to ignore columns for melting. All other columns will be melted.
# # var_name and value_name argument is used to give name to columns; otherwise there name would be variable and value
# tall_table = inflation.melt(id_vars=['country','indicator'], var_name='year', value_name='annual') 
# print(tall_table)

###################################### --> 
