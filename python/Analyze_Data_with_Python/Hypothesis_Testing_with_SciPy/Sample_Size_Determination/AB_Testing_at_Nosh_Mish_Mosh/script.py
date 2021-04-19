# Nosh Mish Mosh: An Assortment of Edible Aliments
# 1.:
import noshmishmosh
# 2.:
import numpy as np

# A/B Testing at Nosh Mish Mosh
# 3-4.:
all_visitors = noshmishmosh.customer_visits

# 5.:
paying_visitors = noshmishmosh.purchasing_customers

# 6.:
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

# 7. get the baseline:
baseline_percent = paying_visitor_count / total_visitor_count * 100
print(f"baseline: {baseline_percent}%")

# Mish Mosh B'Gosh: The Effect Size
# 9.:
payment_history = noshmishmosh.money_spent

# 10.:
average_payment = np.mean(payment_history)

# 11.:
new_customers_needed = int(np.ceil(1240 / average_payment))

# 12.:
percentage_point_increase = new_customers_needed / total_visitor_count * 100
print(f"additional percent of weekly visitors: {percentage_point_increase}%")

# 13. find our minimum detectable effect/desired lift:
mde = percentage_point_increase / baseline_percent * 100
# 14.:
print(f"minimum detectable effect/desired lift: {mde}")

# Nosh Mish Mosh: Tying It All Together
# 15.:
significance_threshold = 10

# 16.:
ab_sample_size = 490
