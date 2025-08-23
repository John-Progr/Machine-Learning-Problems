import numpy as np

def rowScaling(data: np.array):
  
  ans = np.empty(data.shape)
  
  for i in range(data.shape[0]):
    sum_of_elements = np.sum(data[i])
    
    ans[i] = data[i] / sum_of_elements
  
  
  return ans 
  
  
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

data_2 = np.array ([
  [1,2],
  [3,3]
])
# Call your function
result = rowScaling(data_2)

print("Original array:")
print(data_2)
print("\nRow-scaled array:")
print(result)
