from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 2.:
webpage = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')

# 3.:
soup = BeautifulSoup(webpage.content, "html.parser")

# 4.:
#print(soup)

# 5.:
rating_list = soup.find_all(
  attrs = {
    "class": "Rating"
  }
)

# 6-7.:
ratings = [float(val.get_text()) for val in rating_list[1:]]
#print(ratings)

# 8.:
plt.hist(ratings)
plt.title("Ratings")
plt.show()
plt.clf()

# 9-11.:
companies = [company.get_text() for company in soup.select(".Company")[1:]]
#print(companies)

# 12.:
df = pd.DataFrame.from_dict({
  "company": companies,
  "rating": ratings
})
#print(df.head())

# 13.:
avg_ratings = df.groupby("company").rating.mean()
#print(avg_ratings)

best_of_10 = avg_ratings.nlargest(10)
#print(best_of_10) CocoaPercent

# 14.:
cocoa_percentages = [int(float(company.get_text().strip("%"))) for company in soup.select(".CocoaPercent")[1:]]
#print(cocoa_percentages)

# 15.:
df["CocoaPercentage"] = cocoa_percentages
#print(df)

# 16.:
plt.scatter(df.CocoaPercentage, df.rating)
z = np.polyfit(df.CocoaPercentage, df.rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()
plt.clf()

# 18.:
# Where are the best cocoa beans grown?
"Origin", "BroadBeanOrigin"
origin= [company.get_text() for company in soup.select(".Origin")[1:]]
broadBeanOrigin= [company.get_text() for company in soup.select(".BroadBeanOrigin")[1:]]
df["origin"] = origin
df["broadBeanOrigin"] = broadBeanOrigin
best_one = df[df.rating >= df.rating.max()]
print(f"The best cocoa beans grown in {best_one.origin.iloc[0]}, {best_one.broadBeanOrigin.iloc[0]}.")

# Which countries produce the highest-rated bars?
company_location = [company.get_text() for company in soup.select(".CompanyLocation")[1:]]
df["company_location"] = company_location
best_one = df[df.rating >= df.rating.max()]
countries = best_one.company_location
print(f"The highest rated chocolate bars produceds in {next(iter(set(countries)))}. ")

