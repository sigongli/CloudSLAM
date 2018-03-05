import matplotlib.pyplot as plt
import re
import sys
import numpy as np
import pprint
import math

text_file = open(sys.argv[1])
x_list_draw = []
y_list_draw = []
t_list_draw = []
for line in text_file.readlines():
    line.strip()
    cols = line.split()
    #print line
    x = float(cols[1])
    y = float(cols[3])
    #td = 4 * math.pi / 180.0
    td = 0 * math.pi / 180.0
    x_rotated = x * math.cos(td) - math.sin(td) * y
    y_rotated = x * math.sin(td) + math.cos(td) * y
    x_list_draw.append(x_rotated)
    y_list_draw.append(y_rotated)

plt.plot(x_list_draw, y_list_draw, label = "gt", marker='o')

text_file = open(sys.argv[2])
x_list_draw = []
y_list_draw = []
t_list_draw = []
for line in text_file.readlines():
    line.strip()
    cols = line.split()
    #print line
    x = float(cols[1])
    y = float(cols[3])
    #td = 4 * math.pi / 180.0
    td = 0 * math.pi / 180.0
    x_rotated = x * math.cos(td) - math.sin(td) * y
    y_rotated = x * math.sin(td) + math.cos(td) * y
    x_list_draw.append(x_rotated)
    y_list_draw.append(y_rotated)

plt.plot(x_list_draw, y_list_draw, label = "orginal", marker='o')

text_file = open(sys.argv[3])
x_list_draw = []
y_list_draw = []
t_list_draw = []
for line in text_file.readlines():
    line.strip()
    cols = line.split()
    #print line
    x = float(cols[1])
    y = float(cols[3])
    #td = 4 * math.pi / 180.0
    td = 0 * math.pi / 180.0
    x_rotated = x * math.cos(td) - math.sin(td) * y
    y_rotated = x * math.sin(td) + math.cos(td) * y
    x_list_draw.append(x_rotated)
    y_list_draw.append(y_rotated)

plt.plot(x_list_draw, y_list_draw, label = "changed", marker='o')




legend = plt.legend(loc='upper right', shadow=True)
plt.show()



