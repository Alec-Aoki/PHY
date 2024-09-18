import numpy as np

R_1 = np.array([1, 2, 0]).reshape(3, 1)
R_2 = np.array([1, 1, 0]).reshape(3, 1)

print(R_1)
print(R_2)

g = np.eye(3)
#g[0,1] = 0.5
#g[1,0] = 0.5
print(g)

print(R_1.T @ g @ R_2) #como as duas matrizes estão na mesma "direção", precisamos transpor uma delas