import pprint
# from model import fit_model
# from visualize import plot_accuracy, plot_heatmap
# from report import class_names

learning_rate = 0.0001
# Too many epochs can lead to overfitting, and too few to underfitting. 
num_epochs = 100
batch_size = 4096

history, features_test, labels_test = fit_model(learning_rate, num_epochs, batch_size)
#pprint.pprint(history.__dict__)
#pprint.pprint(history.model.__dict__)

plot_accuracy(history)

y_pred = report(history.model, features_test, labels_test)

plot_heatmap(class_names, y_pred, labels_test)
