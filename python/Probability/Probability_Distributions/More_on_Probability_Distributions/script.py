import scipy.stats as stats

## Practice Question 1
calls = 1 - stats.poisson.cdf(12, 9)
print(calls)


## Practice Question 2
false_backup = stats.poisson.cdf(12, 9) - stats.poisson.cdf(9, 9)
print(false_backup)

## Practice Question 3
expected_serves = 80 * 0.62
print(expected_serves)

## Practice Question 4
variance_serves = expected_serves * (1 - 0.62)
print(variance_serves)

