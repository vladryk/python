
class TreeNode(object):

    def __init__(self,  value, left=None, right=None):
        self.left_node = left
        self.right_node = right
        self.value = value


class TreeNodeManager(object):

    def __init__(self, root=None, count=0):
        self.root_node = root
        self.count = count

    def add_node(self, value):
        node = self.search_node(self.root_node, value)
        node_value = getattr(node, 'value', None)
        if value == node_value:
            print("This value is present")
        elif value > node_value:
            node.right_node = TreeNode(value)
        elif value < node_value:
            node.left_node = TreeNode(value)

    def remove_node(self, value):
        node = self.search_node(self.root_node, value)
        if value != getattr(node, 'value', None):
            print("value not found")
            return
        if value == getattr(node, 'value', None):
            


    def create_tree(self, value):
        self.root_node = TreeNode(value)
        return self.root_node

    def search_node(self, node, value):
        node_value = getattr(node, 'value', None)
        if value == node_value:
            return node

        elif value > node_value:
            right_node = getattr(node, 'right_node', None)
            if right_node is None:
                return node
            else:
                node = right_node

        elif value < node_value:
            left_node = getattr(node, 'left_node', None)
            if left_node is None:
                return node
            else:
                node = left_node

        return self.search_node(node, value)
