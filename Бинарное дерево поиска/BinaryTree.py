class CostItem:
    def __init__(self, number):
        self.number = number
        self.parent = None
        self.LeftChild = None
        self.RightChild = None

def AddCost(root, NewItem):
    if NewItem.number < root.number:
        if root.LeftChild is None:
            root.LeftChild = NewItem
            NewItem.parent = root
        else:
            AddCost(root.LeftChild, NewItem)
    else:
        if root.RightChild is None:
            root.RightChild = NewItem
            NewItem.parent = root
        else:
            AddCost(root.RightChild, NewItem)

def FindCost(root, FindCostNumber):
    if root is None or root.number == FindCostNumber:
        return root

    if FindCostNumber < root.number:
        return FindCost(root.LeftChild, FindCostNumber)
    else:
        return FindCost(root.RightChild, FindCostNumber)

def PrintElem(root):
    if root is not None:
        print("Номер:", root.number)
        if root.LeftChild is not None:
            print("Левый потомок:", root.LeftChild.number)
        if root.RightChild is not None:
            print("Правый потомок:", root.RightChild.number)
        print()
        PrintElem(root.LeftChild)
        PrintElem(root.RightChild)
    else:
        return

# Создание древовидной структуры данных с несколькими статьями затрат
root = CostItem(100)
AddCost(root, CostItem(25))

AddCost(root, CostItem(100))
AddCost(root, CostItem(60))
AddCost(root, CostItem(135))
AddCost(root, CostItem(300))

# Вывод иерархии статей затрат
PrintElem(root)

# Поиск статьи затрат по номеру существующей статьи
FindCostNumber = 135
elem = FindCost(root, FindCostNumber)

if elem is not None:
    print("Статья затрат c номером", FindCostNumber, "найдена!")
else:
    print("Статья затрат c номером", FindCostNumber, "не найдена!")

print()

# Поиск статьи затрат по номеру несуществующей статьи
FindCostNumber = 145
elem = FindCost(root, FindCostNumber)

if elem is not None:
    print("Статья затрат c номером", FindCostNumber, "найдена!")
else:
    print("Статья затрат c номером", FindCostNumber, "не найдена!")

print()
