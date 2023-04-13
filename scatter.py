import csv
import matplotlib
import numpy as np

with open('./sessions.csv') as f:
    reader = csv.DictReader(f)
