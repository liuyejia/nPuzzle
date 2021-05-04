# Node initialization and cost comparison for each search method
# __init__: initialize each node with h(n), estimated distance from current node to the goal node
# __lt__: compare nodes with f(n) = g(n) + h(n), where g(n) is the depth of getting to the node

import numpy as np
from path import GOAL_FILE
from utils import read_matrix

goal_state = read_matrix(GOAL_FILE)

class Node:
  def __init__(self, depth, state, prev, move):
    self.state = state
    self.depth = depth
    self.prev = prev
    self.move = move
    self.h = None
  
  def init_node(self, depth, state, prev, move):
    return Node(depth, state, prev, move)


# Uniform cost search
class UniformNode(Node):
  def __init__(self, depth, state, prev, move):
    # h(n) = 0
    super(UniformNode, self).__init__(depth, state, prev, move)
  
  def __lt__(self, other):
    # select node with smallest g(n)
    return self.depth < other.depth
  
  def init_node(self, depth, state, prev, move):
    return UniformNode(depth, state, prev, move)


# A* search with misplaced tile heuristic
class MisplacedNode(Node):
  def __init__(self, depth, state, prev, move):
    super(MisplacedNode, self).__init__(depth, state, prev, move)
    # h(n) = sum of misplaced tiles
    self.h = (self.state != goal_state).sum()
    # not count '0' if it's misplaced
    if np.where(self.state == 0) != np.where(goal_state == 0):
      self.h = self.h - 1

  
  def __lt__(self, other):
    # select node with smallest h(n) + g(n)
    return self.depth + self.h < other.depth + other.h
  
  def init_node(self, depth, state, prev, move):
    return MisplacedNode(depth, state, prev, move)


# A* search with Manhattan distance heuristic
class ManhattanNode(Node):
  def __init__(self, depth, state, prev, move):
    super(ManhattanNode, self).__init__(depth, state, prev, move)
    self.h = 0
    # h(n) = sum of ideal moves from current pos to goal pos for each tile
    for i, line in enumerate(goal_state):
      for j, num in enumerate(line):
        if num == 0:  # Not count '0'
          continue
        else:
          rows, cols = np.where(state == num)
          self.h += abs(i - int(rows)) + abs(j - int(cols))
  
  def __lt__(self, other):
    # select node with smallest g(n) + h(n)
    return self.depth + self.h < other.depth + other.h
  
  def init_node(self, depth, state, prev, move):
    return ManhattanNode(depth, state, prev, move)
