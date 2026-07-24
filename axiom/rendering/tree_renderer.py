class TreeRenderer:
    """
    Renders a TraceNode tree to the console.
    """

    def render(self, node):
        self._render(node, "", True)

    def _render(self, node, prefix, is_last):
        connector = "└── " if is_last else "├── "

        if prefix:
            print(prefix + connector + node.name)
        else:
            print(node.name)

        child_prefix = prefix + ("    " if is_last else "│   ")

        for index, child in enumerate(node.children):
            self._render(
                child,
                child_prefix,
                index == len(node.children) - 1,
            )