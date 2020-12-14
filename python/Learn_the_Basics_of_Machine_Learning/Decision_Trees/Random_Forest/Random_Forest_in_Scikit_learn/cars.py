import random
random.seed(1)

def make_cars():
    f = open("car.data", "r")
    cars = []
    for line in f:
        cars.append(line.rstrip().split(","))
    return cars
  
def change_data(data):
    dicts = [{'vhigh' : 1.0, 'high' : 2.0, 'med' : 3.0, 'low' : 4.0},
    {'vhigh' : 1.0, 'high' : 2.0, 'med' : 3.0, 'low' : 4.0},
    {'2' : 1.0, '3' : 2.0, '4' : 3.0, '5more' : 4.0},
    {'2' : 1.0, '4' : 2.0, 'more' : 3.0},
    {'small' : 1.0, 'med' : 2.0, 'big' : 3.0},
    {'low' : 1.0, 'med' : 2.0, 'high' : 3.0}]

    for row in data:
        for i in range(len(dicts)):
            row[i] = dicts[i][row[i]]

    return data
  
cars = change_data(make_cars())
random.shuffle(cars)
car_data = [x[:-1] for x in cars]
car_labels = [x[-1] for x in cars]

training_points = car_data[:int(len(car_data)*0.9)]
training_labels = car_labels[:int(len(car_labels)*0.9)]

testing_points = car_data[int(len(car_data)*0.9):]
testing_labels = car_labels[int(len(car_labels)*0.9):]
