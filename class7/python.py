class Node:
    def _init_(self, value):
        self.value = value
        self.children = []

def dfs(root, goal):
    if not root:
        return 

    stack = [root]

    while stack:
        current_node = stack.pop()
        print(f"Visiting: {current_node.value}")

        if current_node.value == goal:
            print(f"Goal node '{current_node.value}' found!")
            return current_node

