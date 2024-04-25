#Алгоритм XOR
print("Алгоритм XOR:")
def FindElem(arr):
    n = len(arr)
    xorSum = 0
    
    for a in arr:
        xorSum ^= a
    
    for i in range(1, n + 2):
        xorSum ^= i
    
    return xorSum

# Пример1 использования:
arr = [1, 4, 2, 5]  # Массив с пропущенным элементом 3
elem = FindElem(arr)
print("Недостающий элемент:", elem)

# Пример2 использования:

arr = [6, 1, 2, 4, 3, 8, 5]  # Массив с пропущенным элементом 7
elem = FindElem(arr)
print("Недостающий элемент:", elem)