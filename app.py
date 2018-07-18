from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# READ DATA AND Z

# n=the number of columns in your data

fig, axs = plt.subplots(n, n, subplot_kw={'projection': '3d'})

for rowid in range(n):
	for colid in range(n):
		if (rowid == colid):
			# plot histogram
		else:
			axs[rowid*n + coldid].plot_trisurf(data[:,rowid], data[:,colid], z, linewidth=0.2, antialiased=True)

plt.show()