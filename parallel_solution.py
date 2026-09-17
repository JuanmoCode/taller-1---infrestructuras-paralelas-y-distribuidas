import time
import concurrent.futures




# Algoritmo recursivo para calcular el n-ésimo número de Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Función para calcular Fibonacci en paralelo
def calcular_fibonacci_paralelo(n_elementos):
    inicio = time.time()

    resultados = [None] * n_elementos

    # Pool de procesos
    with concurrent.futures.ProcessPoolExecutor() as executor:

        # Se paraleliza el ciclo que calcula cada número de Fibonacci
        futuros = []

        for i in range(n_elementos):
            futuro = executor.submit(fibonacci, i)
            futuros.append(futuro)

        # Se recuperan los resultados en el mismo orden
        for i in range(n_elementos):
            resultados[i] = futuros[i].result()

    fin = time.time()

    # Este ciclo se mantiene secuencial para evitar problemas
    # de impresión(trampa serial) y mantener el orden de los resultados.
    print("[", end=" ")
    for i in range(n_elementos):
        print(f"{resultados[i]} ", end="")
    print("]")

    print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")


if __name__ == "__main__":
    for i in range(1, 9):
        calcular_fibonacci_paralelo(i*5)
