import matplotlib.pyplot as plt

def plot(history):
    fig = plt.figure(figsize = (15,10))
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(history.history['mae'])
    ax1.plot(history.history['val_mae'])
    ax1.set_title('model mae')
    ax1.set_ylabel('MAE')
    ax1.set_xlabel('epoch')
    ax1.legend(['train', 'validation'], loc='upper left')

    # Plot loss and val_loss over each epoch
    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(history.history['loss'])
    ax2.plot(history.history['val_loss'])
    ax2.set_title('model loss')
    ax2.set_ylabel('loss')
    ax2.set_xlabel('epoch')
    ax2.legend(['train', 'validation'], loc='upper left')

    # used to keep plots from overlapping each other  
    fig.tight_layout()
    
    plt.show()