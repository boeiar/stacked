#
#https://stackoverflow.com/questions/21397549/stack-bar-plot-in-matplotlib-and-add-label-to-each-section
import xml.etree.ElementTree as ET
import string
import numpy as np
import matplotlib.pyplot as plt
import sys
from operator import attrgetter

tree = ET.parse('callGraph.cgx')
root = tree.getroot()
mcs = root.findall('.//maxCallChain')
fcs = root.findall('.//functions/function')
fnames = {}
for f in fcs:
    fnames[int(f.find('id').text)] = f.find('name').text

chains = list(string.ascii_uppercase[:len(mcs)])

stacks = {}
columns = []
nodes = []
stacksizes = []
currentcolumn = 0
for column, mc in enumerate(mcs):
    stacks[column] = {
        'nodes' : [],
        'fcns' : [],
        'sszs' : [],
        'sumszs' : 0
    }
    for e in mc.findall('./entry'):
        node = int(e.find('./function').text)
        xpath_string = f"./functions/function/[id='{node}']"
        name = root.find(xpath_string).find('name').text
        stack = -1 * int(e.find('./stack').text)
        stacks[column]['nodes'].insert(0,node)
        stacks[column]['fcns'].insert(0,name)
        stacks[column]['sszs'].insert(0,stack)
        stacks[column]['sumszs'] += stack

stackKeys = stacks.keys()
def getSum(e):
    return stacks[e]['sumszs']

def getCount(e):
    return len(stacks[e]['fcns'])

sortedStacks = sorted(stackKeys, key = getSum)
deepestStack = {'sum': getSum(sortedStacks[0]), 'count': getCount(sortedStacks[0])}

#colors ='rgbymc'    
colors = "rgb"

patch_handles = []
fig = plt.figure(figsize=(19.2,10.8))
ax = fig.add_subplot(111)

r = len(stacks)
bottoms = np.zeros(r,)
row_counts = np.zeros(r,)
multiText = ""
for plotCol, col in enumerate(sortedStacks):
    for (h, l) in zip (stacks[col]['sszs'], stacks[col]['fcns']):
        patch_handles.append(ax.bar(plotCol, h, align='center', bottom=bottoms[col],
                            color=colors[int(row_counts[col]) % len(colors)]))
        bottoms[col] += h
        row_counts[col] += 1
        patchText = l + ":" + str(abs(h))
        if (0 == h):
            if ("" != multiText):
                multiText += "\n " 
            multiText += patchText
            continue
        if ("" == multiText):
            multiText = patchText
        else:
            multiText += "\n" + patchText
        patch = patch_handles[-1][0] 
        bl = patch.get_xy()
        x = bl[0] + 0.5 * patch.get_width() 
        y = bl[1] + 0.5 * patch.get_height()
        txt = ax.text(x, y, multiText, ha='center',va='center', fontsize='small')
        txt.set_bbox({'facecolor': 'white', 'alpha':0.5})
        multiText = ""
    if ("" != multiText):        
        patch = patch_handles[-1][0] 
        bl = patch.get_xy()
        x = bl[0] + 0.5 * patch.get_width() 
        y = bl[1] + 0.5 * patch.get_height()
        txt = ax.text(x, y, multiText, ha='center',va='center', fontsize='small')
        txt.set_bbox({'facecolor': 'white', 'alpha':0.5})
        multiText = ""
        
  
x_pos = np.arange(r)
ax.set_xticks(x_pos)
ax.set_xticklabels(chains)
ax.set_ylabel('Stack Depth')
ax.set_ylim(ymax= abs(deepestStack['sum'] / deepestStack['count']))
#for s in sortedStacks:
#    print(stacks[s]['fcns'])
#print(deepestStack)                            
#plt.ion()    
#plt.show()
plt.savefig(r"E:\Users\boe\Documents\boeboe\VC-stuff\stacked\tg3.svg")
