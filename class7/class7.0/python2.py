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

        # Push children in reverse for left-to-right traversal
        for child in reversed(current_node.children):
            stack.append(child)

print(f"Goal node '{goal}' not found in the tree.")

# Create tree nodes
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

# Build tree
A.children = [B, C, D]
B.children = [E]
D.children = [F]

# Run DFS to search for node 'D'
dfs(A, 'D')
