import numpy as np


def matrixNormalization(data:np.array):
  
    ans = data.astype(float)  # make a float copy
    min_value = ans.min()
    max_value = ans.max()
    # vectorized normalization
    ans = (ans - min_value) / (max_value - min_value)
    return ans
  
  
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

data_3 = np.array ([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])

data_2 = np.array ([
  [1,2],
  [3,3]
])


data_4 = np.array([
  [2,4],
  [6,8]
  ])
# Call your function
result = matrixNormalization(data_4)

print("Original array:")
print(data_3)
print("\nSfited array:")
print(result)
