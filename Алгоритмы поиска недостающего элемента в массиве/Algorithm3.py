#реализация алгоритма с использованием дополнительного массива
print("Реализация алгоритма с использованием дополнительного массива:")

def FindElem(arr):
    n = len(arr) + 1
    arrNew = []
    for _ in range(n + 1):
        arrNew.append(False)

    for num in arr:
        arrNew[num] = True

    for i in range(1, n):
        if not arrNew[i]:
            return i

    return None  # Если недостающий элемент не найден

# Пример1 использования:
arr = [1, 4, 2, 5]  # Массив с пропущенным элементом 3
elem = FindElem(arr)
print("Недостающий элемент:", elem)

# Пример2 использования:

arr = [6, 1, 2, 4, 3, 8, 5]  # Массив с пропущенным элементом 7
elem = FindElem(arr)
print("Недостающий элемент:", elem)



