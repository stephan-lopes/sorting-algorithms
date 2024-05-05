def bubble_sort(lista: list) -> list:
    list_length = len(lista) - 1
    for i in range(list_length):
        swap = False
        for j in range(list_length - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swap = True
        if swap == False:
            return lista
    return lista

if  __name__ == "__main__":
    print(bubble_sort([10, 20, 1, 67, 9, 100, 2]))