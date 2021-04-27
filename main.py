import heapq
import argparse

from node import UniformNode, MisplacedNode, MattHattenNode, goal_state
from utils import expand, read_matrix, write_nodes


# parser
def get_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('--method', type=int, default=3)
  parser.add_argument('--in_file', type=str, default='data/oh_boy.txt')
  parser.add_argument('--out_file', type=str, default='data/out_file.txt')
  return parser.parse_args()


# general search
def genereal_search(puzzle, args):
  if args.method == 1:
    start_node = UniformNode(0, puzzle, None, None)
  elif args.method == 2:
    start_node = MisplacedNode(0, puzzle, None, None)
  elif args.method == 3:
    start_node = MattHattenNode(0, puzzle, None, None)
  else:
    raise ValueError("Not Implemented Method!")
  
  if (start_node.state == goal_state).all():
    print("Expanded: ", 0)
    return start_node
  
  queue = []
  heapq.heappush(queue, start_node)
  explored_states = [start_node.state]
  while len(queue) > 0:
    expand_node = heapq.heappop(queue)
    end_node = expand(queue, expand_node, goal_state, explored_states)
    if end_node is not None:
      print("Expanded: ", len(explored_states))
      return end_node
  return None


if __name__ == "__main__":
  args = get_parser()
  puzzle = read_matrix(args.in_file)
  node = genereal_search(puzzle, args)
  write_nodes(args.out_file, node)
