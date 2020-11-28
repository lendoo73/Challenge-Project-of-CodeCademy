from sklearn.metrics import classification_report
import numpy as np

class_names = ['Spruce/Fir', 'Lodgepole Pine',
                   'Ponderosa Pine', 'Cottonwood/Willow',
                   'Aspen', 'Douglas-fir', 'Krummholz']

def report(model, features_test, labels_test):
    score = model.evaluate(features_test, labels_test, verbose = 0)
    print(f'Test loss: {score[0]}')
    print(f'Test accuracy: {score[1]}')

    # evaluating the model:
    y_pred = model.predict(features_test)
    # Convert the pred to discrete values
    y_pred = np.argmax(y_pred, axis=1)
    print(classification_report(labels_test, y_pred, target_names = class_names))

    return y_pred
