import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create a dummy dataset with numeric and categorical columns
X = pd.DataFrame({
    "Age": [25, 30, 22, 28, 35],
    "Income": [50000, 60000, 45000, 52000, 70000],
    "Gender": ["Male", "Female", "Female", "Male", "Female"],
    "Region": ["North", "South", "East", "West", "North"]
})

# Create a dummy target column (numeric)
y = np.array([[1], [0], [1], [0], [1]])

# Define function to compute MSE using linear regression
def linearRegressionMSE(X, y):
    # Initialize OneHotEncoder for categorical variables
    enc = OneHotEncoder()
    
    # Store number of columns and rows in X
    ncols = X.shape[1]
    nrows = X.shape[0]
    
    # Loop through each column of the dataframe
    for idx, col in enumerate(X.columns):
        # Check if the column is categorical (dtype object)
        if X[col].dtype == object:
            # Get unique values and integer indices for categories
            unique, unique_inverse = np.unique(X[col], return_inverse=True)
            
            # Reshape the indices into a column vector
            unique_inverse = unique_inverse.reshape(len(unique_inverse), 1)
            
            # One-hot encode the categorical indices
            bits = enc.fit_transform(unique_inverse).toarray()
            
            # Drop the last column to get N-1 dummies
            bits = bits[:, :bits.shape[1]-1]
            print(f"Column '{col}' one-hot encoded (N-1 dummies):\n", bits)
            
            # If first column, initialize preds, else concatenate
            if idx == 0:
                preds = bits
            else:
                preds = np.concatenate((preds, bits), axis=1)
        else:
            # For numeric columns, reshape as a column vector
            col_values = X[col].values.reshape(nrows, 1)
            print(f"Column '{col}' numeric values:\n", col_values)
            
            # If first column, initialize preds, else concatenate
            if idx == 0:
                preds = col_values
            else:
                preds = np.concatenate((preds, col_values), axis=1)
    
    # Print the final feature matrix after combining all columns
    print("\nFinal feature matrix (preds):\n", preds)
    
    # Initialize Linear Regression model
    LR = LinearRegression()
    
    # Fit model to feature matrix and target
    LR.fit(preds, y)
    
    # Predict target values using the trained model
    y_pred = LR.predict(preds)
    print("\nPredicted y:\n", y_pred)
    
    # Compute Mean Squared Error between true and predicted values
    mse = mean_squared_error(y, y_pred)
    print("\nMean Squared Error:", mse)
    
    # Return MSE
    return mse

# Test the function with our dataset
linearRegressionMSE(X, y)
