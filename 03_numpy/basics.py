
# Import the numpy package as np
import numpy as np

# # Create 1-D numpy arrays using different methods
# # Note: np.zeros(), np.ones(), np.empty(), np.full(), and np.arange() are used to create numpy arrays with specific initial values or shapes
# a = np.zeros(3) # Create a numpy array of zeros with 3 elements
# aa = np.zeros(5, dtype=np.int8) # Create a numpy array of zeros with 5 elements and integer type
# aaa = np.zeros(5, dtype=np.float64) # Create a numpy array of zeros with 5 elements and float type
# b = np.ones(3) # Create a numpy array of ones with 3 elements
# c = np.empty(3) # Create a numpy array of empty elements with 3 elements # Note: np.empty() does not initialize the elements, it just allocates memory. The values will be whatever was in memory before.
# d = np.full(3, 5) # Create a numpy array of 3 elements with all elements initialized to 5
# e = np.arange(3) # Create a numpy array with elements 0, 1, 2
# f = np.arange(3, 10) # Create a numpy array with elements 3, 4, 5, 6, 7, 8, 9
# g = np.arange(3, 10, 2) # Create a numpy array with elements 3, 5, 7, 9 (step of 2)
# h = np.linspace(0, 1, 5) # Create a numpy array with 5 elements evenly spaced between 0 and 1
# print("a: ", a,'\n',"aa: ", aa,'\n',"aaa: ", aaa,'\n',"b: ", b,'\n',"c: ", c,'\n',"d: ", d,'\n',"e: ", e,'\n',"f: ", f,'\n',"g: ", g,'\n',"h: ", h)

# # Create a 2-D numpy arrays using different methods
# a = np.zeros((3, 4)) # Create a 2-D numpy array of zeros with 3 rows and 4 columns
# b = np.ones((2, 3)) # Create a 2-D numpy array of ones with 2 rows and 3 columns
# c = np.empty((2, 3)) # Create a 2-D numpy array of empty elements with 2 rows and 3 columns
# d = np.full((2, 3), 5) # Create a 2-D numpy array of 2 rows and 3 columns with all elements initialized to 5
# e = np.arange(3, 10, 2).reshape((2, 2)) # Create a 2-D numpy array with elements 3, 5, 7, 9 and reshape it to 2 rows and 4 columns
# f = np.linspace(0, 1, 6).reshape((2, 3)) # Create a 2-D numpy array with 6 elements evenly spaced between 0 and 1 and reshape it to 2 rows and 3 columns
# g = np.random.rand(2, 3) # Create a 2-D numpy array with random float numbers between 0 and 1 with 2 rows and 3 columns
# print("a: ", a,'\n',"b: ", b,'\n',"c: ", c,'\n',"d: ", d,'\n',"e: ", e,'\n',"f: ", f,'\n',"g: ", g)

# # Create a 3-D numpy arrays using different methods
# a = np.arange(24).reshape((2, 3, 4)) # Create a 3-D numpy array with elements from 0 to 23 and reshape it to 2 layers, 3 rows, and 4 columns
# print(a)
# print(a.ndim) # Get the number of dimensions of the array
# print(a.size) # Get the total number of elements in the array
# print(a.shape) # Get the shape of the array (number of layers, rows, columns)
# print(a.dtype) # Get the data type of the array elements


# ### Create a numpy array from a list or tuple
# baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# np_baseball = np.array(baseball)

# # Convert 1-D array into 2-D array
# print(np_baseball.reshape((2, 4))) # Reshape the 1-D array into a 2-D array with 2 rows and 4 columns
# print(np_baseball[np.newaxis, :]) # Add a new axis to the array, converting it into a 2-D array with 1 row and 8 columns
# print(np_baseball[:, np.newaxis]) # Add a new axis to the array, converting it into a 2-D array with 8 rows and 1 column

# # Operations and indexing on NumPy Arrays
# double_np_baseball = np_baseball * 2 # it will take each element and multiple it with 2
# add_np_baseball = np_baseball + 2 # it will take each element and add 2 to it

# print(type(np_baseball))
# print(double_np_baseball)
# print(add_np_baseball)
# print(add_np_baseball[0])
# print(add_np_baseball[0:2])
# print(np_baseball > 200)
# print(np_baseball[np_baseball > 200])

