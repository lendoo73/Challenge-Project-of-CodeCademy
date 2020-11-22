# visualize.py
from tensorflow.keras import Model
from tensorflow import argmax
from tensorflow import expand_dims
from matplotlib import pyplot as plt

#Visualizes convolutional layer activations
def visualize_activations(model, validation_iterator):
    #A keras model that will output our previous model's activations for each convolutional layer:
    activation_extractor = Model(
        inputs = model.inputs, 
        outputs = [layer.output for layer in model.layers if "conv2d" in layer.name]
    )

    #Take matplotlib frame and remove axes.
    def clean_plot(plot):
        plot.axes.get_xaxis().set_visible(False)
        plot.axes.get_yaxis().set_visible(False)

    #Dict mapping from class numbers to string labels:
    class_names = {
        0: "Covid",
        1: "Normal",
        2: "Pneumonia"
    }

    #Loads a sample batch of data
    sample_batch_input, sample_labels = validation_iterator.next()
    
    #Grabs the first five images
    sample_batch_input = sample_batch_input[:5]
    sample_labels = sample_labels[:5]

    #Makes predictions using model.predict(x)
    sample_predictions = model.predict(sample_batch_input)

    #Iterate of images, predictions, and true labels
    for i, (image, prediction, label) in enumerate(zip(sample_batch_input, sample_predictions, sample_labels)):

        image_name = "X_ray{}".format(i)

        #Gets predicted class with highest probability
        predicted_class = argmax(prediction).numpy()

        #Gets correct label
        actual_class = argmax(label).numpy()

        print(image_name)
        print("\tModel prediction: {}".format(prediction))
        print("\tTrue label: {} ({})".format(class_names[actual_class], actual_class))
        print("\tCorrect:", predicted_class == actual_class)

        #Saves image file using matplotlib
        sample_image = image
        clean_plot(plt.imshow(
            sample_image[:, :, 0],
            cmap = "gray"
        ))
        plt.title(image_name + " Predicted: {}, Actual: {}".format(class_names[predicted_class], class_names[actual_class]))
        plt.tight_layout()
        plt.show()
        model_layer_output = activation_extractor(expand_dims(sample_image, 0))
        
        plt.clf()

        #Iterates over each layer output
        for l_num, output_data in enumerate(model_layer_output):
            #Creates a subplot for each filter
            fig, axs = plt.subplots(1, output_data.shape[-1])
            
            #For each filter
            for i in range(output_data.shape[-1]):
                #Plots the filter's activations
                clean_plot(axs[i].imshow(output_data[0][:, :, i], cmap = "gray"))
        
            plt.suptitle(image_name + " Conv {}".format(l_num), y = 0.6)
            plt.tight_layout()
            plt.show()
            plt.clf()
    
def visualize_accuracy(history):
    # plotting categorical and validation accuracy over epochs
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(history.history['categorical_accuracy'])
    ax1.plot(history.history['val_categorical_accuracy'])
    ax1.set_title('model accuracy')
    ax1.set_xlabel('epoch')
    ax1.set_ylabel('accuracy')
    ax1.legend(['train', 'validation'], loc='upper left')

    # plotting auc and validation auc over epochs
    keys = list(history.history.keys())
    #print(keys)
    #print(keys[2])
    #print(keys[-1])
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(history.history[keys[2]])
    ax2.plot(history.history[keys[-1]])
    ax2.set_title('model auc')
    ax2.set_xlabel('epoch')
    ax2.set_ylabel('auc')
    ax2.legend(['train', 'validation'], loc='upper left')

    plt.tight_layout()
    plt.show()
