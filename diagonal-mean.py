import numpy as np

def diagonalRowMean(data: np.array):
  
  ans = np.copy(data).astype(float)
  means = []
  for i in range (data.shape[0]):
    mean_of_elements = np.mean(data[i])
    means.append(mean_of_elements)
    

  np.fill_diagonal(ans, means)
  
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
result = diagonalRowMean(data)

print("Original array:")
print(data)
print("\nRow-scaled array:")
print(result)
