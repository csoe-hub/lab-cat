'''
This program prints stdin to the screen.
'''
import sys

def cat(filename):
    with open(filename, 'r') as f:
        for line in f:
            sys.stdout.write(line)

if __name__ == "__main__":
    for filename in sys.argv[1:]:
         cat(filename)
