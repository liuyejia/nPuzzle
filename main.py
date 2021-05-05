import heapq
import argparse

from node import UniformNode, MisplacedNode, ManhattanNode, goal_state
from utils import expand, read_matrix, write_nodes


# parser: read input arguments from command line
def get_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('--method', type=int, default=3)
  parser.add_argument('--puzzle_input', type=str, default='data/oh_boy.txt')
  parser.add_argument('--out_file', type=str, default='data/out_file.txt')
  return parser.parse_args()


def genereal_search(puzzle, args):
  if args.method == 1:
    # init node of uniform cost search using its heuristic
    start_node = UniformNode(0, puzzle, None, None)
  elif args.method == 2:
    # init node of A* with misplaces tile using its heuristic
    start_node = MisplacedNode(0, puzzle, None, None)
  elif args.method == 3:
    # init node of A* with Manhattan distance using its heuristic
    start_node = ManhattanNode(0, puzzle, None, None)
  else:
    raise ValueError("Not Implemented Method!")
  
  if (start_node.state == goal_state).all():  # no need to expand if input is the goal state
    print("Number of expanded nodes: ", 0)
    print("Max queue size: ", 0)
    return start_node
  
  queue = []
  max_queue = 0
  heapq.heappush(queue, start_node)
  explored_states = [start_node.state]
  while len(queue) > 0:
    max_queue = max(len(queue), max_queue)
    expand_node = heapq.heappop(queue)  # pop smallest cost node from queue to expand/explore
    end_node = expand(queue, expand_node, goal_state, explored_states)
    if end_node is not None:
      print("Number of expanded nodes: ", len(explored_states))
      print("Max queue size: ", max_queue)
      # print("Depth:", end_node.depth)
      return end_node
  return None


if __name__ == "__main__":
  # parse inputs. Example input: 'python main.py --method 2 --puzzle_input data/doable.txt --out_file data/out.txt'
  args = get_parser()
  str = ''
  if args.method == 1:
    str = 'uniform cost search'
  elif args.method == 2:
    str = 'A* search with misplaced tile heuristic'
  else:
    str = 'A* search with Manhattan distance heuristic'
  print("Your selected search algorithm is: ", str, "\nYour input puzzle is located in file: ", args.puzzle_input)
  print("Puzzle Input: ")
  input_file = open(args.puzzle_input)
  for line in input_file:
    print(line)
  puzzle = read_matrix(args.puzzle_input)  # read initial puzzle
  print("---------solving puzzle---------------")
  node = genereal_search(puzzle, args)
  write_nodes(args.out_file, node)  # record solution backtrack
  print("The puzzle solution backtrace is stored in file: ", args.out_file)

