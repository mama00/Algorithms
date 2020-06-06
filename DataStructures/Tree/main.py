from tree import Tree
from node import Node

root_node=Node(42)
n_554=Node(554)
n_55=Node(34)
root=Tree(root_node)
root.insert(Node(4))
root.insert(Node(2))
root.insert(Node(5))
root.insert(Node(6))
root.insert(n_55)

root.insert(n_554)
root.insert(Node(72))
root.insert(Node(33))
root.delete(55)
# root.printTree()
root.printOrder()
