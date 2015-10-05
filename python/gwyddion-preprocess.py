__author__ = 'Philipp Oertle'

import csv
import numpy as np
import tkinter as tk
from tkinter import filedialog
import  scipy.stats as stats

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilenames()
fileLength = 0

#-------------------------------------------------------Process the height file-------------------------------------------------------

with open(file[0], newline='') as csvfile:
        heightMap = csv.reader(csvfile, delimiter='\t')
        i = 0
        for row in heightMap:
            i += 1
        fileLength = i

chArray_np = np.zeros(shape=(fileLength, fileLength))


with open(file[0], newline='') as csvfile:
        heightMap = csv.reader(csvfile, delimiter='\t')
        i = 0
        for row in heightMap:
            try:
                chArray_np[i] = row
                i += 1
            except ValueError:
                print(row[1] + ' is no number!')

#Rotate 90 clockwise and negate height map
chArray_np = np.rot90(-1*chArray_np,3)

col_mean = stats.nanmedian(chArray_np,axis=0)
inds = np.where(np.isnan(chArray_np))
chArray_np[inds] = np.take(col_mean,inds[1])

ninetyFive = np.percentile(chArray_np,[5,95],axis=0)
print(ninetyFive)


with open(file[0] + '-processed', 'w', newline='') as csvfile:
    twodMapProcessed = csv.writer(csvfile, delimiter='\t')
    for row in chArray_np:
        twodMapProcessed.writerow(row)

#-------------------------------------------------------Process the stiffness file-------------------------------------------------------

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilenames()
print(file[0])

with open(file[0], newline='') as csvfile:
        stiffnessMap = csv.reader(csvfile, delimiter='\t')
        i = 0
        for row in stiffnessMap:
            i += 1
        fileLength = i

chArray_np = np.zeros(shape=(fileLength, fileLength))


with open(file[0], newline='') as csvfile:
        stiffnessMap = csv.reader(csvfile, delimiter='\t')
        i = 0
        for row in stiffnessMap:
            try:
                chArray_np[i] = row
                i += 1
            except ValueError:
                print(row[1] + ' is no number!')

#Rotate 90 clockwise and negate height map
chArray_np = np.rot90(chArray_np,3)

col_mean = stats.nanmedian(chArray_np,axis=0)
inds = np.where(np.isnan(chArray_np))
chArray_np[inds] = np.take(col_mean,inds[1])

with open(file[0] + '-processed', 'w', newline='') as csvfile:
    twodMapProcessed = csv.writer(csvfile, delimiter='\t')
    for row in chArray_np:
        twodMapProcessed.writerow(row)