#%%
import random
import time

 #%% Ordenar una lista con el algoritmo Merge Sort
def merge_sort(arr):
    """
    Implementación del algoritmo Merge Sort para ordenar una lista.

    Args:
    arr (list): La lista que se desea ordenar.

    Returns:
    None: La lista se ordena in-place.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
                
# %%
# Lista desordenada
unsorted_list = [5, 3, 8, 1, 2, 7, 4, 6]

# %%
merge_sort(unsorted_list)
print("Lista ordenada:", unsorted_list)

# Output: Lista ordenada: [1, 2, 3, 4, 5, 6, 7, 8]

# %%

'''
Veamos un ejemplo aplicando Merge Sort. 

Observarás que el tiempo de ejecución aumenta de manera logarítmica con el tamaño de la entrada,
lo que confirma la complejidad temporal de O(n log n) del algoritmo Merge Sort.

'''

# %% Ejemplo

## Función para medir el tiempo de ejecución del merge_sort()
def measure_time(n):
    """
    Mide el tiempo de ejecución del algoritmo Merge Sort para una lista de tamaño n.

    Args:
    n (int): Tamaño de la lista de números aleatorios.

    Returns:
    float: Tiempo de ejecución en segundos.
    """
    arr = [random.randint(0, 1000) for _ in range(n)]
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    return end_time - start_time


for n in [1000, 2000, 3000]:
    execution_time = measure_time(n)
    print(f"Tamaño de entrada: {n}, Tiempo de ejecución: {execution_time} segundos")

# Output:
# Tamaño de entrada: 1000, Tiempo de ejecución: 0.0030634403228759766 segundos
# Tamaño de entrada: 2000, Tiempo de ejecución: 0.007953882217407227 segundos
# Tamaño de entrada: 3000, Tiempo de ejecución: 0.008277177810668945 segundos

# %%

'''
Casos de uso:

Merge Sort es ideal para:

  Ordenar grandes conjuntos de datos: Su eficiencia lo hace ideal para conjuntos de datos que no caben en la memoria caché o que requieren un procesamiento rápido.
  Ordenar datos sensibles a la memoria: Su bajo uso de memoria lo hace ideal para situaciones donde la memoria es limitada.
  Ordenar datos en paralelo: Su naturaleza divide y vencerás facilita la implementación paralela, lo que mejora aún más el rendimiento.
  Implementar algoritmos más complejos: Se utiliza como base para algoritmos más avanzados como el algoritmo de ordenamiento externo.
'''

# %%

'''
Referencias: 
  https://www.studysmarter.co.uk/explanations/computer-science/algorithms-in-computer-science/merge-sort/
  https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php
  https://chat.openai.com/
  https://gemini.google.com/app
'''

# %%




