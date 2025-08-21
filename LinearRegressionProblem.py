import numpy as np
from numpy.typing import NDArray




class Solution:
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        
        result = np.zeros((X.shape[0], weights.shape[1]))
              
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                result[i, 0] += X[i, j] * weights[j, 0]
          
        return np.round(result, 5)
        
        
    def get_model_prediction_2(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is Nx3, weights is 3x1
        # Use matrix multiplication
        result = np.matmul(X, weights)  # shape will be Nx1
        return np.round(result, 5)   
        
     def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # model_prediction is an Nx1 NumPy array
        # ground_truth is an Nx1 NumPy array
        # HINT: np.mean(), np.square() will be useful
        # return round(your_answer, 5)

        error_result = np.mean(np.square(model_prediction - ground_truth))
        return np.round(error_result, 5)


    # Sample data
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
], dtype=float)

weights = np.array([
    [0.1],
    [0.2],
    [0.3]
], dtype=float)

# Create solution object and predict
sol = Solution()
y_pred = sol.get_model_prediction(X, weights)
y_pred_2 = sol.get_model_prediction_2(X, weights)
print("Predicted y:\n", y_pred)
print("Predicted y:\n", y_pred_2)
