import numpy as np
def jacobi_method(A, b, eps):
    global x, i
    x = np.zeros_like(b)
    for it_count in range(100):
        x_new = np.zeros_like(x).astype(float)

        for i in range(len(A[0])):
            s1 = np.dot(A[i][:i], x[:i])
            s2 = np.dot(A[i][i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / float(A[i][i])
            if x_new[i] == x[i]:
                break

        if np.allclose(x, x_new, atol=eps, rtol=0.):
            break

        # if np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(len(A[0])))) <= eps:
        #     break

        x = x_new
    return x.tolist()