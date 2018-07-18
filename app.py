import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D

from collections import OrderedDict
from  matplotlib import pyplot as plt
import numpy as np
import csv


# READ DATA AND Z

# ask user for input files of data and index
inputFile = 'data.txt'
#raw_input("Enter the name of your input file (pay attention to path): ") #ex: data.txt
inputFileNum = 'data2.txt'
#raw_input("Enter the name of the file with corresponding values (pay attention to path): ") #ex: data2.txt

# create dictionary to add lists of values to
indexValues = {}
#create lists to add data to
data_input =[] #the matrix
data_input2 = [] #the vector

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

print (data_input)
print (data_input2)

################

n = len(data_input[0])

# fig, axs = plt.subplots(n, n, subplot_kw={'projection': '3d'})

for rowid in range(n):
	for colid in range(n):
		if (rowid == colid):
			#iterate through list of given data to add to dictionary indexValues
			for i in range(len(data_input)):
			    if data_input[i][rowid] in indexValues:
			        # append the corresponding value over in the other matrix
			        indexValues[data_input[i][rowid]].append(data_input2[i])
			    else:
			        #add the value to the list with identifier j[d] in the dictionary
			        indexValues[data_input[i][rowid]] = [data_input2[i]]

			# create ordered dictionary to sort indexValues with
			sorted_indexValues = OrderedDict()

			#sort indexValues
			for key in sorted(indexValues.iterkeys()):
			    sorted_indexValues[key]= indexValues[key]

			#create empty array to store arrays of data to plot
			all_data = []

			#convert all values in the dictionary from string to int
			for key in sorted_indexValues:

			    #flat list from list of lists
			    flat_list = []
			    for sublist in sorted_indexValues[key]:
			       for item in sublist:
			           flat_list.append(item)

			    testArrays = [int(i) for i in flat_list]
			    all_data.append(testArrays)

			#create list for keys
			x_values_keys = []
			for key in sorted_indexValues:
			    x_values_keys.append(int(key))

			print (sorted_indexValues)

			plt.subplot()

			# plt.boxplot(all_data)
			plt.boxplot(all_data, positions=x_values_keys)

		# elif (rowid < colid):
 	# 		axs[rowid*n + colid].plot_trisurf(data[:,rowid], data[:,colid], z, linewidth=0.2, antialiased=True)

	plt.show()

plt.show()