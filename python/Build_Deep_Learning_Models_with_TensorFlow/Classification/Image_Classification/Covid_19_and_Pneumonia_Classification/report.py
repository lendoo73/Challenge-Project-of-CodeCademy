# report.py
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def report(model, validation_iterator):
    test_steps_per_epoch = np.math.ceil(validation_iterator.samples / validation_iterator.batch_size)
    predictions = model.predict(validation_iterator, steps = test_steps_per_epoch)
    predicted_classes = np.argmax(predictions, axis = 1)
    true_classes = validation_iterator.classes
    class_labels = list(validation_iterator.class_indices.keys())
    report = classification_report(true_classes, predicted_classes, target_names = class_labels)
    
    print(report)

    cm = confusion_matrix(true_classes, predicted_classes)
    print(cm)