CHOOSING A LINEAR REGRESSION MODEL
R-Squared
R-squared is one of the most common metrics to evaluate linear regression models. We can interpret R-squared as the proportion of variation in an outcome variable that is explained by a linear regression model. More explained variation is generally better.

For example, suppose we have a dataset containing information about apartment rentals for NYC apartments. We can build two different models to predict rental price and print out the R-Squared for each model as follows:

# Create and fit the first model to predict rent
model1 = sm.OLS.from_formula('rent ~ bedrooms + size_sqft + min_to_subway', data=rentals).fit()
 
# Create and fit the second model
model2 = sm.OLS.from_formula('rent ~ bathrooms + building_age_yrs + borough', data=rentals).fit()
 
# Print out R-squared for both models
print(model1.rsquared) #Output: 0.664
print(model2.rsquared) #Output: 0.596
This tells us that the first model (using bedrooms, square-footage, and minutes to the subway) explains about 66.4% of the variation in rental prices, whereas the second model only explains about 59.6% of the variation. This would lead us to choose the first model over the second.
