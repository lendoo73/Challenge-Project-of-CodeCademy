import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
# 1:
#print(ad_clicks.head())

# 2:
count_utm_source = ad_clicks.groupby("utm_source").user_id.count().reset_index()
#print(count_utm_source)

# 3:
ad_clicks["is_click"] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks.head())

# 4:
clicks_by_source = ad_clicks.groupby(["utm_source", "is_click"]).user_id.count().reset_index()
#print(clicks_by_source)
# 5:
clicks_pivot = clicks_by_source.pivot(
  columns = "is_click",
  index = "utm_source",
  values = "user_id"
).reset_index()
#print(clicks_pivot)
# 6:  
clicks_pivot["percent_clicked"] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
#print(clicks_pivot)
# 7:
both_adds = ad_clicks.groupby("experimental_group").user_id.count().reset_index()
#print(both_adds)
# 8:
clicked_A_B = ad_clicks.groupby(["experimental_group", "is_click"]).user_id.count().reset_index().pivot(
  columns = "is_click",
  index = "experimental_group",
  values = "user_id"
).reset_index()
#print(clicked_A_B)
# 9:
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
#print(a_clicks)
#print(b_clicks)
# 10:
# a:
a_clicked_by_day = a_clicks.groupby(["is_click", "day"]).user_id.count().reset_index().pivot(
  columns = "is_click",
  index = "day",
  values = "user_id"
).reset_index()
a_clicked_by_day["percent_clicked"] = a_clicked_by_day[True] / a_clicked_by_day[True] + a_clicked_by_day[False]
print(a_clicked_by_day)

# b:
b_clicked_by_day = b_clicks.groupby(["is_click", "day"]).user_id.count().reset_index().pivot(
  columns = "is_click",
  index = "day",
  values = "user_id"
).reset_index()
b_clicked_by_day["percent_clicked"] = b_clicked_by_day[True] / b_clicked_by_day[True] + b_clicked_by_day[False]
print(b_clicked_by_day)


