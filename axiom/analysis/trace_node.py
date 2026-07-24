class TraceNode:
    """
    Represents one node in a call tree.
    """

    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)