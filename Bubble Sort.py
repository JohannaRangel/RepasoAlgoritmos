#%%
import time

 #%% Ordenar una lista de cadenas
def bubble_sort_strings(arr):
    """
    Ordena una lista de cadenas utilizando el algoritmo de Bubble Sort.

    Args:
        arr (list): La lista de cadenas a ordenar.

    Returns:
        None: La función ordena la lista en su lugar, por lo que no devuelve nada.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
# %%
string_list = ["banana", "apple", "orange", "grape", "cherry"]

# %%
bubble_sort_strings(string_list)
print("Lista ordenada alfabéticamente:", string_list)

# Output: Lista ordenada alfabéticamente: ['apple', 'banana', 'cherry', 'grape', 'orange']

# %%

'''
Si quisieramos verificar la complejidad temporal de manera práctica, puedes medir el tiempo de ejecución del algoritmo para diferentes tamaños 
de entrada y luego comparar los resultados con la función de complejidad esperada. 

En la práctica, no necesitas realizar mediciones adicionales para verificar la complejidad espacial del algoritmo Bubble Sort, ya que su 
comportamiento de uso de memoria es directo y constante.

Es importante tener en cuenta que los resultados pueden variar según el entorno de ejecución y otros factores, por lo que se recomienda ejecutar 
varias pruebas y tomar promedios para obtener una estimación más precisa del tiempo de ejecución.

Veamos un ejemplo
'''

# %% Ejemplo

## Función para generar una lista de cadenas de longitud n
def generate_string_list(n):
    """
    Genera una lista de cadenas de longitud n.

    Args:
        n (int): Longitud de la lista de cadenas a generar.

    Returns:
        list: Una lista de cadenas que van desde '0' hasta 'n-1'.
    """
    return [str(i) for i in range(n)]


## Función para medir el tiempo de ejecución del bubble_sort_strings
def measure_time(n):
    """
    Mide el tiempo de ejecución del algoritmo bubble_sort_strings para una lista de cadenas de longitud n.

    Args:
        n (int): Longitud de la lista de cadenas.

    Returns:
        float: El tiempo de ejecución del algoritmo en segundos.
    """
    arr = generate_string_list(n)
    start_time = time.time()
    bubble_sort_strings(arr)
    end_time = time.time()
    return end_time - start_time


## Probamos para diferentes tamaños de entrada
for n in [1000, 2000, 3000]:
    execution_time = measure_time(n)
    print(f"Tamaño de entrada: {n}, Tiempo de ejecución: {execution_time} segundos")

# Output:
# Tamaño de entrada: 1000, Tiempo de ejecución: 0.055765628814697266 segundos
# Tamaño de entrada: 2000, Tiempo de ejecución: 0.20585131645202637 segundos
# Tamaño de entrada: 3000, Tiempo de ejecución: 0.45195913314819336 segundos

# %%





#Referencias: 
#  https://www.studysmarter.co.uk/explanations/computer-science/computer-programming/python-bubble-sort/
#  https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php
#  https://chat.openai.com/
