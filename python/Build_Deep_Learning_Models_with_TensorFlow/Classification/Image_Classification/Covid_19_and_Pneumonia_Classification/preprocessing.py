# preprocessing.py
def create_iterator(data_generator, directory, batch_size):
  
    return data_generator.flow_from_directory(
        directory,
        class_mode = "categorical",
        color_mode = "grayscale",
        batch_size = batch_size
    )