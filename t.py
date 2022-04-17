#
#https://pythonguides.com/stacked-bar-chart-matplotlib/#Stacked_bar_chart_matplotlib
# Import Library

import matplotlib.pyplot as plt

# Define Data

Class = ["First", "Second", "Third", "Fourth", "Fifth"]
Pass = [30, 33, 20, 26, 15]
Fail = [1, 2, 3, 1, 4]

# Define width of stacked chart

w = 0.6

# Plot stacked bar chart

plt.bar(Class, Pass, w)
plt.bar(Class, Fail, w, bottom=Pass)

# Add labels

plt.xlabel("Classes")
plt.ylabel("No.of students")

# Display

plt.show()
