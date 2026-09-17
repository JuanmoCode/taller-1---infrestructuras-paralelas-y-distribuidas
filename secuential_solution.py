import numpy as np

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


MAX_VECTOR = 10

vector = np.arange(MAX_VECTOR)

for i in range(MAX_VECTOR):
    vector[i] = fibonacci(i)

print("[", end=' ')
for i in range(MAX_VECTOR):
    print(f"{vector[i]} ", end='')
print("]")

#En este código, el ciclo:
