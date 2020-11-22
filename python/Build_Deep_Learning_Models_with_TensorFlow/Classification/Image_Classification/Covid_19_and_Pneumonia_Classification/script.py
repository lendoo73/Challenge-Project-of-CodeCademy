# script.py
from model import fit_model
from visualize import visualize_activations, visualize_accuracy
from report import report
import pprint

BATCH_SIZE = 16
LEARNING_RATE = 0.005
EPOCHS = 20

history, validation_iterator = fit_model(BATCH_SIZE, LEARNING_RATE, EPOCHS)
model = history.model

visualize_activations(model, validation_iterator)

visualize_accuracy(history)

#pprint.pprint(history.__dict__)
#pprint.pprint(history.model.__dict__)
#print("validation_iterator")
#pprint.pprint(validation_iterator.__dict__)

report(model, validation_iterator)