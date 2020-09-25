# Calculating Financial Statistics

`display_as_percentage()`: converting a decimal value to the percent form

### Simple Rate of Return
The difference between the starting and ending price of an investment over a time period, divided by the starting price.
If an investment returns dividends, those dividends should be added to the numerator.
#### <a href="https://www.codecogs.com/eqnedit.php?latex=R&space;=&space;\frac{E&space;-&space;S&space;&plus;&space;D}{S}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R&space;=&space;\frac{E&space;-&space;S&space;&plus;&space;D}{S}" title="R = \frac{E - S + D}{S}" /></a>
R: simple rate of return<br />
S: starting price of investment<br />
E: ending price of investment<br />
D: dividend<br />

`calculate_simple_return()`: calculate the simple rate of return
### Logarithmic Rate of Return
Also known as the continuously compounded return.
This is the expected return for an investment where the earnings are assumed to be continually reinvested over the time period.
It is calculated by taking the difference between the log of the ending price and the log of the starting price.
#### <a href="https://www.codecogs.com/eqnedit.php?latex=r&space;=&space;log(E)&space;-&space;log(S)&space;=&space;log(\frac{E}{S})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r&space;=&space;log(E)&space;-&space;log(S)&space;=&space;log(\frac{E}{S})" title="r = log(E) - log(S) = log(\frac{E}{S})" /></a>
r: logarithmic rate of return<br />
S: starting price of investment<br />
E: ending price of investment<br />

`calculate_log_return()`: calculate the logarithmic rate of return

### Aggregate Across Time I
When describing the rate of return of an investment, something that is important to keep in mind is the time frame of the investment.
Aggregating across time for a single asset can easily be calculated using the log rate of return.
To convert a log rate of return from one time period to another, we can multiple the rate of return by the number of original time periods there are in the new time period.
#### r = r<sub>0</sub> * t
r: converted log rate of return<br />
r0: original log rate of return<br />
t: the number of original time periods in the new time period<br />

If we are converting daily returns to annual returns, t may be 252 because that is typically the number of trading days in a year.
`calculate_variance()`: calculate the variance

`annualize_return()`: calculate the converted rate of return

### Aggregate Across Time II
An extension of the previous conversion formula.
#### <a href="https://www.codecogs.com/eqnedit.php?latex=r&space;=&space;\frac{r0_{1}&space;&plus;&space;r0_{2}&space;&plus;&space;...&space;r0_{n}}{n}&space;*&space;t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r&space;=&space;\frac{r0_{1}&space;&plus;&space;r0_{2}&space;&plus;&space;...&space;r0_{n}}{n}&space;*&space;t" title="r = \frac{r0_{1} + r0_{2} + ... r0_{n}}{n} * t" /></a>
r: converted log rate of return<br />
r<sub>0</sub><sub>n</sub>: the n<sup>th</sup> log return from the original time period<br />
n: the number of returns from the original time period<br />
t: the number of original time periods in the new time period

`convert_returns()`: calculate the converted rate of return

### Aggregate Across Assets
Investments often make up the pieces of a larger financial portfolio.
Let’s get a preview of how to calculate the expected rate of return for an entire portfolio of investments.
Using the simple rate of return makes it easy to aggregate across multiple assets. The portfolio return would simply be the weighted average of each individual asset’s simple rate of return.
#### <a href="https://www.codecogs.com/eqnedit.php?latex=R&space;=&space;(W_{1}&space;*&space;R_{1})&space;&plus;&space;(W_{2}&space;*&space;R_{2})&space;&plus;&space;...&space;&plus;&space;(W_{n}&space;*&space;R_{n})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R&space;=&space;(W_{1}&space;*&space;R_{1})&space;&plus;&space;(W_{2}&space;*&space;R_{2})&space;&plus;&space;...&space;&plus;&space;(W_{n}&space;*&space;R_{n})" title="R = (W_{1} * R_{1}) + (W_{2} * R_{2}) + ... + (W_{n} * R_{n})" /></a>
R: portfolio simple rate of return<br />
W<sub>i</sub>: weight of the i<sup>th</sup> investment in the portfolio<br />
R<sub>i</sub>: simple rate of return of the i<sup>th</sup> investment in the portfolio

