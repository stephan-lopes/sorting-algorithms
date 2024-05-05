def insertion_sort(lista: list) -> list:
    for i in range(1, len(lista)): 
        value = lista[i] 
        while i > 0 and lista[i - 1] > value:
            lista[i] = lista[i - 1] 
            i = i - 1
        lista[i] = value
    return lista

if __name__ == "__main__":
    print(insertion_sort([6, 5, 8, 2]))