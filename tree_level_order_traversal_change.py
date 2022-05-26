from collections import deque
from typing import Union, List


class Node:
    """ Single tree node class """

    def __init__(self, title: Union[str, int], nodes: List = None) -> None:
        self.title: Union[str, int] = title
        self.children: List[Node] = nodes or []

    def log_node_title(self) -> None:
        """ Log the node title """
        print(self.title, end=" ")


def main(root_node: Node) -> None:
    """ Main traversal method for the tree with changing traversal direction on each level """

    if root_node is None:
        return

    if not root_node.children:
        root_node.log_node_title()
        return

    queue: deque = deque()  # Queue of nodes to process
    nodes_for_reverse_log: list = []  # Use list to maintain reverse order logic
    reverse: bool = False  # Define the traversal direction
    queue.append(root_node)

    # Process queue until it will not be empty
    while queue:
        for i in range(len(queue)):
            # Get node to process from the queue
            temp: Node = queue.popleft()

            # If not reversed order - log the title, otherwise add it to the nodes_for_reverse_log, so we will process it later
            if not reverse:
                temp.log_node_title()
            else:
                nodes_for_reverse_log.append(temp)

            # Add all children to the queue
            for child in temp.children:
                queue.append(child)

        # If reverse, then log all nodes titles in reverse order from
        if reverse:
            while nodes_for_reverse_log:
                nodes_for_reverse_log.pop(-1).log_node_title()

        reverse = not reverse  # Change reverse value to opposite
        print()  # New line


if __name__ == '__main__':
    node_11 = Node(11)
    node_10 = Node(10)
    node_9 = Node(9)
    node_8 = Node(8)
    node_7 = Node(7)
    node_6 = Node(6)
    node_5 = Node(5, [node_10, node_11])
    node_4 = Node(4, [node_8, node_9])
    node_3 = Node(3, [node_6, node_7])
    node_2 = Node(2, [node_4, node_5])
    root = Node(1, [node_2, node_3])

    main(root)
