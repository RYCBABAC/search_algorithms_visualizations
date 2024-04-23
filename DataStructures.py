# Node class
class Node(object):

    # Constructor
    def __init__(self, state, parent, action, value=0):
        self.state = state  # Current state
        self.parent = parent  # Previous node
        self.action = action  # Previous action
        self.value = value  # Node's value


# LIFO stack class
class Stack(object):

    # Constructor
    def __init__(self):
        self.nodes = []  # List of the nodes in the stack

    # Checks if the stack is empty
    def empty(self):
        return len(self.nodes) == 0

    # Checks if a state is in the stack
    def contains(self, state):
        return any(node.state == state for node in self.nodes)

    # Adds a node to the stack
    def add(self, node):
        self.nodes.append(node)

    # Removes a node from the stack
    def remove(self):
        if self.empty():
            raise Exception("Empty Stuck")

        temp = self.nodes[-1]
        self.nodes = self.nodes[:-1]
        return temp


# FIFO queue class
class Queue(Stack):

    # Removes a node from the queue
    def remove(self):
        if self.empty():
            raise Exception("Empty Queue")

        temp = self.nodes[0]
        self.nodes = self.nodes[1:]
        return temp


# Heap queue class
class Heap(Queue):

    def add(self, node):

        if self.empty():
            self.nodes.append(node)
            return
        elif node.value <= self.nodes[0].value:
            self.nodes.insert(0, node)
            return
        elif node.value >= self.nodes[-1].value:
            self.nodes.append(node)
            return

        check_point = int(len(self.nodes) / 2)
        while True:
            if node.value <= self.nodes[check_point].value:
                if node.value >= self.nodes[check_point-1].value:
                    self.nodes.insert(check_point, node)
                    return
                check_point = int(check_point / 2)
            else:
                if node.value <= self.nodes[check_point+1].value:
                    self.nodes.insert(check_point, node)
                    return
                check_point = int((len(self.nodes) - check_point) / 2) + check_point
