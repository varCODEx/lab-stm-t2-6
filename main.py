from gauss_method import gauss_method, gauss_method_linalg
from tridiagonal_mx_algorithm import tridiagonal_mx_algorithm
from seidel_method import seidel_method
from jacobi_method import jacobi_method

from numpy import linalg, array


### #12 - Override this

# 6.1
A = [[-1, -8, 0, 5],
     [6, -6, 2, 4],
     [9, -5, -6, 4],
     [-5, 0, -9, 1, ]]

b = [60, -10, 65, 18]

# 6.2

A_ = [[-11, 9, 0, 0, 0],
      [1, -8, 1, 0, 0],
      [0, -2, -11, 5, 0],
      [0, 0, 3, -14, 7],
      [0, 0, 0, 8, 10]]

b_ = [-114, 81, -8, -38, 144]

# 6.3

A__ = [[14, -4, -2, 3],
       [-3, 23, -6, -9],
       [-7, -8, 21, -5],
       [-2, -2, 8, 18], ]

b__ = [38, -195, -27, 142]

eps = 0.01

###
def printm(A):
    for r in A:
        print(r)

print("gauss m-d")
print(gauss_method(A, b))
print(f"gauss m-d determinant:  {gauss_method_linalg(A,return_determinant=True)}")
print(f"numpy determinant:  {linalg.det(array(A))}")
print()
print("gauss m-d inverse matrix")
printm(gauss_method_linalg(A,return_determinant=False))
print()

print("gauss m-d")
print(gauss_method(A_, b_))
print("tridiagonal mx alg-m")
print(tridiagonal_mx_algorithm(A_, b_))
print()

print("gauss m-d")
print(gauss_method(A__, b__))
print("jacobi m-d")
print(jacobi_method(A__, b__, eps))
print("seidel m-d")
print(seidel_method(A__, b__, eps))
