import matplotlib.pyplot as plt
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
	ax1.scatter(xfloat,yfloat)
	ax1.set_title("Graph of Data",fontsize=11)
	ax1.set_xlabel("x variable",fontsize=10)
	ax1.set_ylabel("y variable",fontsize=10)
	plt.plot(x_model, y_model)
	ax1.set_xlim(0,6)
	ax1.set_ylim(0,50)
	ax1.margins(y=0)
	ax1.grid()
	display(fig1, target='graph', append=False)
