**What is the P-Value Formula?**

**P** is a statistical measure that helps researchers to determine whether their hypothesis is correct. It helps determine the significance of results. The null hypothesis is a default position that there is no relationship between two measured phenomena. It is denoted by H0. An alternative hypothesis is the one you would believe if the null hypothesis is concluded to be untrue. Its symbol is H1 or Ha.

P value is a number between 0 and 1. There are tables, spreadsheet programs and statistical software to help calculate the p-value. Level of significance (α) is a pre-defined threshold set by the researcher. It is generally 0.05. A very small p-value, which is lesser than the level of significance indicates that you reject the null hypothesis. P value which is greater than the level of significance indicates that we fail to reject the null hypothesis.

 
Explanation of the P-Value Formula
The formula for the calculation of the p-value can be derived by using the following steps:

Calculating P-Value from a Z Statistic
Step 1: We need to find out the test statistic z

P Value Z statistic
Where

Sample Proportionis Sample Proportion
p0 is Assumed Population Proportion in the Null Hypothesis
n is the Sample Size
Step 2: We need to find the corresponding level of p from the z value obtained. For this purpose, we need to look at the z table.

Z Table
Start Your Free Investment Banking Course

Download IB Excel Templates, Accounting, Valuation, Financial Modeling, Video Tutorials
Source: www.dummies.com

For instance, let us find the value of p corresponding to z ≥ 2.81. Since normal distribution is symmetric, negative values of z are equal to its positive values. 2.81 is a sum of 2.80 and 0.01. Look at 2.8 in z column and the corresponding value of 0.01. We get p = 0.0025.

 
Examples of P-Value Formula (with Excel Template)
Let’s see some simple to advanced examples of P-Value equation to understand it better.
You can download this P Value Formula Excel Template here – P Value Formula Excel Template
Example #1
a) P-value is 0.3015. If the level of significance is 5%, find if we can reject the null hypothesis.

b) P-value is 0.0129. If the level of significance is 5%, find if we can reject the null hypothesis.


 
Solution:

Use the following data for the calculation of P-Value.

P-value Example 1
P-Value will be –

P-value Example 1.1
a) Since the p-value of 0.3015 is greater than the level of significance of 0.05 (5%), we fail to reject the null hypothesis.

 Popular Course in this category
All in One Financial Analyst Bundle (250+ Courses, 40+ Projects)
250+ Courses | 40+ Projects | 1000+ Hours | Full Lifetime Access | Certificate of Completion
4.9 (1,067 ratings)Course Price
$299 $1999
View Course
Related Courses
M&A Modeling CourseLBO Modeling CourseValuation Modeling Course
b) Since p-value of 0.0129 is less than the level of significance of 0.05, we reject the null hypothesis.

Example #2
27% of people in India speak Hindi as per a research study. A researcher is curious if the figure is higher in his village. Hence, he frames the null and alternate hypothesis. He tests H0: p = 0.27. Ha: p > 0.27. Here, p is the proportion of people in the village who speak Hindi. He commissions a survey in his village to find out the number of people who can speak Hindi. He finds that 80 out of 240 people sampled can speak Hindi. Find out the approximate p-value for the researcher’s test if we were to assume that the necessary conditions are met and the significance level is 5%.

Solution:

Use the following data for the calculation of P-Value.

P-value Example 2
Here, the sample size n = 240,

p0 is population proportion We will have to find the sample proportionSample Proportion
= 80 / 240

Sample Proportion= 0.33

Z Statistic

Calculation of Z Statistic

P Value Z statistic
P-value Example 2.1
=0.33 – 0.27 / √ 0.27 * (1 – 0.27 ) / 240

Z Statistic will be –

P-value Example 2.2
Z = 2.093696

P Value will be –

P-value Example 2.3
P Value = P (z ≥ 2.09)

We have to look at the value of 2.09 is the z table. So, we have to look at -2.0 in z column and the value in 0.09 column. Since normal distribution is symmetrical, the area to the right of the curve is equal to that on the left. We get the p-value as 0.0183.

P Value = 0.0183

Since the p-value is less than significant level of 0.05 (5%), we reject the null hypothesis.

Note: In Excel, the p-value is coming as 0.0181

Example #3
Studies show that a higher number of flight tickets are bought by males as compared to females. They are bought by males and females in the ratio of 2:1. The research was carried out at a particular airport in India to find the distribution of air tickets among males and females. Out of 150 tickets, 88 tickets were bought by males and 62 by females. We need to find out if the experimental manipulation causes the change in the results, or we are observing a chance variation. Calculate the p-value assuming the degree of significance is 0.05.

Solution:

Use the following data for the calculation of P-Value.

Example 3
Step 1: The observed value is 88 for males and 62 for females.

Expected Value for males = 2/3* 150 = 100 males
Expected Value for females = 1/3* 150 = 50 females
Step 2: Find out chi-square

Chi Square Formula
Example 3.1
=((88-100)2)/100 + (62-50) 2/50

=1.44+2.88

Chi-Square (X^2)

Chi-Square(X^2) will be –

 Example 3.2
Chi-Square(X^2) = 4.32


 
Step 3: Find the degrees of freedom

Since there are 2 variables – males and females, n=2

Degrees of freedom = n-1 = 2-1 = 1

Step 4: From the p-value table, we look at the first row in the table as the degree of freedom is 1.We can see that p-value is between 0.025 and 0.05. Since the p-value is less than the degree of significance of 0.05, we reject the null hypothesis.

P Value will be –

Example 3.3
P Value = 0.037666922

Note: Excel directly gives the p-value using the formula:

CHITEST (actual range, expected range)

Example #4
It is known that 60% of the people who enter apparel stores in a city purchase something. An apparel shop owner wanted to find if the number is higher for the apparel shop owned by him. He already had the results of a study conducted for his shop. 128 out of 200 people who entered his shop purchased something. The shop owner denoted pas the proportion of people who entered his apparel shop and purchased something. The null hypothesis framed by him was p = 0.60 and the alternate hypothesis was p > 0.60. Find the p-value for the research at a significance level of 5%.

Solution:

Use the following data for the calculation of P-Value.

Example 4
Here, the sample size n = 200. We will have to find the sample proportion

= 128 / 200

Sample Proportion= 0.64

Z Statistic

Calculation of Z Statistic

P Value Z statistic

 
 Example 4.1
= 0.64 – 0.60 / √ 0.60 * (1 – 0.60) /200

Z Statistic will be –

 Example 4.2
Z Statistic =1.1547

P Value = P (z ≥ 1.1547)

NORMSDIST Function in Excel

Example 4.4
NORMSDIST will be –

 Example 4.5
NORMSDIST = 0.875893461

There is an inbuilt function to calculate a p-value from a z statistic in Excel. It is known as the NORMSDIST function. The Excel NORMSDIST function calculates the Standard Normal Cumulative Distribution Function from a supplied value. Its format is NORMSDIST(z). Since z statistic value is in cell B2, the function used is = NORMSDIST(B2).

P Value will be –

 Example 4.3
P Value = 0.12410654

Since we have to find the area to the right of the curve,

p-value = 1 – 0.875893 = 0.124107

Since p-value of 0.124107 is more than significant level of 0.05, we fail to reject the null hypothesis.

Source: https://www.wallstreetmojo.com/p-value-formula/

