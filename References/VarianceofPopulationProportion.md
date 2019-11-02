**Variance of population proportion**: is the squared deviation of a variable from its mean. Basically, it measures the spread of random data in a set from its mean or median value. A low value for variance indicates that the data are clustered together and are not spread apart widely, whereas a high value would indicate that the data in the given set are much more spread apart from the average value.

Python code to demonstrate the working of 

variance() function of Statistics Module 


Importing Statistics module 

import statistics 

**Creating a sample of data** 

sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98] 

Prints variance of the sample set 

Function will automatically calulate 

it's mean and set it as xbar 

print("Variance of sample set is % s"
	
	%(statistics.variance(sample)))

Output:

Variance of sample set is 0.40924

Source: https://www.geeksforgeeks.org/

