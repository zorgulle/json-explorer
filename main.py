class Node:
    def __init__(self, node_type, node_value):
        self.node_type = node_type
        self.node_value = node_value

    def __str__(self):
        return "%s(%s)" % (self.node_type.upper(), self.node_value)

def construct(dict_to_explore):
    for node_type, node_value in dict_to_explore.items():
        node = Node(node_type, node_value)
    return node

if __name__ == '__main__':
    print("Main")
    construct({"toto": "bernard"})
