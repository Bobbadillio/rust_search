import sys

import argparse
from maze import Maze
import random
parser = argparse.ArgumentParser(description='Process number of graphs to generate')

parser.add_argument('--seed', dest='seed', nargs = '?', type= int,
                    help='sum the integers (default: find the max)')

parser.add_argument('--maze-count', dest='maze_count', nargs = '?',
                    type = int,
                    help='sum the integers (default: find the max)')

parser.add_argument('--height', dest='height', nargs='?', type = int,
                    help='sum the integers (default: find the max)')
parser.add_argument('--width', dest='width', nargs='?', type = int,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args)

seed = int(args.seed)
for _ in range(args.maze_count):
    start = str((random.randrange(0, args.width),
                random.randrange(0, args.height)))
    end = str((random.randrange(0, args.width),
                random.randrange(0, args.height)))
    graph = Maze.generate(width=args.width,height=args.height,seed=seed)
#    print(graph)
    cell_representation = ",".join([str((cell.x,cell.y)) for cell in graph.cells])
    edges = [tuple(sorted(((cell.x,cell.y),(neighbor.x,neighbor.y)))) for cell in graph.cells for neighbor in graph.neighbors(cell)]
    print(len(edges))
    edge_representation = ",".join([str(edge) for edge in set(edges)])
    print(len(set(edges)))
#    print(edges)
    print(":".join([start,end,cell_representation,edge_representation]))
    seed = seed + 1

