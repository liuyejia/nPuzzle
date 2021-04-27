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


class UniformNode(Node):
  def __init__(self, depth, state, prev, move):
    super(UniformNode, self).__init__(depth, state, prev, move)
  
  def __lt__(self, other):
    return self.depth < other.depth
  
  def init_node(self, depth, state, prev, move):
    return UniformNode(depth, state, prev, move)


class MisplacedNode(Node):
  def __init__(self, depth, state, prev, move):
    super(MisplacedNode, self).__init__(depth, state, prev, move)
    self.h = (self.state != goal_state).sum()
  
  def __lt__(self, other):
    return self.depth + self.h < other.depth + other.h
  
  def init_node(self, depth, state, prev, move):
    return MisplacedNode(depth, state, prev, move)


class MattHattenNode(Node):
  def __init__(self, depth, state, prev, move):
    super(MattHattenNode, self).__init__(depth, state, prev, move)
    self.h = 0
    for i, line in enumerate(goal_state):
      for j, num in enumerate(line):
        if num == 0:
          continue
        else:
          rows, cols = np.where(state == num)
          self.h += abs(i - int(rows)) + abs(j - int(cols))
  
  def __lt__(self, other):
    return self.depth + self.h < other.depth + other.h
  
  def init_node(self, depth, state, prev, move):
    return MattHattenNode(depth, state, prev, move)
