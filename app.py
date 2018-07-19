#change variable names

import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D

from collections import OrderedDict
from  matplotlib import pyplot as plt
import numpy as np
import csv


# READ DATA AND Z

# ask user for input files of data and index
inputFile = 'data.txt'
#raw_input("Enter the name of your matrix file: ") #ex: data.txt
inputFileNum = 'data2.txt'
#raw_input("Enter the name of vector file: ") #ex: data2.txt

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

n = len(data_input[0])

data_input  = np.array(data_input, dtype=np.float_)
data_input2 = np.array(data_input2, dtype=np.float_).flatten()

fig, axs = plt.subplots(n, n, subplot_kw={'projection': '3d'})

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
                for item in sorted_indexValues[key]:
                   flat_list.append(item)

                all_data.append(flat_list)

            #create list for keys
            x_values_keys = []
            for key in sorted_indexValues:
                x_values_keys.append(int(key))

            # plt.boxplot(all_data)
            axs[rowid][colid].boxplot(all_data, positions=x_values_keys)

            axs[rowid][colid].set_xlabel("Col " + str(rowid))
            axs[rowid][colid].set_ylabel("Value")
            axs[rowid][colid].set_zticklabels([])
            axs[rowid][colid].view_init(-90, -90)


            # axs[rowid][colid].set_xticklabels(rotation=30)
            

        elif (rowid < colid):
            axs[rowid][colid].plot_trisurf(data_input[:,rowid], data_input[:,colid], data_input2, linewidth=0.2, antialiased=True, )
            axs[rowid][colid].set_xlabel("Col " + str(rowid))
            axs[rowid][colid].set_ylabel("Col " + str(colid))
            axs[rowid][colid].set_zlabel("Vector")



plt.suptitle("Multiverse")
plt.show()


# , 7
# , 0
# , 3
# , 9
# , 2
# , 0
# , 9
# , 3
# , 2
# , 2
# , 8
# , 2
# , 5
# , 3
# , 3
# , 6
# , 3
# , 2
# , 6

