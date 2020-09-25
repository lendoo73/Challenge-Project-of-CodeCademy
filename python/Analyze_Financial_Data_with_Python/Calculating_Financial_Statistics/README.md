`display_as_percentage()`: converting a decimal value to the percent form

### Simple Rate of Return
The difference between the starting and ending price of an investment over a time period, divided by the starting price.
If an investment returns dividends, those dividends should be added to the numerator.
#### R = (E - S + D) / S
R: simple rate of return<br />
S: starting price of investment<br />
E: ending price of investment<br />
D: dividend<br />
`calculate_simple_return()`: calculate the simple rate of return
### Logarithmic Rate of Return
Also known as the continuously compounded return.
This is the expected return for an investment where the earnings are assumed to be continually reinvested over the time period.
It is calculated by taking the difference between the log of the ending price and the log of the starting price.
#### r = log(E) - log(S) = log(E / S)
r: logarithmic rate of return
S: starting price of investment
E: ending price of investment
