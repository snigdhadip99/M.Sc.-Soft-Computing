import numpy as np
W = np.array([[0.25, 0.12, 0.13], [0.24, 0.14, 0.25], [0.19, 0.17, 0.33], [0.21, 0.17, 0.22]]) #Weight values
I = np.array([[5, 3, 7, 4], [2, 1, 7, 3]]) #Input values
B = np.array([0.5, 0.5, 0.5]) #Bias values
O = (I @ W) + B #Finding the outputs
for i, o in zip(I,O):
    print("The output for input vector ", i, " is below\n", o)