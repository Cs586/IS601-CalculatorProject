**Correlation Coefficient
Correlation coefficients** measure the strength of association between two variables. The most common correlation coefficient, called the Pearson product-moment correlation coefficient, measures the strength of the linear association between variables measured on an interval or ratio scale.

In this tutorial, when we speak simply of a correlation coefficient, we are referring to the Pearson product-moment correlation. Generally, the correlation coefficient of a sample is denoted by r, and the correlation coefficient of a population is denoted by ρ or R.


How to Interpret a Correlation Coefficient
The sign and the absolute value of a correlation coefficient describe the direction and the magnitude of the relationship between two variables.

The value of a correlation coefficient ranges between -1 and 1.
The greater the absolute value of the Pearson product-moment correlation coefficient, the stronger the linear relationship.
The strongest linear relationship is indicated by a correlation coefficient of -1 or 1.
The weakest linear relationship is indicated by a correlation coefficient equal to 0.
A positive correlation means that if one variable gets bigger, the other variable tends to get bigger.
A negative correlation means that if one variable gets bigger, the other variable tends to get smaller.
Keep in mind that the Pearson product-moment correlation coefficient only measures linear relationships. Therefore, a correlation of 0 does not mean zero relationship between two variables; rather, it means zero linear relationship. (It is possible for two variables to have zero linear relationship and a strong curvilinear relationship at the same time.)


Scatterplots and Correlation Coefficients
The scatterplots below show how different patterns of data produce different degrees of correlation.


Maximum positive correlation
(r = 1.0)


Strong positive correlation
(r = 0.80)


Zero correlation
(r = 0)


Maximum negative correlation
(r = -1.0)


Moderate negative correlation
(r = -0.43)


Strong correlation & outlier
(r = 0.71)

Several points are evident from the scatterplots.

When the slope of the line in the plot is negative, the correlation is negative; and vice versa.
The strongest correlations (r = 1.0 and r = -1.0 ) occur when data points fall exactly on a straight line.
The correlation becomes weaker as the data points become more scattered.
If the data points fall in a random pattern, the correlation is equal to zero.
Correlation is affected by outliers. Compare the first scatterplot with the last scatterplot. The single outlier in the last plot greatly reduces the correlation (from 1.00 to 0.71).

How to Calculate a Correlation Coefficient
If you look in different statistics textbooks, you are likely to find different-looking (but equivalent) formulas for computing a correlation coefficient. In this section, we present several formulas that you may encounter.

The most common formula for computing a product-moment correlation coefficient (r) is given below.

Product-moment correlation coefficient. The correlation r between two variables is:

r = Σ (xy) / sqrt [ ( Σ x2 ) * ( Σ y2 ) ]

where Σ is the summation symbol, x = xi - x, xi is the x value for observation i, x is the mean x value, y = yi - y, yi is the y value for observation i, and y is the mean y value.

The formula below uses population means and population standard deviations to compute a population correlation coefficient (ρ) from population data.

Population correlation coefficient. The correlation ρ between two variables is:

ρ = [ 1 / N ] * Σ { [ (Xi - μX) / σx ]
* [ (Yi - μY) / σy ] }

where N is the number of observations in the population, Σ is the summation symbol, Xi is the X value for observation i, μX is the population mean for variable X, Yi is the Y value for observation i, μY is the population mean for variable Y, σx is the population standard deviation of X, and σy is the population standard deviation of Y.

The formula below uses sample means and sample standard deviations to compute a sample correlation coefficient (r) from sample data.

Sample correlation coefficient. The correlation r between two variables is:

r = [ 1 / (n - 1) ] * Σ { [ (xi - x) / sx ]
* [ (yi - y) / sy ] }

where n is the number of observations in the sample, Σ is the summation symbol, xi is the x value for observation i, x is the sample mean of x, yi is the y value for observation i, y is the sample mean of y, sx is the sample standard deviation of x, and sy is the sample standard deviation of y.

The interpretation of the sample correlation coefficient depends on how the sample data are collected. With a large simple random sample, the sample correlation coefficient is an unbiased estimate of the population correlation coefficient.

Each of the latter two formulas can be derived from the first formula. Use the first or second formula when you have data from the entire population. Use the third formula when you only have sample data, but want to estimate the correlation in the population. When in doubt, use the first formula.

Fortunately, you will rarely have to compute a correlation coefficient by hand. Many software packages (e.g., Excel) and most graphing calculators have a correlation function that will do the job for you.


Test Your Understanding
Problem 1

A national consumer magazine reported the following correlations.

The correlation between car weight and car reliability is -0.30.
The correlation between car weight and annual maintenance cost is 0.20.
Which of the following statements are true?

I. Heavier cars tend to be less reliable.
II. Heavier cars tend to cost more to maintain.
III. Car weight is related more strongly to reliability than to maintenance cost.

(A) I only
(B) II only
(C) III only
(D) I and II only
(E) I, II, and III

Solution

The correct answer is (E). The correlation between car weight and reliability is negative. This means that reliability tends to decrease as car weight increases. The correlation between car weight and maintenance cost is positive. This means that maintenance costs tend to increase as car weight increases.

The strength of a relationship between two variables is indicated by the absolute value of the correlation coefficient. The correlation between car weight and reliability has an absolute value of 0.30. The correlation between car weight and maintenance cost has an absolute value of 0.20. Therefore, the relationship between car weight and reliability is stronger than the relationship between car weight and maintenance cost.

Source: stattrek.com







