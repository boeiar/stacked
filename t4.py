#
#https://stackoverflow.com/questions/21397549/stack-bar-plot-in-matplotlib-and-add-label-to-each-section
import numpy as np
import matplotlib.pyplot as plt

# some labels for each row
people = ('A','B','C','D','E','F','G','H')
r = len(people)

# how many data points overall (average of 3 per person)
n = r * 3

# which person does each segment belong to?
rows = np.random.randint(0, r, (n,))
# how high is the segment?
heights = np.random.randint(3,12, n,)
# what label to put on the segment (xrange in py2.7, range for py3)
labels = range(n)
colors ='rgbymc'

patch_handles = []

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)



bottoms = np.zeros(r,)
row_counts = np.zeros(r,)

for (r, h, l) in zip(rows, heights, labels):
    print (r, h, l)
    patch_handles.append(ax.bar(r, h, align='center', bottom=bottoms[r],
        color=colors[int(row_counts[r]) % len(colors)]))
    bottoms[r] += h
    row_counts[r] += 1
    # we know there is only one patch but could enumerate if expanded
    patch = patch_handles[-1][0] 
    bl = patch.get_xy()
    x = 0.5*patch.get_width() + bl[0]
    y = 0.5*patch.get_height() + bl[1]
    ax.text(x, y, "%d%%" % (l), ha='center',va='center')
  
x_pos = np.arange(8)
ax.set_xticks(x_pos)
ax.set_xticklabels(people)
ax.set_ylabel('Distance')

plt.show()
