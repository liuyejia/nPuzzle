# CS 205 Project 1
This project aims at solving the 8 puzzle problem. 

## Install & Run
1. Git clone the repo to your own local directory 

2. Go to nPuzzle directory

   > cd nPuzzle
   
3. Run the program
   
   > python main.py --method 1 --puzzle_input data/doable.txt --out_file data/out.txt
   
   
   - --method: input search algorithm number. '1' : uniform cost search; **2** represents the A* search with misplaced tile heuristic; **3** represents A* search with Manhatten distance heuristic. 
   
   - --puzzle_input: file location of puzzle input
   
   - --out_file: file location of solution backtrace

## Folder Structure


* main.py:  determine which search algorithm to run by parsing user inputs
* node.py:  initialize search nodes with corresponding heuristic of search algorithm
* path.py:  store goal state file path
* utils.py:  a series of util functions, including read/write nodes, expand/explore candidate nodes depth, move black tile and etc
* data/:   store test puzzles and solution backtrace outputs *(note: you can specify your own inputs/outputs locations)*
   
   
