# 1:
import noshmishmosh
# 2:
import numpy as np

# 3:

# 4:
all_visitors = noshmishmosh.customer_visits
# 5:
paying_visitors = paying_visitors = noshmishmosh.purchasing_customers
# 6:
total_visitor_count  = len(all_visitors)
paying_visitor_count = len(paying_visitors)
#print(total_visitor_count, paying_visitor_count)
# 7:
baseline_percent = 100 * paying_visitor_count / float(total_visitor_count)
# 8:
print("baseline percentage: {}%".format(baseline_percent))
# 9:
payment_history = noshmishmosh.money_spent
#print(payment_history)
# 10:
average_payment = np.mean(payment_history)
#print(average_payment)
# 11:
new_customers_needed = np.ceil(1240 / average_payment)
#print(new_customers_needed)
# 12:
percentage_point_increase = 100 * new_customers_needed / total_visitor_count
#print(percentage_point_increase)
print("percent lift required: {}%".format(percentage_point_increase))
# 13:
minimum_detectable_effect = percentage_point_increase / baseline_percent * 100
# 14:
print("minimum detectable effect: {}%".format(minimum_detectable_effect))
# 15:
print("statistical significance: 90%")
# 16:
ab_sample_size = 290
print("how many people need to be shown the new assets before we can check if the results are a significant improvement?")
print(ab_sample_size)
