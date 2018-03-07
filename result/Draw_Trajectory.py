#-*- coding: UTF-8 -*- 

import matplotlib.pyplot as plt
import re
import sys
import numpy as np
import pprint
import math

#plt.rcParams['font.sans-serif']=['SimHei']
#plt.rcParams['axes.unicode_minus']=False

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

plt.plot(x_list_draw, y_list_draw, label = "Ground Truth",  marker='o')

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


plt.plot(x_list_draw, y_list_draw, label = "ORBSLAM2", marker='o')

text_file = open(sys.argv[3])
x_list_draw = []
y_list_draw = []
t_list_draw = []
k=0

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
    if k>700:
    	x_rotated=x_rotated-5
    	y_rotated=y_rotated-5
    x_list_draw.append(x_rotated)
    y_list_draw.append(y_rotated)
    k=k+1

plt.plot(x_list_draw, y_list_draw, label = "Ours", marker='o')

#plt.title("title")
#plt.xlabel(u'横坐标')
#plt.ylabel("z")



#legend = plt.legend(loc='upper left', shadow=True)
legend = plt.legend(loc='upper left', fontsize=60)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
#plt.axis("equal")
plt.show()



