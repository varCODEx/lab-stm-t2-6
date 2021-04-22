def Pi(ci, bi, ai, Pi_prev):
    return -1*ci/(bi+ai*Pi_prev)

def Qi(di, bi, ai, Pi_prev, Qi_prev):
    return (di - ai*Qi_prev)/(bi + ai*Pi_prev)

def tridiagonal_mx_algorithm(A, b):
    n = len(A)
    for i in range(n):
        A[i] = [0]+A[i]+[0]

    PQ = []
    Pi_prev = Qi_prev = 0
    for i in range(n):
        ai, bi, ci = A[i][i:i+3]
        di = b[i]
        P = Pi(ci, bi, ai, Pi_prev)
        Q = Qi(di, bi, ai, Pi_prev, Qi_prev)
        PQ.append((P, Q))
        Pi_prev, Qi_prev = P, Q

    x = [0]
    for P, Q in reversed(PQ):
        x.append(x[-1]*P+Q)

    return list(reversed(x[1:]))