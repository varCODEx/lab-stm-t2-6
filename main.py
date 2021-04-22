from gauss_method import gauss_method
from tridiagonal_mx_algorithm import tridiagonal_mx_algorithm


def printm(a):
    for row in a:
        print(row)
    print()


### #12 - Override this

# 6.1
A = [[-1, -8, 0, 5],
     [6, -6, 2, 4],
     [9, -5, -6, 4],
     [-5, 0, -9, 1,]]

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
      [-2, -2, 8, 18],]

b__ = [38, -195, -27, 142]


###


print(gauss_method(A, b))
print()

print(gauss_method(A_, b_))
print(tridiagonal_mx_algorithm(A_, b_))
