import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

from pyweb import pydom
from pyscript import display

def update_graph(event):
	y1 = pydom["input#y1"][0].value
	y2 = pydom["input#y2"][0].value
	y3 = pydom["input#y3"][0].value
	y4 = pydom["input#y4"][0].value

	x = [1,2,3,4]
	y = [y1,y2,y3,y4]
	x = np.array(x)
	y = np.array(y)
	xfloat = [float(i) for i in x]
	yfloat = [float(i) for i in y]
	x_model = np.arange(0.0,50.0,.01)
	y_model = 2*x_model*x_model
	fig1, ax1 = plt.subplots(1,dpi=150,figsize=(5,3))
	fig1, ax1 = plt.subplots()
	ax1.scatter(yfloat,xfloat)
	ax1.set_title("Graph of Data",fontsize=11)
	ax1.set_xlabel("x variable",fontsize=10)
	ax1.set_ylabel("y variable",fontsize=10)
	plt.plot(x_model, y_model)
	ax1.set_xlim(0,6)
	ax1.set_ylim(0,50)
	ax1.margins(y=0)
	ax1.grid()
	display(fig1, target='graph', append=False)

# First create the x and y coordinates of the points.
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = (np.cos(radii) * np.cos(3 * angles)).flatten()

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(x, y)

# Mask off unwanted triangles.
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                            y[triang.triangles].mean(axis=1))
                < min_radius)

fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

display(fig1, target="mpl")
