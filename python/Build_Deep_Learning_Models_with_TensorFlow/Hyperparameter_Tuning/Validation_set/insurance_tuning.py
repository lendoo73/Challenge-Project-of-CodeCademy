#see model.py file for more details
from model import design_model, features_train, labels_train 

model = design_model(
  features_train, 
  learning_rate = 0.01
)
#your code here
model.fit(
  features_train, 
  labels_train, 
  epochs = 40, 
  batch_size = 8, 
  verbose = 1, 
  validation_split = 0.33
)
