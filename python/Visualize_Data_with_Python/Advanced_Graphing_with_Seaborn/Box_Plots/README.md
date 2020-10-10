# [Box Plots](https://www.codecademy.com/paths/visualize-data-with-python/tracks/advanced-graphing-in-python/modules/seaborn-dvp/lessons/seaborn-distributions/exercises/box-plots-i)
The box plot (also known as a box-and-whisker plot) can’t tell us about how our dataset is distributed, like a KDE plot. But it shows us the range of our dataset, gives us an idea about where a significant portion of our data lies, and whether or not any outliers are present.

Let’s examine how we interpret a box plot:
* The **box** represents the interquartile range
* The **line in the middle** of the box is the median
* The **end lines** are the first and third quartiles
* The **diamonds** show outliers

![Box Plot](https://content.codecademy.com/courses/updated_images/box-plot-white_Updated_1.svg)

```
sns.boxplot(
    data=df,      # the dataset we’re plotting, like a DataFrame, list, or an array
    x = 'label',  # a one-dimensional set of values, like a Series, list, or array
    y='value'     # a second set of one-dimensional data
)
plt.show()
```

If you use a Pandas Series for the x and y values, the Series will also generate the axis labels. 
