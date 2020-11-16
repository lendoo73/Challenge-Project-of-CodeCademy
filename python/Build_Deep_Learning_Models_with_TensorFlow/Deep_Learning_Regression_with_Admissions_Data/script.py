from model import fit_model
from plotting import plot

learning_rate = 0.01
num_epochs = 1000
history = fit_model(num_epochs)

for property, value in vars(history).items():
    #print(property, ":", value)
    pass

val_mse, val_mae = history.model.evaluate(
    features_test, 
    labels_test, 
    verbose = 0
)

print("MAE: ", val_mae)

#print(history.history.keys())
plot(history)