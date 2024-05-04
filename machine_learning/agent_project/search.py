import sys
from collections import deque

from utils import is_in

class Problem:

    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        raise NotImplementedError
    
    def result(self, state, action):
        raise NotImplementedError
    
    def goal_test(self, state):
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal
        
    def path_cost(self, c, state1, action, state2):
        return c + 1
    
    def value(self, state):
        raise NotImplementedError
    
class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self) -> str:
        return "<Node {}>".format(self.state)
    
    def __lt__(self, node):
        return self.state < node.state
    
    def expand(self, problem):
        return [self.child_node(problem, action) for action in problem.actions(self.state)]
    
    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node
    
    def solution(self):
        return [node.action for node in self.path()[1:]]
    
    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state
    
    def __hash__(self):
        return hash(self.state)
    
def breatdth_first_tree_search(problem):
    frontier = deque([Node(problem.initial)])

    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None

def depth_first_tree_search(problem):
    frontier = [Node(problem.initial)]

    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None


class Graph:

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
        
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect1(self, A, B, distance):
        self.graph_dict.setdefault(A, {})[B] = distance

def UndirectedGraph(graph_dict=None):
    return Graph(graph_dict=graph_dict, directed=False)

class GraphProblem(Problem):

    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, A):
        return list(self.graph.get(A).keys())
    
