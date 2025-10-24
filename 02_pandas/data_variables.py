import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Create dataframe from List of dictionaries
avocados_data = [
    {"date": "2015-08-23", "type": "organic", "year": 2015, "avg_price": np.nan, "size": "small", "nb_sold": 34},
    {"date": "2015-12-20", "type": "organic", "year": 2015, "avg_price": 0.98, "size": "small", "nb_sold": 123},
    {"date": "2015-12-13", "type": "organic", "year": 2015, "avg_price": 0.93, "size": "small", "nb_sold": 120033},
    {"date": "2015-12-06", "type": "conventional", "year": 2015, "avg_price": 0.89, "size": "small", "nb_sold": None},
    {"date": "2015-08-23", "type": "conventional", "year": 2015, "avg_price": 0.99, "size": "small", "nb_sold": 321},
    {"date": "2015-12-06", "type": "organic", "year": 2015, "avg_price": 1.80, "size": "large", "nb_sold": 15000},
    {"date": "2015-08-23", "type": "organic", "year": 2015, "avg_price": 1.75, "size": "large", "nb_sold": 17000},
    {"date": "2015-08-23", "type": "organic", "year": 2015, "avg_price": 1.90, "size": "extra_large", "nb_sold": 120000},
    {"date": "2015-11-01", "type": "conventional", "year": 2015, "avg_price": None, "size": "extra_large", "nb_sold": None},
    {"date": "2015-10-25", "type": "conventional", "year": 2015, "avg_price": 0.82, "size": "small", "nb_sold": 321},
    {"date": "2015-10-18", "type": "conventional", "year": 2015, "avg_price": 0.85, "size": "large", "nb_sold": 2312},
    {"date": "2015-10-11", "type": "organic", "year": 2015, "avg_price": 0.92, "size": "small", "nb_sold": 1231},
    {"date": "2015-10-04", "type": "organic", "year": 2015, "avg_price": 1.50, "size": "large", "nb_sold": None},
    {"date": "2015-12-06", "type": "organic", "year": 2015, "avg_price": 1.45, "size": "small", "nb_sold": 20000},
    {"date": "2015-12-06", "type": "organic", "year": 2015, "avg_price": 1.40, "size": "extra_large", "nb_sold": 1800},
    {"date": "2015-09-13", "type": "conventional", "year": 2015, "avg_price": 0.88, "size": "large", "nb_sold": 123},
    {"date": "2015-09-13", "type": "conventional", "year": 2015, "avg_price": 0.90, "size": "large", "nb_sold": 12321},
    {"date": "2015-12-06", "type": "organic", "year": 2015, "avg_price": 1.60, "size": "large", "nb_sold": 14500},
    {"date": "2015-08-23", "type": "organic", "year": 2015, "avg_price": 1.55, "size": "extra_large", "nb_sold": 16600},
    {"date": "2015-08-23", "type": "conventional", "year": 2015, "avg_price": 0.83, "size": "small", "nb_sold": 12321},
]
avocados = pd.DataFrame(avocados_data)

### Create data frame from dictionary of lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
my_dict = {
    "country": names,
    "drives_right": dr,
    "cars_per_cap": cpc
}
cars_df = pd.DataFrame(my_dict) # Build a DataFrame cars from my_dict: cars

###
test_df = pd.DataFrame({
    'A': 1.0,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})

### Importing Data from a CSV
cars = pd.read_csv('/home/tk-lpt-648/my-work/Personal/Projects/python/00_datasets/cars.csv', index_col=0) # set 1st column as index column

### Importing Data from a CSV
sales = pd.read_csv('/home/tk-lpt-648/my-work/Personal/Projects/python/00_datasets/sales_data.csv')
sales['date'] = pd.to_datetime(sales['date'],
                            #    errors='coerce' # # Return missing value for error(wrong date format)
                               ) # convert date column to dateTime type

