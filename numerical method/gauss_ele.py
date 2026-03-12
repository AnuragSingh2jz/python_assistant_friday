# solve (A,B) means it solve AX = B
# import numpy as np
# # coff of matrix
# A = np.array([[1,1], [2,3]], dtype = float)

# # Right hand side
# b=np.array([5,13], dtype=float)
# # Gauss Elimination using numpy
# x = np.linalg.solve(A,b)
# print("Solution:", x)







import numpy as np
# coff of matrix
A = np.array([[2,3,-1], [4,1,2], [3,-2,1]], dtype = float)

# Right hand side
b=np.array([5,6,4], dtype=float)
# Gauss Elimination using numpy
x = np.linalg.solve(A,b)
print("Solution:", x)




# import numpy as np
# # coff of matrix
# A = np.array([[1,1,1,1], [2,-1,3,2], [3,2,-1,1], [4,-1,2,3]], dtype = float)

# # Right hand side
# b=np.array([10,15,10,20], dtype=float)
# # Gauss Elimination using numpy
# x = np.linalg.solve(A,b)
# print("Solution:", x)