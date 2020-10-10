# [KDE Plots](https://www.codecademy.com/paths/visualize-data-with-python/tracks/advanced-graphing-in-python/modules/seaborn-dvp/lessons/seaborn-distributions/exercises/kde-plots-ii)
Kernel Density Estimator

A KDE plot gives us the sense of a univariate as a curve. A univariate dataset only has one variable and is also referred to as being one-dimensional, as opposed to bivariate or two-dimensional datasets which have two variables.

A KDE plot takes the following arguments:
* `data`: a Pandas DataFrame, Python list, or NumPy array
* `shade`: a boolean that determines whether or not the space underneath the curve is shaded

When using a KDE we need to plot each of the original datasets separately:

```
sns.kdeplot(dataset1, shade = True)
sns.kdeplot(dataset2, shade=True)
sns.kdeplot(dataset3, shade=True)
plt.legend()
plt.show()
```
