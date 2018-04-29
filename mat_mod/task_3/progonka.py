def method_progonki(n, a, b, c, f, mu1_local, mu2_local):
    alpha = [0]*(n - 1)
    beta = [0]*(n - 1)

    alpha[0] = 0
    beta[0] = mu1_local

    for i in range(0, n - 2):
        alpha[i+1] = a[i] / (c[i] - b[i] * alpha[i])
        beta[i+1] = (b[i] * beta[i] + f[i]) / (c[i] - b[i] * alpha[i])

    # print(alpha)
    # print(beta)

    y = [0] * n
    y[n - 1] = mu2_local

    for i in range(n - 1, 0, -1):
        y[i-1] = alpha[i-1]*y[i] + beta[i-1]

    return y
