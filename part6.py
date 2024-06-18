# # Бинарный поиск
def binary_search(l, x):
    low = 0
    high = len(l) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1
l = [4, 2, 6, 10, 8, 22, 18, 9]
x = 10

result = binary_search(l, x)

if result != -1:
    print(f"Элемент {x} найден в позиции {result}.")
else:
    print(f"Элемент {x} не найден.")

#Пузырьковая сортировка
def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

l = [5, 7, 15, 25, 34, 16, 95]
bubble_sort(l)
for i in range(len(l)):
    print(l[i])
