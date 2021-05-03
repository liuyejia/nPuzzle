# Node initialization and cost comparison for each search method
# __init__: initialize each node with heuristic value h(n)
# __lt__: compare nodes with f(n) = g(n) + h(n), where g(n) is the expanding depth

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
  
  def __lt__(self, other):
    # select node with smallest h(n) + g(n)
    return self.depth + self.h < other.depth + other.h
  
  def init_node(self, depth, state, prev, move):
    return MisplacedNode(depth, state, prev, move)


# A* search with Manhatten distance heuristic
class MattHattenNode(Node):
  def __init__(self, depth, state, prev, move):
    super(MattHattenNode, self).__init__(depth, state, prev, move)
    self.h = 0
    # h(n) = sum of ideal moves from current pos to goal pos for each tile
    for i, line in enumerate(goal_state):
      for j, num in enumerate(line):
        if num == 0:
          continue
        else:
          rows, cols = np.where(state == num)
          self.h += abs(i - int(rows)) + abs(j - int(cols))
  
  def __lt__(self, other):
    # select node with smallest g(n) + h(n)
    return self.depth + self.h < other.depth + other.h
  
  def init_node(self, depth, state, prev, move):
    return MattHattenNode(depth, state, prev, move)
