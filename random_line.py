import argparse
import random

### Argument parser ###
parser = argparse.ArgumentParser(description='Get a random line from a text file')
parser.add_argument('file',nargs=1, type=str)
parser.add_argument('-r', '--remove', action='store_true', help="Remove drawn line from files") 
parser.add_argument('-v', '--verbose', action='store_true', help="Print verbose") 
args = parser.parse_args()

lines = list()

def read_file():
    try:
        f = open(args.file[0], "r")
    except FileNotFoundError:
        print(f'File "{args.file[0]}" not found')
        exit()
    for line in f:
        lines.append(line.rstrip())
    if (len(lines) == 0):
        print("No more lines remaining in file")
        exit()

def get_random_line():
    random_item = random.choice(lines)
    return random_item 

def remove_line(line):
    lines.remove(line)

def write_file():
    f = open(args.file[0], "w")
    for line in lines:
        f.write(line + '\n')

read_file()
line = get_random_line()
if args.verbose: print(f'Got random line: {line}')
else: print(line)
if args.remove: 
    remove_line(line)
    if args.verbose: print('line removed')
if args.verbose: print(f'Lines remaining: {len(lines)}')
write_file()