#########################################################################
taxi_owners_list = [
  { "rid": "T6285", "vid": 6285, "owner": "AGEAN TAXI LLC", "address": "4536 N. ELSTON AVE.", "zip": 60630 },
  { "rid": "T1495", "vid": 1495, "owner": "FUNRIDE, INC.", "address": "3351 W. ADDISON ST.", "zip": 60618 },
  { "rid": "T5971", "vid": 5971, "owner": "EUNIFFORD INC.", "address": "3351 W. ADDISON ST.", "zip": 60618 },
  { "rid": "T3867", "vid": 3867, "owner": "T-BAR TAXI LLC", "address": "2532 W. WARREN BLVD.", "zip": 60612 },
  { "rid": "T1236", "vid": 1236, "owner": "YC20 LLC", "address": "3351 W. ADDISON ST.", "zip": 60618 },
  { "rid": "T2164", "vid": 2164, "owner": "COMPUTER CAB CO", "address": "4626 W. CORNELIA AVE.", "zip": 60641 },
  { "rid": "T5494", "vid": 54944, "owner": "NBA TAXI INC.", "address": "4020 W. GLENLAKE AVE.", "zip": 60646 },
  { "rid": "T227", "vid": 227, "owner": "BABY CAB CORP.", "address": "2617 S. WABASH AVE.", "zip": 60616 },
  { "rid": "T1609", "vid": 1609, "owner": "MG & KA INC", "address": "3351 W. ADDISON ST.", "zip": 60618 },
  { "rid": "T1447", "vid": 1447, "owner": "SNOWSTORM II HACKING CORP.", "address": "2617 S. WABASH AVE.", "zip": 60616 },
  { "rid": "T468", "vid": 468, "owner": "M ASANTE INC.", "address": "3351 W. ADDISON ST.", "zip": 60618 }
]
taxi_vehicle_list = [
  { "vid": 6285, "make": "TOYOTA", "model": "CAMRY", "year": 2013, "fuel_type": "HYBRID", "owner": "SEYED M. BADRI", "zip":60630 },
  { "vid": 1495, "make": "TOYOTA", "model": "RAV4", "year": 2017, "fuel_type": "HYBRID", "owner": "DESZY CORP." },
  { "vid": 5971, "make": "NISSAN", "model": "SENTRA", "year": 2019, "fuel_type": "GASOLINE", "owner": "AGAPH CAB CORP" },
  { "vid": 3867, "make": "FORD", "model": "ESCAPE", "year": 2012, "fuel_type": "HYBRID", "owner": "BLUE EYES CAB CORP.", "zip": 60612 },
  { "vid": 2164, "make": "TOYOTA", "model": "PRIUS", "year": 2013, "fuel_type": "HYBRID", "owner": "SKAMPA INC." },
  { "vid": 227, "make": "TOYOTA", "model": "CAMRY", "year": 2014, "fuel_type": "HYBRID", "owner": "3860 TAXI CORP" },
  { "vid": 1447, "make": "TOYOTA", "model": "CAMRY", "year": 2015, "fuel_type": "HYBRID", "owner": "SARDAR BAIG ENTERPRISES INC" },
  { "vid": 12332, "make": "TOYOTA", "model": "CAMRY", "year": 2013, "fuel_type": "HYBRID", "owner": "RIDGEVIEW CAB CORP.", "zip":60618  },
  { "vid": 1609, "make": "TOYOTA", "model": "RAV4", "year": 2015, "fuel_type": "GASOLINE", "owner": "LEROY RAMSAY" },
  { "vid": 5494, "make": "TOYOTA", "model": "CAMRY", "year": 2011, "fuel_type": "HYBRID", "owner": "BATUNDE INC" },
  { "vid": 1236, "make": "TOYOTA", "model": "CAMRY", "year": 2013, "fuel_type": "HYBRID", "owner": "SAHARAN CAB INC", "zipp":60618 },
  { "vid": 3311, "make": "TOYOTA", "model": "SIENNA", "year": 2019, "fuel_type": "GASOLINE", "owner": "1363 CAB INC" },
]

taxi_owners = pd.DataFrame(taxi_owners_list)
taxi_vehicle = pd.DataFrame(taxi_vehicle_list)

