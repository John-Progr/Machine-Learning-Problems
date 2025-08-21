import numpy as np



def model_fit_quality(training_accuracy, test_accuracy):
  
  fit = 0
  
  if(training_accuracy - test_accuracy > 0.2):
    fit = 1
  elif(training_accuracy < 0.7 and test_accuracy < 0.7):
    fit = -1
  
  return fit
  
  
fit = model_fit_quality (0.8,0.8)

print(fit)
