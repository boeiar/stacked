#
#https://pythonguides.com/stacked-bar-chart-matplotlib/#Stacked_bar_chart_matplotlib
# Import libraries


import matplotlib.pyplot as plt
import pandas as pd

# Define Data


df = pd.DataFrame({
    'Male': [35, 20, 43, 12, 19],
    'Female': [20, 11, 18, 6, 9]
 })

MClass = ["MFirst","MSecond","MThird","MFourth","MFifth"]
FClass = ["FFirst","FSecond","FThird","FFourth","FFifth"]
ClassN = len(MClass)
# Plot stacked bar chart


ax = df.plot(stacked=True, kind='bar')

for n,bar in enumerate(ax.patches):
    height = bar.get_height()
    width = bar.get_width()
    x = bar.get_x()
    y = bar.get_y()
    if (n < ClassN):
        cat = MClass[n]
    else:
        cat = FClass[n-ClassN]
        
    label_text = str(n) + "--" + str(height) + cat 
    label_x = x + width / 2
    label_y = y + height / 2
    ax.text(label_x, label_y, label_text, ha='center',    
            va='center')
    
# Set Tick labels


#ax.set_xticklabels(Class,rotation='horizontal')

# Display chart


plt.show()
