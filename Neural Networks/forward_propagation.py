import numpy as np

def dense(a_in, W, b, g):
    units = W.shape()
    a_out = np.zeros(units)
    for j in range(units):
        w = W[:, j]
        z = np.dot(w, a_in) + b[j]
        a_out[j] = g(z)
    return a_out

# W's and b's are unique to the specific data and model.
# For simplicity, we set them to 1, 2, 3, 4.
W1, W2, W3, W4 = 1, 2, 3, 4
b1, b2, b3, b4 = 1, 2, 3, 4

def sequential(x):
    a1 = dense(x, W1, b1)
    a2 = dense(a1, W2, b2)
    a3 = dense(a2, W3, b3)
    a4 = dense(a3, W4, b4)
    f_x = a4
    return f_x

def dense(a_in, W, b, g):
    z = np.matmul(a_in, W) + b
    a_out = g(z)
    return a_out