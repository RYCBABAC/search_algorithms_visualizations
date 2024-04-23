from DataStructures import *
import abc


class Search(object):

    @abc.abstractmethod
    def neighbors(self, node):
        pass

    @abc.abstractmethod
    def heuristic(self, state):
        pass

    def dfs(self, start, target):

        if start == target:
            raise Exception("Starting point is the target")

        temp = Node(state=start, parent=None, action=None)
        frontier = Stack()
        frontier.add(temp)

        explored = set()

        while True:
            # Checks if frontier is empty
            if frontier.empty():
                raise Exception("No solution")

            # Move to next state
            temp = frontier.remove()

            # Found the target
            if temp.state == target:
                actions = []
                states = []

                while temp.parent is not None:
                    actions.append(temp.action)
                    states.append(temp.state)
                    temp = temp.parent

                actions.reverse()
                states.reverse()
                res = (states, actions, explored)
                return res

            explored.add(temp.state)
            for state, action in self.neighbors(temp):
                if not frontier.contains(state) and state not in explored:
                    frontier.add(Node(state=state, parent=temp, action=action))

    def bfs(self, start, target):

        if start == target:
            raise Exception("Starting point is the target")

        temp = Node(state=start, parent=None, action=None)
        frontier = Queue()
        frontier.add(temp)

        explored = set()

        while True:
            # Checks if frontier is empty
            if frontier.empty():
                raise Exception("No solution")

            # Move to next state
            temp = frontier.remove()

            # Found the target
            if temp.state == target:
                actions = []
                states = []

                while temp.parent is not None:
                    actions.append(temp.action)
                    states.append(temp.state)
                    temp = temp.parent

                actions.reverse()
                states.reverse()
                res = (states, actions, explored)
                return res

            explored.add(temp.state)
            for state, action in self.neighbors(temp):
                if not frontier.contains(state) and state not in explored:
                    frontier.add(Node(state=state, parent=temp, action=action))

    def greedy_bfs(self, start, target):

        if start == target:
            raise Exception("Starting point is the target")

        temp = Node(state=start, parent=None, action=None, value=self.heuristic(start))
        frontier = Heap()
        frontier.add(temp)

        explored = set()

        while True:
            # Checks if frontier is empty
            if frontier.empty():
                raise Exception("No solution")

            # Move to next state
            temp = frontier.remove()

            # Found the target
            if temp.state == target:
                actions = []
                states = []

                while temp.parent is not None:
                    actions.append(temp.action)
                    states.append(temp.state)
                    temp = temp.parent

                actions.reverse()
                states.reverse()
                res = (states, actions, explored)
                return res

            explored.add(temp.state)
            for state, action in self.neighbors(temp):
                if not frontier.contains(state) and state not in explored:
                    frontier.add(Node(state=state, parent=temp, action=action, value=self.heuristic(state)))

    def a_star(self, start, target):

        if start == target:
            raise Exception("Starting point is the target")

        temp = Node(state=start, parent=None, action=None, value=self.heuristic(start))
        frontier = Heap()
        frontier.add(temp)

        explored = set()
        cost = {temp.state: 0}

        while True:
            # Checks if frontier is empty
            if frontier.empty():
                raise Exception("No solution")

            # Move to next state
            temp = frontier.remove()

            # Found the target
            if temp.state == target:
                actions = []
                states = []

                while temp.parent is not None:
                    actions.append(temp.action)
                    states.append(temp.state)
                    temp = temp.parent

                actions.reverse()
                states.reverse()
                res = (states, actions, explored, cost)
                return res

            explored.add(temp.state)
            for state, action in self.neighbors(temp):
                if not frontier.contains(state) and state not in explored:
                    cost[state] = cost[temp.state]+1
                    frontier.add(Node(state=state, parent=temp, action=action, value=self.heuristic(state)+cost[state]))
