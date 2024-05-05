def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]

        left = []
        middle = []
        right = []

        for x in arr:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else: 
                right.append(x)
        return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    array = [3,6,8,10,1,2,1]
    sorted_array = quicksort(array)
    print(sorted_array)

