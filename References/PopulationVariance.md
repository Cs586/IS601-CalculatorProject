How to Measure **Variability**
Statisticians use summary measures to describe the amount of variability or spread in a set of data. The most common measures of variability are the range, the interquartile range (IQR), variance, and standard deviation.

The Range
The range is the difference between the largest and smallest values in a set of values.

For example, consider the following numbers: 1, 3, 4, 5, 5, 6, 7, 11. For this set of numbers, the range would be 11 - 1 or 10.

The Interquartile Range (IQR)
The interquartile range (IQR) is a measure of variability, based on dividing a data set into quartiles.

Quartiles divide a rank-ordered data set into four equal parts. The values that divide each part are called the first, second, and third quartiles; and they are denoted by Q1, Q2, and Q3, respectively.

Q1 is the "middle" value in the first half of the rank-ordered data set.
Q2 is the median value in the set.
Q3 is the "middle" value in the second half of the rank-ordered data set.
The interquartile range is equal to Q3 minus Q1. For example, consider the following numbers: 1, 2, 3, 4, 5, 6, 7, 8.

Eight numbers: 1, 2, 3, 4, 5, 6, 7, 8
Q2 is the median of the entire data set - the middle value. In this example, we have an even number of data points, so the median is equal to the average of the two middle values. Thus, Q2 = (4 + 5)/2 or Q2 = 4.5. Q1 is the middle value in the first half of the data set. Since there are an even number of data points in the first half of the data set, the middle value is the average of the two middle values; that is, Q1 = (2 + 3)/2 or Q1 = 2.5. Q3 is the middle value in the second half of the data set. Again, since the second half of the data set has an even number of observations, the middle value is the average of the two middle values; that is, Q3 = (6 + 7)/2 or Q3 = 6.5. The interquartile range is Q3 minus Q1, so IQR = 6.5 - 2.5 = 4.

Notice that this process divided the data set into four parts of equal size. The first part consists of 1 and 2; the second part, 3 and 4; the third part, 5 and 6; and the fourth part, 7 and 8.


An Alternative Definition for IQR
In some texts, the interquartile range is defined differently. It is defined as the difference between the largest and smallest values in the middle 50% of a set of data.

To compute an interquartile range using this definition, first remove observations from the lower quartile. Then, remove observations from the upper quartile. Then, from the remaining observations, compute the difference between the largest and smallest values.

For example, consider the following numbers: 1, 2, 3, 4, 5, 6, 7, 8. After we remove observations from the lower and upper quartiles, we are left with: 3, 4, 5, 6. The interquartile range (IQR) would be 6 - 3 = 3.

The Variance
In a population, variance is the average squared deviation from the population mean, as defined by the following formula:

σ2 = Σ ( Xi - μ )2 / N

where σ2 is the population variance, μ is the population mean, Xi is the ith element from the population, and N is the number of elements in the population.

Observations from a simple random sample can be used to estimate the variance of a population. For this purpose, sample variance is defined by slightly different formula, and uses a slightly different notation:

s2 = Σ ( xi - x )2 / ( n - 1 )

where s2 is the sample variance, x is the sample mean, xi is the ith element from the sample, and n is the number of elements in the sample. Using this formula, the sample variance can be considered an unbiased estimate of the true population variance. Therefore, if you need to estimate an unknown population variance, based on data from a simple random sample, this is the formula to use.

The Standard Deviation
The standard deviation is the square root of the variance. Thus, the standard deviation of a population is:

σ = sqrt [ σ2 ] = sqrt [ Σ ( Xi - μ )2 / N ]

where σ is the population standard deviation, μ is the population mean, Xi is the ith element from the population, and N is the number of elements in the population.

Statisticians often use simple random samples to estimate the standard deviation of a population, based on sample data. Given a simple random sample, the best estimate of the standard deviation of a population is:

s = sqrt [ s2 ] = sqrt [ Σ ( xi - x )2 / ( n - 1 ) ]

where s is the sample standard deviation, x is the sample mean, xi is the ith element from the sample, and n is the number of elements in the sample.

Effect of Changing Units
Sometimes, researchers change units (minutes to hours, feet to meters, etc.). Here is how measures of variability are affected when we change units.

If you add a constant to every value, the distance between values does not change. As a result, all of the measures of variability (range, interquartile range, standard deviation, and variance) remain the same.
On the other hand, suppose you multiply every value by a constant. This has the effect of multiplying the range, interquartile range (IQR), and standard deviation by that constant. It has an even greater effect on the variance. It multiplies the variance by the square of the constant.

Test Your Understanding
Problem 1

A population consists of four observations: {1, 3, 5, 7}. What is the variance?

(A) 2
(B) 4
(C) 5
(D) 6
(E) None of the above

Solution

The correct answer is (C). First, we need to compute the population mean.

μ = ΣX / N = ( 1 + 3 + 5 + 7 ) / 4 = 4

Then we plug all of the known values into formula for the variance of a population, as shown below:

σ2 = Σ ( Xi - μ )2 / N
σ2 = [ ( 1 - 4 )2 + ( 3 - 4 )2 + ( 5 - 4 )2 + ( 7 - 4 )2 ] / 4
σ2 = [ ( -3 )2 + ( -1 )2 + ( 1 )2 + ( 3 )2 ] / 4
σ2 = [ 9 + 1 + 1 + 9 ] / 4 = 20 / 4 = 5

Note: Sometimes, students are unsure about whether the denominator in the formula for the variance should be N or (n - 1). We use N to compute the variance of a population, based on population data; and we use (n - 1) to estimate the variance of a population, based on sample data. In this problem, we are computing the variance of a population based on population data, so this solution uses N in the denominator.




Problem 2

A simple random sample consists of four observations: {1, 3, 5, 7}. Based on these sample observations, what is the best estimate of the standard deviation of the population?

(A) 2
(B) 2.58
(C) 6
(D) 6.67
(E) None of the above

Solution

The correct answer is (B). First, we need to compute the sample mean.

x = Σx / n = ( 1 + 3 + 5 + 7 ) / 4 = 4

Then we plug all of the known values into formula for the standard deviation of a sample, as shown below:

s = sqrt [ Σ ( xi - x )2 / ( n - 1 ) ]
s = sqrt { [ ( 1 - 4 )2 + ( 3 - 4 )2 + ( 5 - 4 )2 + ( 7 - 4 )2 ] / ( 4 - 1 ) }
s = sqrt { [ ( -3 )2 + ( -1 )2 + ( 1 )2 + ( 3 )2 ] / 3 }
s = sqrt { [ 9 + 1 + 1 + 9 ] / 3 } = sqrt (20 / 3) = sqrt ( 6.67 ) = 2.58

Note: This problem asked us to estimate the standard deviation of a population, based on sample data. To do this, we used (n - 1) in the denominator of the standard deviation formula. If the problem had asked us to compute the standard deviation of a population based on population data, we would have used N in the denominator.

Source: stattrek.com