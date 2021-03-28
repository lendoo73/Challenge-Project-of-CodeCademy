import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
# 2:
wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
steel = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
#print(wood)
#print(steel)

# write function to plot rankings over time for 1 roller coaster here:
# 3:
def plot_roller_coaster(name, park, df):
  coaster_ranking = df[(df.Name == name) & (df.Park == park)]
  ax = plt.subplot()
  ax.plot(coaster_ranking["Year of Rank"], coaster_ranking["Rank"])
  ax.set_xticks(coaster_ranking["Year of Rank"].values)
  ax.set_yticks(coaster_ranking["Rank"].values)
  ax.invert_yaxis()
  plt.xlabel("Year")
  plt.ylabel("Ranking")
  plt.title("{} Rankings".format(name))
  plt.show()

#plot_roller_coaster("El Toro", "Six Flags Great Adventure", wood)
plt.clf()

# 4:
# write function to plot rankings over time for 2 roller coasters here:
def double_plot_roller_coaster(name1, name2, park1, park2, df):
  coaster_ranking1 = df[(df.Name == name1) & (df.Park == park1)]
  coaster_ranking2 = df[(df.Name == name2) & (df.Park == park2)]
  ax = plt.subplot()
  ax.plot(coaster_ranking1["Year of Rank"], coaster_ranking1["Rank"])
  ax.plot(coaster_ranking2["Year of Rank"], coaster_ranking2["Rank"])
  plt.legend([name1, name2])
  plt.xlabel("Year")
  plt.ylabel("Ranking")
  ax.set_xticks(coaster_ranking2["Year of Rank"].values)
  ax.set_yticks(coaster_ranking2["Rank"].values)
  ax.invert_yaxis()
  plt.title("Rankings: {} Vs. {}".format(name1, name2))
  plt.show()

#double_plot_roller_coaster("El Toro", "Boulder Dash", "Six Flags Great Adventure", "Lake Compounce",  wood)
plt.clf()

# 5:
# write function to plot top n rankings over time here:
def top_n_roller_coaster(rank, df):
  top_n_rankings = df[df.Rank <= rank]
  ax = plt.subplot()
  for coaster in set(top_n_rankings['Name']):
    coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
    ax.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'], label=coaster, marker = "s")
  plt.legend()
  plt.xlabel("Year")
  plt.ylabel("Ranking")
  ax.set_xticks(top_n_rankings["Year of Rank"].values)
  ax.set_yticks(top_n_rankings["Rank"].values)
  ax.invert_yaxis()
  material = "wood" if df.iloc[0].Name == "Boulder Dash" else "steel"
  plt.title("Top {} Roller Coaster Rankings: {}".format(rank, material))
  plt.show()

#top_n_roller_coaster(5, wood)
#top_n_roller_coaster(5, steel)

plt.clf()
# load roller coaster data here:
captain_df = pd.read_csv("roller_coasters.csv")
#print(captain_df)

# 7:
# write function to plot histogram of column values here:
def plot_histogram(df, col):
  # check if dataframe column exists:
  if col not in df:
    return print("Column {} not exists.".format(col))
  # check if the value of columns is a number:
  type_of_value = type(df.iloc[0][col])
  if (type_of_value == str):
    return print("Invalid type of data")
  # the given column is valid, create histogram:
  if col == "height":
    data = df[df[col].values <= 140]
  else:
    data = df[df[col].values > 0]
    
  plt.xlabel(col)
  plt.ylabel("Number of Roller Coaster")
  plt.hist(data[col], bins = 20)
  #plt.hist(df[col].dropna(), bins = 20)
  plt.show()

#plot_histogram(captain_df, "height")

plt.clf()

# 8:
# write function to plot inversions by coaster at a park here:
def num_of_inversion(df, park_name):
  park_coasters = df[df.park == park_name]
  coaster_names = park_coasters.name
  number_inversions = park_coasters.num_inversions
  ax = plt.subplot()
  ax.set_xticks(range(len(coaster_names)))
  ax.set_xticklabels(coaster_names, rotation = "vertical")
  plt.ylabel("Inversions")
  plt.bar(range(len(coaster_names)), number_inversions)
  plt.show()

#num_of_inversion(captain_df, "Parc Asterix")

plt.clf()

# 9:
# write function to plot pie chart of operating status here:
def number_of_operating_rc(df):
  operating_coasters = len(df[df['status'] == 'status.operating'])
  closed_coasters = len(df[df['status'] == 'status.closed.definitely'])
  plt.pie([operating_coasters, closed_coasters], autopct = "%0.1f%%")
  plt.axis("equal")
  plt.legend(["Operating", "Closed"])
  plt.title("Status")
  plt.show()

#number_of_operating_rc(captain_df)

plt.clf()

# 10:
# write function to create scatter plot of any two numeric columns here:
def create_scatterplot(df, col1, col2):
  # check if dataframe column exists:
  compare = [col1, col2]
  for col in compare:
    if col not in df:
      return print("Column {} not exists.".format(col))
    # check if the value of columns is a number:
    type_of_value = type(df.iloc[0][col])
    if (type_of_value == str):
      return print("Invalid type of data")
  # the given column is valid, create scatterplot:
  if col1 == "height":
    data = df[df.height.values <= 140]
  else:
    data = df[df[col1].values > 0]
  if col2 == "height":
    data = data[data.height.values <= 140]
  else:
    data = df[df[col2].values > 0]
  
  ax = plt.subplot()
  ax.scatter(data[col1], data[col2], alpha = 0.3)
  plt.xlabel(col1)
  plt.ylabel(col2)
  plt.title("{} vs. {}:".format(col1.capitalize(), col2.capitalize()))
  plt.show()

#create_scatterplot(captain_df, "speed", "height")
plt.clf()

# 11:
seating_types = captain_df.groupby("seating_type").name.count().reset_index().rename(columns = {"name": "Count"}).sort_values(by = ["Count"], ascending = False)
print(seating_types)
count = seating_types[seating_types.Count > 0]
print(count)
ax = plt.subplot()
ax.set_xticks(range(len(seating_types)))
ax.set_xticklabels(seating_types.seating_type, rotation = "vertical")
plt.bar(range(len(seating_types)), seating_types.Count)
plt.title("What roller coaster seating type is most popular?")
plt.show()
print(seating_types.iloc[0].seating_type + " seating type is the most popular.")
