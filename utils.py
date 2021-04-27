import heapq
import numpy as np
from copy import deepcopy


# read mat from txt
def read_matrix(file):
  with open(file) as f:
    lines = f.read().splitlines()
  num_lines = len(lines)
  mat = np.zeros((num_lines, num_lines), dtype=np.int32)
  for i in range(num_lines):
    mat[i] = np.array([int(num) for num in lines[i].split()])
  return mat


# write matrix to txt
def write_nodes(file, node):
  with open(file, 'w') as f:
    if node is None:
      f.write("No solution!")
    else:
      write_node(f, node)


def write_node(f, node):
  if node.prev is not None:
    write_node(f, node.prev)
  for line in node.state:
    f.write(' '.join([str(num) for num in line]))
    f.write("\n")
  f.write("\n")


def expand(queue, expand_node, goal_state, explored):
  up_state = move(expand_node.state, explored, "up")
  if up_state is not None:
    up_node = expand_node.init_node(expand_node.depth + 1, up_state, expand_node, 'up')
    if (up_state == goal_state).all():
      return up_node
    else:
      heapq.heappush(queue, up_node)
  
  down_state = move(expand_node.state, explored, "down")
  if down_state is not None:
    down_node = expand_node.init_node(expand_node.depth + 1, down_state, expand_node, 'down')
    if (down_state == goal_state).all():
      return down_node
    else:
      heapq.heappush(queue, down_node)
  
  left_state = move(expand_node.state, explored, "left")
  if left_state is not None:
    left_node = expand_node.init_node(expand_node.depth + 1, left_state, expand_node, 'left')
    if (left_state == goal_state).all():
      return left_node
    else:
      heapq.heappush(queue, left_node)
  
  right_state = move(expand_node.state, explored, "right")
  if right_state is not None:
    right_node = expand_node.init_node(expand_node.depth + 1, right_state, expand_node, 'right')
    if (right_state == goal_state).all():
      return right_node
    else:
      heapq.heappush(queue, right_node)
  
  return None


def move(state, explored, direction):
  rows, cols = np.where(state == 0)
  row = int(rows)
  col = int(cols)
  new_state = deepcopy(state)
  if direction == "up":
    if row == 0:
      return None
    else:
      new_state[row, col] = new_state[row - 1, col]
      new_state[row - 1, col] = 0
  elif direction == "down":
    if row == len(state) - 1:
      return None
    else:
      new_state[row, col] = new_state[row + 1, col]
      new_state[row + 1, col] = 0
  elif direction == "left":
    if col == 0:
      return None
    else:
      new_state[row, col] = new_state[row, col - 1]
      new_state[row, col - 1] = 0
  elif direction == "right":
    if col == len(state) - 1:
      return None
    else:
      new_state[row, col] = new_state[row, col + 1]
      new_state[row, col + 1] = 0
  for s in explored:
    if (new_state == s).all():
      return None
  explored.append(new_state)
  return new_state
