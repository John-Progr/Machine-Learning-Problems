import numpy as np


def columnShiftIndex(data:np.array):
  
  ans = np.copy(data)
  
  for i in range(data.shape[1]):
    ans[:, i] =  np.roll(ans[:, i], shift = i, axis = 0)
    
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
# Call your function
result = columnShiftIndex(data_3)

print("Original array:")
print(data_3)
print("\nSfited array:")
print(result)
