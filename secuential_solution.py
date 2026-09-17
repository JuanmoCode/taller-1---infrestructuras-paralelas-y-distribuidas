import time

import numpy as np

#algoritmo recursivo para calcular el n-ésimo número de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calcular_fibonacci_secuencial(n):

    inicio = time.time()

    MAX_VECTOR = n

    #Creación de un vector de tamaño MAX_VECTOR y llenado con los números de Fibonacci
    vector = np.arange(MAX_VECTOR)

    #Primer ciclo para llenar el vector con los números de Fibonacci
    for i in range(MAX_VECTOR):
        vector[i] = fibonacci(i)

    fin = time.time()

    tiempo_ejecucion = fin - inicio

    #Segundo ciclo para imprimir el vector de números de Fibonacci en orden
    print(f" fibonacci {MAX_VECTOR}[", end=' ')
    for i in range(MAX_VECTOR):
        print(f"{vector[i]} ", end='')
    print("]")

    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")


if __name__ == "__main__":
    for i in range(1, 9):
         calcular_fibonacci_secuencial(i*5)


