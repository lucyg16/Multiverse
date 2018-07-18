import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D

from collections import OrderedDict
from  matplotlib import pyplot as plt
import numpy as np
import csv

# READ DATA AND Z
#create lists to add data to
data_input =[] #the matrix
data_input2 = [] #the vector

inputFile = 'data.txt'
inputFileNum = 'data2.txt'

#read the input file data
with open (inputFile, 'rb') as csvfile:
	inputData = csv.reader(csvfile)
	for row in inputData:
		data_input.append(row)

#read the input file data2
with open (inputFileNum, 'rb') as csvfile:
	inputData2 = csv.reader(csvfile)
	for row in inputData2:
			data_input2.append(row)

#remove whitespaces in data
for item in data_input:
	for i in range(len(item)):
		item[i] = item[i].replace(" ","")

#remove whitespaces in data2
for item in data_input2:
	for i in range(len(item)):
		item[i] = item[i].replace(" ","")

n = len(data_input[0])

data_input  = np.array(data_input, dtype=np.float_)
data_input2 = np.array(data_input2, dtype=np.float_).flatten()

fig, axs = plt.subplots(n, n, subplot_kw={'projection': '3d'})

for rowid in range(n):
	for colid in range(n):
		if (rowid == colid):
			print ('Hello')
		elif (rowid < colid):
			print(data_input[:,rowid].shape, data_input[:,colid].shape, data_input2.shape)
			axs[rowid][colid].plot_trisurf(data_input[:,rowid], data_input[:,colid], data_input2, linewidth=0.2, antialiased=True)

plt.show()


