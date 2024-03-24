# Визначення структури вузла дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для вставки значення у дерево
def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Функція для пошуку найменшого значення у дереві
def find_min(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.value

# Приклад використання:
# Створюємо дерево
root = None
values = [10, 5, 15, 3, 8, 12, 20]
for value in values:
    root = insert(root, value)

# Знаходимо найменше значення у дереві
min_value = find_min(root)
print("Найменше значення у дереві:", min_value)
