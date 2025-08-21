import numpy as np
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import pandas as pd
import numpy as np

def matrixTransform(matrix):
     print("First row: ", matrix[0])
     print("First column: ", matrix[:, 0])
     print("Top-left element: ", matrix[0][0])
     
     matrix[:, 0] = matrix[:, 0] * 10
     
     print("First Column: ", matrix[:, 0])
     

my_matrix = np.array([ [1,2,3],
                      [4,5,6],
                      [7,8,9] ])


matrixTransform(my_matrix)


def editMatrix(X):
    import numpy as np
    ans = np.zeros(X.shape)
    for j in range(X.shape[1]):
        # center mean
        ans[:, j] = X[:, j] - np.mean(X[:, j])
        
        current_std = np.std(ans[:, j], ddof=0)
        target_std = (j+1) ** 4
        
        scale = target_std / current_std
        ans[:, j] = scale * ans[:, j]
        
        target_mean = (j+1)
        ans[:, j] += target_mean
        
    return ans
    
    
A = np.array ([ [3,5],
                [5,14] ])
       
B = editMatrix(A)


print(B)