# print(np.logical_or(np_baseball > 200, np_baseball < 180)) # np_baseball > 200 or np_baseball < 180
# print(np_baseball[np.logical_or(np_baseball > 200, np_baseball < 180)]) # np_baseball > 200 or np_baseball < 180
# print(np.logical_and(np_baseball > 200, np_baseball <= 210)) # np_baseball > 200 and np_baseball <= 210
# print(np.logical_not(np_baseball > 200)) # not  np_baseball > 200

# ### Array Fucntions
# arr = [10, 11.5, 3,2, 15, 27.2, 8, 9.5]
# arr1 = [2, 4, 2, 6, 1]
# nparr = np.array(arr)
# nparr1 = np.array(arr1)

# # nparr.sort() # Sort the array in-place
# # print("a: ", nparr)
# print("b: ", np.sort(nparr)) # Sort the array and return a new array
# print("c: ", np.concatenate((nparr, nparr1))) # Concatenate two arrays
# print("d: ", np.append(nparr, nparr1)) # Append one array to another
# print("e: ", np.unique(nparr1)) # Get unique elements from the array
# print("f: ", np.sum(nparr1)) # Get sum of all elements in the array
# print("g: ", nparr1.mean()) # Get mean of all elements in the array 


## numpy arrays cannot contain elements with different types
# bool_converted_to_number = np.array([True, 1, 2]) + np.array([3, 4, False])
# print(bool_converted_to_number)

# ##### 2D NumPy Array
# list_of_lists = [
#             [180, 78.4],
#             [215, 102.7],
#             [210, 98.5],
#             [188, 3]]
# np_2d_array = np.array(list_of_lists)

# print(np_2d_array.shape)
# print(np_2d_array)


## Subsetting 2D NumPy Arrays
# print(np_2d_array[0][0]) # value at row = 0 and column = 0
# print(np_2d_array[0, 0]) # value at row = 0 and column = 0
# print(np_2d_array[0]) # all values at row = 0
# print(np_2d_array[0, :]) # all values at row = 0 -- means select row = 0 and all columns
# print(np_2d_array[:, 1]) # all values at column = 1 -- means select all rows and column = 1
# print(np_2d_array[:, 1][1]) # select all rows and column = 1; and then pick value at 1 index

# ## arithmatic operations on 2d array
# list_of_lists2 = [
#             [2, 3],
#             [5, 0],
#             [1, 3],
#             [7, 4]]
# np_2d_array2 = np.array(list_of_lists2)
            
# print(np_2d_array + np_2d_array2)
# print(np_2d_array2 * np.array([2, 0]))
# print(np_2d_array >= np_2d_array2)

# ## Concatenation
# concatenatedRows = np.concatenate((np_2d_array, np_2d_array2), axis=0) # Concatenate along rows
# concatenatedCol = np.concatenate((np_2d_array, np_2d_array2), axis=1) # Concatenate along columns
# print(concatenatedRows)
# print(concatenatedCol)

# ## Statictics - mean, median, mode, std, correlation
# all_rows_first_col = np_2d_array[:, 0]
# all_rows_second_col = np_2d_array[:, 1]
# avg = np.mean(all_rows_first_col)
# print("Average: " + str(avg))
# print(np.median(all_rows_first_col))
# print(np.std(all_rows_first_col)) # Get standard Deviation
# print(np.corrcoef(all_rows_first_col, all_rows_second_col)) # Get correlation between first and second column


### LOOPS

# # For loop over 1D Array
# baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# np_baseball = np.array(baseball)
# for b in np_baseball:
#     print(f"{b} inches")

# # For loop over 2D Array
# list_of_lists = [
#         [2, 3],
#         [5, 0],
#         [1, 3],
#         [7, 4]]
# np_2d_array = np.array(list_of_lists)
# for l in np.nditer(np_2d_array):
#     print(f"{l} litre")

# ### Random Number
# # due to seed, "np.random.rand()" variable will always return consistent result for same sequence - means 1st rand, 2nd rand, 3rd rand will always have same value when "np.random.rand()" is called
# # If seed is not provided, "np.random.rand()" will work as normal random method. No consitency in returned values
# np.random.seed(123) 
# rand = np.random.rand() # Generate random float number b/w 0 and 1
# print(rand)

# print(np.random.randint(1, 7)) # Generates random integer between 1 and 6. 7 is not included
# print(np.random.randint(1, 7))
# print(np.random.randn(2, 4)) # Generates 2 rows and 4 columns of random float numbers from standard normal distribution (mean=0, std=1)
# print(np.random.randint(1, 7, size=(2, 4))) # Generates 2 rows and 4 columns of random integers between 1 and 6