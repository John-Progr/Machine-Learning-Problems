import numpy as np

def to_categorical(x, n_col=None):

    shape = (0, 0)
    if n_col != None:
        shape = (len(x), n_col)
        print("Column is set")
    else:
        shape = (len(x), np.max(x) + 1)
        print("Column is none")
        print(shape)

    ans = np.zeros(shape)

    for i in range(len(x)):
        ans[i, x[i]] = 1  # kept your original +1 indexing


    return ans
    
	
	
	
	
x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)

print(output)
