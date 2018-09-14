# import NumPy and MatplotLib pyplot
import numpy as np
import matplotlib.pyplot as plt
# Generate simple data set
from sklearn.datasets import make_blobs
centers = [(0.3, 0.3), (0.7, 0.7)]
n_samples = 30
X1, Y1 = make_blobs(n_samples=n_samples, n_features=2, cluster_std=0.1, centers=centers, shuffle=False, random_state=42)
Y1 = Y1 * 2 - 1


# To plot a point set we use the scatter plot functionality and set the color of each point according to the labels. 
# We plot the second, and third column ignoring the 1 column. For the color of each point we use the label.
# For more info on scatter plots we can simply write "plt.scatter?" in the cell below or in ipython.
plt.axis([0, 1, 0, 1])
plt.scatter(X1[:, 0], X1[:, 1], c=Y1, cmap=plt.cm.Paired, s=80)

# Here we use the 'plt.plot' command. 
# It takes a list of x coordinates, a list of y coordinates and some style options.
# In '-b' the '-' means to connect the points and 'b' means blue. 
# Linewidth is, wait for it... the width of the line.
plt.plot([0,0.6], [0.4,1], '-b', linewidth=2.0)

plt.show()

# Can you guess how you can view the docmumentation of the 'plot' command? 
# Hint, try write: plt.plot?