#########################################################################
jpm_list = [
    {"date_time": "2017-11-17 15:35:17", "close": 98.120},
    {"date_time": "2017-11-17 15:40:04", "close": 98.180},
    {"date_time": "2017-11-17 15:45:01", "close": 97.731},
    {"date_time": "2017-11-17 15:50:55", "close": 97.740},
    {"date_time": "2017-11-17 15:55:00", "close": 97.815},
    {"date_time": "2017-11-17 16:00:30", "close": 98.020},
    {"date_time": "2017-11-17 16:05:07", "close": 97.800},
]
wells_list = [
    {"date_time": "2017-11-17 15:35:08", "close": 54.323},
    {"date_time": "2017-11-17 15:40:00", "close": 54.320},
    {"date_time": "2017-11-17 15:45:32", "close": 54.190},
    {"date_time": "2017-11-17 15:50:07", "close": 54.170},
    {"date_time": "2017-11-17 15:55:00", "close": 54.184},
    {"date_time": "2017-11-17 16:00:30", "close": 54.265},
    {"date_time": "2017-11-17 16:05:52", "close": 54.200},
    {"date_time": "2017-11-17 16:10:22", "close": 54.155},
    {"date_time": "2017-11-17 16:15:43", "close": 54.190},
    {"date_time": "2017-11-17 16:20:07", "close": 54.205},
]

jpm = pd.DataFrame(jpm_list)
wells = pd.DataFrame(wells_list)
jpm['date_time'] = pd.to_datetime(jpm['date_time']) # convert date_time column to dateTime type
wells['date_time'] = pd.to_datetime(wells['date_time']) # convert date_time column to dateTime type

#########################################################################
tracks_master_list = [
    {"tid": 1853, "name": "Battery", "aid": 152, "mtid": 1, "gid": 3, "composer": "J.Hetfield/L.Ulrich", "u_price": 0.99},
    {"tid": 1854, "name": "Master Of Puppets", "aid": 152, "mtid": 1, "gid": 3, "composer": "K.Hammett", "u_price": 0.99},
    {"tid": 1857, "name": "Disposable Heroes", "aid": 152, "mtid": 1, "gid": 3, "composer": "J.Hetfield/L.Ulrich", "u_price": 0.99},
]
tracks_ride_list = [
    {"tid": 1874, "name": "Fight Fire With Fire", "aid": 154, "mtid": 1, "gid": 3, "u_price": 0.99},
    {"tid": 1875, "name": "Ride The Lightning", "aid": 154, "mtid": 1, "gid": 3, "u_price": 0.99},
    {"tid": 1876, "name": "For Whom The Bell Tolls", "aid": 154, "mtid": 1, "gid": 3, "u_price": 0.99},
    {"tid": 1877, "name": "Fade To Black", "aid": 154, "mtid": 1, "gid": 3, "u_price": 0.99},
    {"tid": 1878, "name": "Trapped Under Ice", "aid": 154, "mtid": 1, "gid": 3, "u_price": 0.99},
]
tracks_st_list = [
    {"tid": 1882, "name": "Frantic", "aid": 155, "mtid": 1, "gid": 3, "u_price": 0.99},
    {"tid": 1883, "name": "St. Anger", "aid": 155, "mtid": 1, "gid": 3, "u_price": 0.99},
    {"tid": 1884, "name": "Some Kind Of Monster", "aid": 155, "mtid": 1, "gid": 3, "u_price": 0.99},
    {"tid": 1885, "name": "Dirty Window", "aid": 155, "mtid": 1, "gid": 3, "u_price": 0.99},
    {"tid": 1886, "name": "Invisible Kid", "aid": 155, "mtid": 1, "gid": 3, "u_price": 0.99},
]
tracks_master = pd.DataFrame(tracks_master_list)
tracks_ride = pd.DataFrame(tracks_ride_list)
tracks_st = pd.DataFrame(tracks_st_list)

#########################################################################
inflation_list = [
    {'country': 'Brazil', 'indicator': 'Inflation %', 2017: 3.45, 2018: 3.66, 2019: 3.73},
    {'country': 'Canada', 'indicator': 'Inflation %', 2017: 1.6, 2018: 2.27, 2019: 1.95},
    {'country': 'France', 'indicator': 'Inflation %', 2017: 1.03, 2018: 1.85, 2019: 1.11},
    {'country': 'India', 'indicator': 'Inflation %', 2017: 2.49, 2018: 4.86, 2019: 7.66}
]
inflation = pd.DataFrame(inflation_list)