import requests
from bs4 import BeautifulSoup
import pandas as pd

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them"
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()
  
  stats = turtle.find("ul")
  stats_text = stats.get_text("|")
  turtle_data[turtle_name] = stats_text.split("|")

turtle_df = pd.DataFrame.from_dict(turtle_data, orient = "index")

turtle_df = turtle_df.drop(columns = [0, 2, 4, 6, 8, 10])
columns = turtle_df.columns
for col in columns:
  name = str(turtle_df[col].str.split(":")[0][0]).lower()
  val = str(turtle_df[col].str.split(":")[0][1])
  turtle_df = turtle_df.rename(columns = {
    col: name
  })
turtle_df.age = pd.to_numeric(turtle_df.age.str.split(" ").str.get(1))
turtle_df.weight = pd.to_numeric(turtle_df.weight.str.split(" ").str.get(1))
turtle_df.sex = turtle_df.sex.str.split(" ").str.get(1)
turtle_df.breed = turtle_df.breed.str.replace("BREED: ", "")
turtle_df.source = turtle_df.source.str.replace("SOURCE: ", "")
print(turtle_df.iloc[0])
print(turtle_df.iloc[1])

