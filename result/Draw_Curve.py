import matplotlib.pyplot as plt
import re
import sys
import numpy as np
import pprint
import math

text_file = open(sys.argv[1])
x_list_draw = []
y_list_draw = []
for line in text_file.readlines():
    line.strip()
    cols = line.split()
    #print line
    x = float(cols[0])
    y = float(cols[1])
    x_list_draw.append(x)
    y_list_draw.append(y)

plt.plot(x_list_draw, y_list_draw, label = "curve", marker='o')


legend = plt.legend(loc='upper right', shadow=True)
#plt.axis("equal")
plt.show()



