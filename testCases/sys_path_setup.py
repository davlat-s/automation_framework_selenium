import sys
from os.path import dirname, abspath

def add_parent_dir():
    parent_dir = dirname(dirname(abspath(__file__)))
    sys.path.append(parent_dir)