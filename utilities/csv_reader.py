import csv
import sys
from os.path import dirname, abspath
parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)

def read_csv(filepath):
    list = []
    csv_data = open(filepath, "r")
    csv_reader = csv.reader(csv_data)
    for row in csv_reader:
        list.append(row)
    return list