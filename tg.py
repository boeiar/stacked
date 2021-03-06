#
#https://stackoverflow.com/questions/21397549/stack-bar-plot-in-matplotlib-and-add-label-to-each-section
import xml.etree.ElementTree as ET
import string
import numpy as np
import matplotlib.pyplot as plt

tree = ET.parse('callgraph/callGraph.xml')
root = tree.getroot()
mcs = root.findall('.//maxCallChain')
fcs = root.findall('.//functions/function')
fnames = {}
for f in fcs:
    fnames[int(f.find('id').text)] = f.find('name').text

chains = list(string.ascii_uppercase[:len(mcs)])
r = len(chains)

columns = []
nodes = []
stacksizes = []
currentcolumn = 0
for mc in mcs:
    for e in mc.findall('./entry'):
        node = int(e.find('./function').text)
        xpath_string =  f"./functions/function/[id='{node}']"
        name = root.find(xpath_string).find('name').text
        stack = int(e.find('./stack').text)
        columns.append(currentcolumn)
        nodes.append(node)
        stacksizes.append(stack)
    currentcolumn += 1


#colors ='rgbymc'    
def pyjama_colors():
    cs = []
    maxrange = 2
    for i in range(maxrange):
        ri = maxrange - i 
        for j in range(maxrange):
            rj = maxrange - j
            for k in range(maxrange):
                rk = maxrange -k
                cs.append((i/maxrange,j/maxrange,k/maxrange))
                cs.append((ri/maxrange,rj/maxrange,rk/maxrange))
    return(cs)

colors = "rgb"

patch_handles = []
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

bottoms = np.zeros(r,)
row_counts = np.zeros(r,)

for (r, h, l) in zip(columns, stacksizes, nodes):
    patch_handles.append(ax.bar(r, h, align='center', bottom=bottoms[r],
        color=colors[int(row_counts[r]) % len(colors)]))
    bottoms[r] += h
    row_counts[r] += 1
    # we know there is only one patch but could enumerate if expanded
    patch = patch_handles[-1][0] 
    bl = patch.get_xy()
    x = 0.5*patch.get_width() + bl[0]
    y = 0.5*patch.get_height() + bl[1]
    ax.text(x, y, fnames[l], ha='center',va='center', fontsize='small')
  
x_pos = np.arange(r+1)
ax.set_xticks(x_pos)
ax.set_xticklabels(chains)
ax.set_ylabel('Distance')

plt.show()
