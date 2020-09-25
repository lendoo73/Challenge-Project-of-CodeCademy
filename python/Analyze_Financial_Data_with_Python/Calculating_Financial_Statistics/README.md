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

`annualize_return()`: calculate the converted rate of return

### Aggregate Across Time II
An extension of the previous conversion formula.
#### <a href="https://www.codecogs.com/eqnedit.php?latex=r&space;=&space;\frac{r0_{1}&space;&plus;&space;r0_{2}&space;&plus;&space;...&space;r0_{n}}{n}&space;*&space;t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r&space;=&space;\frac{r0_{1}&space;&plus;&space;r0_{2}&space;&plus;&space;...&space;r0_{n}}{n}&space;*&space;t" title="r = \frac{r0_{1} + r0_{2} + ... r0_{n}}{n} * t" /></a>


