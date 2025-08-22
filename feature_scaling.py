import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
   standardized_data = np.empty(data.shape)
   normalized_data = np.empty(data.shape)
   
   for i in range(data.shape[1]):
       current_mean = np.mean(data[:, i])
       standardized_data[:, i] = data[:, i] - current_mean
       standardized_data[:, i] = standardized_data[:, i] / np.std(data[:, i])
       
       min_element = np.min(data[:, i])
       max_element = np.max(data[:, i])
       range_element = max_element - min_element
       
       if range_element == 0:
           normalized_data[:, i] = 0.0
       else:
           normalized_data[:, i] = (data[:, i] - min_element) / range_element
                                           
   return standardized_data, normalized_data
