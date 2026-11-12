"""
Enunciado:
Implementa y compara el rendimiento de dos algoritmos de ordenamiento clásicos con Quicksort y Mergesort, en Python.

Funciones a desarrollar:
- `quicksort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Quicksort, dividiendo la lista en subconjuntos menores,
    mayores o iguales a un elemento pivote, y luego ordenando esos subconjuntos recursivamente.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `mergesort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Mergesort, dividiendo la lista en mitades hasta obtener
    subconjuntos que se consideran ordenados, para luego mezclar esos subconjuntos de manera ordenada.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `merge(left: List[int], right: List[int]) -> List[int]`:
    Descripción:
    Función auxiliar para el Mergesort que mezcla dos sublistas ordenadas en una sola lista ordenada.
    Parámetros:
        - `left` (List[int]): Sublista izquierda ordenada.
        - `right` (List[int]): Sublista derecha ordenada.

Ejemplo:
    start = time.time()
    sorted_array_quicksort = quicksort(test_array.copy())
    end_time = time.time() - start
    print(f"Quicksort on {size} elements took: {end_time:.5f} seconds.")
    print("First 10 elements after Quicksort:", sorted_array_quicksort[:10])

Salida esperada:
- Demostración del proceso de ordenación de una lista de números enteros con Quicksort y Mergesort, incluyendo la
visualización del tiempo que cada algoritmo toma para ordenar la misma lista.
"""

import random
import time
from typing import List


def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    # Divide los elementos según su valor respecto al pivote 
    # Pivot obtiene el elemento que ocupa la posición central
    pivot = arr[len(arr) // 2]
    # List comprehension: el elemento que queremos añadir
    # Recorrer los elementos de la lista
    # Filtrar los elementos que cumplan la condición
    left = [element for element in arr if element < pivot]
    middle = [element for element in arr if element == pivot]
    right = [element for element in arr if element > pivot]
    # Al hacer quicksort se vuelve a dividir hasta que llega a tener
    # 0 o un elemento.
    return quicksort(left) + middle + quicksort(right)


def mergesort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    # Divide la lista en dos mitades por su posición 
    # Obtiene el índice central
    middle = len(arr) // 2 
    left = arr[:middle]
    right = arr[middle:]
    # Llamar recursivamente a mergesort para
    # ordenar cada mitad
    left = mergesort(left) 
    right = mergesort(right)
    # Utiliza merge para unir las dos mitades ya ordenadas
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    # Continúa mientras las dos listas tengan elementos
    while len(left) > 0 and len(right) > 0:
        # Si el primer elemento de la lista izquierda es menor 
        # que el de la lista derecha, se añade a results y se 
        # elimina el primer elemento de left
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    # Incorpora los elementos que puedan quedar tanto en left como 
    # en right al quedar una de ellas vacías y terminar el bucle while
    result.extend(left)
    result.extend(right)
    return result


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    sizes = [100]  
    for size in sizes:
        test_array = [random.randint(1, 100) for _ in range(size)]
        
        print(f"\nOriginal array (first 10 elements of {size}):")
        print(test_array[:10])  
        
        start = time.time()
        sorted_array_quicksort = quicksort(test_array.copy())
        end_time = time.time() - start
        print(f"Quicksort on {size} elements took: {end_time:.5f} seconds.")
        print("First 10 elements after Quicksort:", sorted_array_quicksort[:10])
        
        start = time.time()
        sorted_array_mergesort = mergesort(test_array.copy())
        end_time = time.time() - start
        print(f"Mergesort on {size} elements took: {end_time:.5f} seconds.")
        print("First 10 elements after Mergesort:", sorted_array_mergesort[:10])
