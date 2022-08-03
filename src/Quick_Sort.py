from re import L


def partition(array, low, high):
    pivot, p = array[high], low
    for i in range(low, high):
        if array[i] <= pivot:
            array[i], array[p] = array[p], array[i]
            p += 1
    array[high], array[p] = array[p], array[high]

    return p

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

array = [10, 7, 8, 9, 1, 5]
print(array)
quick_sort(array, 0, len(array) - 1)
print(array)
    