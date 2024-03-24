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

# Функція для знаходження суми всіх значень у дереві
def tree_sum(root):
    if root is None:
        return 0
    return root.value + tree_sum(root.left) + tree_sum(root.right)

# Приклад використання:
# Створюємо дерево
root = None
values = [10, 5, 15, 3, 8, 12, 20]
for value in values:
    root = insert(root, value)

# Знаходимо суму всіх значень у дереві
total_sum = tree_sum(root)
print("Сума всіх значень у дереві:", total_sum)
