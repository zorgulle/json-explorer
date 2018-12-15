class Node:
    def __init__(self, node_type, node_value):
        self.node_type = node_type
        self.node_value = node_value
        self.children = []



    def get_dict(self):
        return {self.node_type: self.node_value}

    def get_value(self, node_type):
        if self.node_type == node_type:
            return self.node_value



class NodeWithChildren(Node):
    def add_child(self, node):
        self.children.append(node)

    def get_dict(self):
        result = {}
        for child in self.children:
            result.update({child.node_type: child.node_value})

        return result

    def get_value(self, node_type):
        result = []
        for child in self.children:
            child.get_value(node_type)

        return result

def construct(dict_to_explore):
    root_node = NodeWithChildren("root", "root")
    for node_type, node_value in dict_to_explore.items():
        root_node.add_child(Node(node_type, node_value))
    return root_node

if __name__ == '__main__':
    print("Main")
    construct({"toto": "bernard"})
