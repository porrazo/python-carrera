def wallis(n):
    resultado = 1.0
    for i in range(1,n,1):
        left = float((2 * i) / (2.0 * i - 1))
        right = float((2 * i) / (2.0 * i + 1))
        total = left * right
        resultado *= total
    return resultado*2
print(wallis(10))

