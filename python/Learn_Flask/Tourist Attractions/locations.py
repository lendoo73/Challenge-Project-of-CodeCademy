import csv

class Locations:
    def __init__(self):
        self.locations = []
        self.load_data()

    def add(self, name, description, category):
        if name is not None and description is not None and category is not None:
            location = Location(name, description, category)
            self.locations.append(location)

    def get_index_by_name(self, name):
        for i, location in enumerate(self.locations):
            if location.name == name:
                return i

    def get_list_by_category(self, category):
        locs = []
        for i, location in enumerate(self.locations):
            if location.category == category:
                locs.append(location)
        return locs

    def delete(self, name):
        i = self.get_index_by_name(name)
        self.locations.pop(i)

    def moveup(self, name):
        i = self.get_index_by_name(name)
        if self.locations[i].category == "recommended":
            self.locations[i].category = "tovisit"
        elif self.locations[i].category == "tovisit":
            self.locations[i].category = "visited"

    def load_data(self):
        with open("data.csv", "r") as csvfile:
            locations = csv.reader(csvfile)
            for row in locations:
                self.add(row[0], row[1], row[2])

    def __repr__(self):
        for location in self.locations:
            print(f'{location.name} - {location.description} - {location.category}')


class Location:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    

    