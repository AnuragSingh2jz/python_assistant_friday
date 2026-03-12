# import numpy as np
# A = np.array([[2,3,-1], [4,1,2],[3,-2,1]], dtype = float)

# b = np.array([5,6,4], dtype = float)

# #Convert to symoy matrix and augment
# import sympy as sp
# aug = sp.Matrix(np.hstack((A,b.reshape(-1,1))))
# #Reduce to RREF
# rref_matrix , _ = aug.rref()
# print("RREFform:\n", rref_matrix)
# #Extract Solution
# solution = [rref_matrix[i,-1] for i in range(rref_matrix.rows)]
# print("Solution:", solution)

import numpy as np
A = np.array([[1,1,1], [4,3,-1],[3,5,3]], dtype = float)

b = np.array([1,6,4], dtype = float)

#Convert to symoy matrix and augment
import sympy as sp
aug = sp.Matrix(np.hstack((A,b.reshape(-1,1))))
#Reduce to RREF
rref_matrix , _ = aug.rref()
print("RREFform:\n", rref_matrix)
#Extract Solution
solution = [rref_matrix[i,-1] for i in range(rref_matrix.rows)]
print("Solution:", solution)