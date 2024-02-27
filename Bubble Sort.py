# Ordenar una lista de cadenas
 #%%
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
# %%

#Referencia: https://www.studysmarter.co.uk/explanations/computer-science/computer-programming/python-bubble-sort/
