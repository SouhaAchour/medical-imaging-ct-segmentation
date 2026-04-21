import numpy as np
import matplotlib.pyplot as plt 
import math
from mpl_toolkits.mplot3d import Axes3D
import skimage as ski
import scipy.io as scio
from scipy import ndimage
from scipy.ndimage import binary_erosion

from skimage import measure



data_array = scio.loadmat('data_matlab.mat')
print(data_array)
print(data_array['data_dicom'][0][0][1])
data = data_array['data_dicom'][0][0][1]
print(data.size)
print(type(data))
print(data.shape)
segmented = np.load("segmented.npy")
erosed = np.zeros_like(data)


for i in range(0,300):
    for j in range(len(segmented[i])):
        for k in range(len(segmented[i][j])):
            if i!=0 and i!= len(segmented)-1 and j!=0 and j!= len(segmented[i])-1 and k!=0 and k!= len(segmented[i][j])-1:
               
                neighbor=[segmented[i-1][j][k],segmented[i+1][j][k],segmented[i][j][k-1],segmented[i][j][k+1],segmented[i][j-1][k],segmented[i][j+1][k]]
                if segmented[i][j][k]==1 and not(np.any(neighbor==0)):
                    erosed[i][j][k] = 1
                
np.save('erosed.npy',erosed)
