from warnings import warn


def subtract_row(r1, r2):
    return [r1[i] - r2[i] for i in range(len(r1))]


# return xs from upper-triangular matrix backward substitution
def backward_substitution(A, b):
    x = [None for i in range(len(A))]
    for i in reversed(range(len(A))):
        subtrahend = 0
        for j in range(i, len(A) - 1):
            subtrahend += x[j + 1] * A[i][j + 1]
        x[i] = (b[i] - subtrahend) / A[i][i]

    return x


def gauss_method(A, b):
    n = len(A)

    # M = [M|b]
    M = [None for i in range(n)]
    for i in range(n):
        M[i] = [l for l in A[i]] + [b[i]]

    for i in range(n):

        if M[i][i] == 0:
            # pivot around the biggest (absolute) element in a row
            M[i:] = sorted(M[i:], reverse=True, key=lambda row: abs(row[i]))
            if M[i][i] == 0:
                # if all elements below the diagonal are also zero, the matrix is singular
                warn("The result of the gauss method is indecisive (either no or infinite solutions)")
                return [None for i in range(n)]

        for j in range(i + 1, n):
            M[j] = subtract_row(M[j], [elem * (M[j][i] / M[i][i]) for elem in M[i]])

    # A_, b_ from [A|b]
    A_ = [el[:-1] for el in M]
    b_ = [el[-1] for el in M]

    return backward_substitution(A_, b_)
