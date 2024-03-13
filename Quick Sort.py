#%%
'''
El código proporcionado implementa el algoritmo de Quick Sort y cuenta el número total de comparaciones realizadas durante la ordenación del array. 

Para determinar si este código representa el mejor, peor o caso promedio, necesitarías ejecutarlo con diferentes conjuntos de datos y analizar el número de comparaciones en cada caso.

En el mejor caso, el número de comparaciones sería mínimo.
En el peor caso, el número de comparaciones sería máximo.
En el caso promedio, el número de comparaciones estaría entre el mejor y el peor caso.
'''
def partition(arr, low, high):
    """
    Función que implementa la partición del array en Quick Sort.

    Parameters:
    arr (list): La lista que se va a ordenar.
    low (int): Índice inferior del subarray.
    high (int): Índice superior del subarray.

    Returns:
    int: El índice del pivote después de completar la partición.
    """
    pivot = arr[high]
    i = low - 1
    comparisons = 0  # Contador de comparaciones
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, comparisons

def quick_sort(arr, low, high):
    """
    Función que implementa el algoritmo de Quick Sort de manera recursiva.

    Parameters:
    arr (list): La lista que se va a ordenar.
    low (int): Índice inferior del subarray.
    high (int): Índice superior del subarray.

    Returns:
    None
    """    
    comparisons = 0  # Contador de comparaciones
    if low < high:
        pi, comparisons_partition = partition(arr, low, high)
        comparisons += comparisons_partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return comparisons


# Ejemplo de uso
arr = [5, 3, 8, 4, 2, 7, 1, 6]
n = len(arr)
comparisons = quick_sort(arr, 0, n - 1)
print("Arreglo ordenado:", arr)
print("Número de comparaciones:", comparisons)

# Output: 
#Arreglo ordenado: [1, 2, 3, 4, 5, 6, 7, 8]
#Número de comparaciones: 7

# %%

'''
Casos de uso:

Quick Sort, gracias a su velocidad y eficiencia promedio, se utiliza en una amplia variedad de aplicaciones del mundo real que involucran el ordenamiento de grandes conjuntos de datos. 

1. Inteligencia Artificial (IA):
  Aprendizaje automático: En algoritmos de aprendizaje automático, Quicksort se emplea para ordenar grandes cantidades de datos de entrenamiento. Estos datos pueden incluir imágenes, texto, números u otros tipos de información que el modelo necesita procesar para aprender patrones y hacer predicciones.
  Procesamiento del lenguaje natural (PNL): En aplicaciones de PNL como la traducción automática o la generación de texto, Quicksort se utiliza para ordenar listas de palabras, frases o documentos según criterios específicos, como la frecuencia de aparición o la relevancia para la tarea en cuestión.
2. Análisis de Datos:
  Ordenamiento de datasets masivos: Quicksort es ideal para analizar grandes conjuntos de datos financieros, de marketing, científicos, de redes sociales, etc. Permite ordenar los datos por fecha, valor, categoría u otros criterios relevantes para su exploración y visualización.
  Preparación de datos para análisis: A menudo, antes de aplicar técnicas de análisis de datos, se necesita limpiar y preparar los datos. Quicksort puede ayudar a ordenar los datos para identificar valores duplicados, outliers (valores atípicos) o inconsistencias, facilitando su limpieza y posterior análisis preciso.
3. Computación Gráfica:
  Ordenamiento de objetos 3D: En la renderización de escenas 3D, Quicksort se puede utilizar para ordenar objetos en función de su profundidad o distancia a la cámara. Esto permite al motor gráfico dibujar los objetos en el orden correcto, creando una imagen realista.
  Ordenamiento de geometrías: Al procesar geometrías 3D complejas compuestas por polígonos, Quicksort puede ayudar a ordenar las caras o vértices según diversos criterios. Esto puede ser útil para optimizar el proceso de renderizado y mejorar el rendimiento gráfico.
4. Aplicaciones Web:
  Ordenamiento de listas: En interfaces web dinámicas, Quicksort se utiliza para ordenar listas de productos, resultados de búsqueda, feeds de noticias o cualquier lista de elementos que necesite ser presentada al usuario de forma organizada.
  Ranking y recomendaciones: Para generar rankings o recomendaciones personalizadas, Quicksort permite ordenar elementos en función de criterios como la calificación del usuario, la popularidad, la relevancia para la búsqueda o el historial de compras.
5. Otros casos de uso:
  Ordenamiento de archivos: Quicksort se puede aplicar para ordenar archivos en un sistema informático según su nombre, tamaño, fecha de creación o cualquier otro atributo.
  Simulaciones: En simulaciones por computadora que involucran grandes cantidades de agentes o partículas, Quicksort puede utilizarse para ordenar y actualizar su estado de forma eficiente.
  Juegos: En el desarrollo de videojuegos, Quicksort se puede emplear para ordenar elementos del juego como enemigos, inventario o listas de puntajes, mejorando la eficiencia y fluidez del juego.
'''

# %%

'''
Referencias: 
  https://www.studysmarter.co.uk/explanations/computer-science/algorithms-in-computer-science/quick-sort/
  https://medium.com/karuna-sehgal/a-quick-explanation-of-quick-sort-7d8e2563629b
  https://chat.openai.com/
  https://gemini.google.com/app
'''

# %%




