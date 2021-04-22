from gauss_method import gauss_method


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


###


print(gauss_method(A, b))