The weights of each asset is obtained by:
#### <a href="https://www.codecogs.com/eqnedit.php?latex=W_{i}&space;=&space;\frac{S_{i}}{S_{1}&space;&plus;&space;S_{2}&space;&plus;&space;...&space;&plus;&space;S_{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?W_{i}&space;=&space;\frac{S_{i}}{S_{1}&space;&plus;&space;S_{2}&space;&plus;&space;...&space;&plus;&space;S_{n}}" title="W_{i} = \frac{S_{i}}{S_{1} + S_{2} + ... + S_{n}}" /></a>
W<sub>i</sub>: weight of the i<sup>th</sup> investment in the portfolio<br />
S<sub>i</sub>: starting price of the i<sup>th</sup> investment in the portfolio
### Variance
One of the key statistics for understanding risk is variance. Variance is a measure of the spread of a dataset, or how far apart each value is from the mean. The greater the variance, the more spread out or variable the data is.
An asset with a high variance is generally a riskier one because its return can vary significantly in a short period of time, making it less stable and more unpredictable.
The formula for calculating variance is:
#### <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma^{2}&space;=&space;\frac{\sum&space;(X_{i}&space;-&space;\bar{X})^2}{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma^{2}&space;=&space;\frac{\sum&space;(X_{i}&space;-&space;\bar{X})^2}{n}" title="\sigma^{2} = \frac{\sum (X_{i} - \bar{X})^2}{n}" /></a>
σ<sup>2</sup>: variance<br />
X<sub>i</sub>: the i<sup>th</sup> value in the dataset<br />
X̄: the mean of the dataset<br />
n: the number of values in the dataset
### Standard Deviation
It is common to use the standard deviation to describe the spread of the dataset.
Standard deviation is simply the square root of the variance. It has the same unit as the original dataset.
#### <a href="https://www.codecogs.com/eqnedit.php?latex=\sigma&space;=&space;\sqrt[]{\frac{\sum&space;(X_{i}&space;-&space;\bar{X})^2}{n}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma&space;=&space;\sqrt[]{\frac{\sum&space;(X_{i}&space;-&space;\bar{X})^2}{n}}" title="\sigma = \sqrt[]{\frac{\sum (X_{i} - \bar{X})^2}{n}}" /></a>
σ: standard deviation<br />
X<sub>i</sub: the i<sup>th</sup> value in the dataset<br />
X̄: the mean of the dataset<br />
n: the number of values in the dataset

`calculate_stddev()`: calculate the standard deviation
### Correlation I
Another important statistic for assessing risk is the correlation between the returns of two assets. Correlation is a measure of how closely two datasets are associated with each other. It is often represented by the correlation coefficient, which is a value that ranges between -1 and 1. This indicates whether there is a positive correlation, negative correlation, or no correlation:
* **Positive correlation** – when the rate of return of one asset deviates upward from its mean, the other usually deviates upward as well.

* **Negative correlation** – when the rate of return of one asset deviates upward from its mean, the other usually deviates downward.

* **No correlation** – when a change in one asset’s rate of return does not dictate a change in another. The correlation coefficient will be close to 0.

Two assets from the same industry generally have a positive correlation, as they are likely affected by similar external conditions.
When building a portfolio, it is generally a good idea to include assets that are not correlated with each other. If assets are independent of one another, then there is a lower risk of the financial loss that can occur when assets in a portfolio are correlated. This allows for greater diversification and balances out the overall risk and return of the portfolio.

The formula for the Pearson correlation coefficient:
### <a href="https://www.codecogs.com/eqnedit.php?latex=r_{xy}&space;=&space;\frac{n&space;*&space;\sum&space;(X_{i}&space;*&space;Y_{i})&space;-&space;\sum&space;X_{i}&space;*&space;\sum&space;Y_{i}}{\sqrt{n&space;*&space;\sum&space;X_{i}^{2}&space;-&space;(\sum&space;X_{i})^{2}}\sqrt{n&space;*&space;\sum&space;Y_{i}^{2}&space;-&space;(\sum&space;Y_{i})^{2}}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_{xy}&space;=&space;\frac{n&space;*&space;\sum&space;(X_{i}&space;*&space;Y_{i})&space;-&space;\sum&space;X_{i}&space;*&space;\sum&space;Y_{i}}{\sqrt{n&space;*&space;\sum&space;X_{i}^{2}&space;-&space;(\sum&space;X_{i})^{2}}\sqrt{n&space;*&space;\sum&space;Y_{i}^{2}&space;-&space;(\sum&space;Y_{i})^{2}}}" title="r_{xy} = \frac{n * \sum (X_{i} * Y_{i}) - \sum X_{i} * \sum Y_{i}}{\sqrt{n * \sum X_{i}^{2} - (\sum X_{i})^{2}}\sqrt{n * \sum Y_{i}^{2} - (\sum Y_{i})^{2}}}" /></a>
r<sub>xy</sub>: correlation coefficient<br />
X<sub>i</sub>: the i<sup>th</sup> value in dataset X<br />
Y<sub>i</sub>: the i<sup>th</sup> value in dataset Y<br />
n: the number of values in the dataset
