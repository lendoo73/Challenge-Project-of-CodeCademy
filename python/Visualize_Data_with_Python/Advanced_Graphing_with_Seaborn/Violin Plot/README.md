# [Violin Plots](https://www.codecademy.com/paths/visualize-data-with-python/tracks/advanced-graphing-in-python/modules/seaborn-dvp/lessons/seaborn-distributions/exercises/violin-plots-i)
Violin plots provide more information than box plots because instead of mapping each individual data point, we get an estimation of the dataset thanks to the KDE.

Violin Plots are a powerful graphing tool that allows you to compare multiple distributions at once. It also retains the shape of the distributions.

Violin plots are less familiar and trickier to read:
* There are two **KDE plots** that are symmetrical along the center line.
* A **white dot** represents the median.
* The **thick black line** in the center of each violin represents the interquartile range.
* The **lines that extend from the center** are the confidence intervals - just as we saw on the bar plots, a violin plot also displays the 95% confidence interval.

```
sns.violinplot(
    data = df,     # a list, DataFrame, or array
    x = "label",   # x, y, and hue: a one-dimensional set of data, such as a Series, list, or array
    y = "value"
)
plt.show()
```

![Violin Plot](https://content.codecademy.com/programs/dataviz-python/unit-5/intro-to-seaborn/seaborn_distributions/violin-plot-white.svg)
