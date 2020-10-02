# [Scikit-Learn](https://www.codecademy.com/paths/finance-python/tracks/regression-for-finance/modules/linear-regression-python-finance/lessons/linear-regression/exercises/sklearn)
We can use Python’s scikit-learn library.<br />
Inside the linear_model module, there is a LinearRegression() function we can use:<br />
`from sklearn.linear_model import LinearRegression`<br />
You can first create a `LinearRegression` model, and then fit it to your `x` and `y` data:<br />
`line_fitter = LinearRegression()
line_fitter.fit(X, y)`
The .fit() method gives the model two variables that are useful to us:
1. `line_fitter.coef_`: contains the slope
2. `line_fitter.intercept_`: contains the intercept

We can also use the .predict() function to pass in x-values and receive the y-values that this line would predict:<br />
`y_predicted = line_fitter.predict(X)`
