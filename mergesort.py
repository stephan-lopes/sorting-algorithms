def merge_sort(arr):
    if len(arr) > 1:
        # Dividindo a lista em duas metades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Ordenação recursiva das duas metades
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Mesclando as duas metades ordenadas
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copiando os elementos restantes de left_half, se houver
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copiando os elementos restantes de right_half, se houver
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Exemplo de uso
if __name__ == "__main__":
    example_array = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = merge_sort([10, 2,2, 90, 32])
    print("Array ordenado:", sorted_array)