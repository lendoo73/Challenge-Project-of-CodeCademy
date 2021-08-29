CHOOSING A LINEAR REGRESSION MODEL
R-Squared and the Dangers of Overfitting
Let’s again suppose that we want to use the StreetEasy data to predict rental prices in NYC. We have the following two models that we want to compare:

# Fit model 1
model1 = sm.OLS.from_formula('rent ~ bedrooms + size_sqft + min_to_subway', data=rentals).fit()
 
# Fit model 2
model2 = sm.OLS.from_formula('rent ~ bedrooms + size_sqft + min_to_subway + borough', data=rentals).fit()
 
# Print out R-squared for both models
print(model1.rsquared) # Output: 0.664
print(model2.rsquared) # Output: 0.728
Note that these models both use bedrooms, size_sqft, and min_to_subway as predictors; but model2 uses borough as well. Because all of the predictors in model1 are also contained in model2, these are called nested models.

It turns out that larger nested models will ALWAYS have higher R-squared than their smaller counterparts. However, adding a lot of additional predictors can lead to a different issue: over-fitting. To understand the intuition behind why overfitting is problematic, consider the following plot of rental prices vs. number of bathrooms. We can perfectly predict each datapoint if we fit the zig-zagging line shown below:

plot showing rent vs. bedrooms for 9 apartments. The points are all connected by a zig-zagging dotted line.

However, imagine that we collect a new sample of apartments in NYC and record the number of bathrooms in each. Then, suppose we want to use our model to predict rental prices. Even if the overall relationship between bathrooms and rent is the same in our new data, the exact values will be slightly different. Predictions based on the zig-zag line may be less accurate because the model was so heavily influenced by the quirks of the data we originally collected. A straight line through the middle of the points is actually more useful.
