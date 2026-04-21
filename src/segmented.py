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

binaryData = np.zeros_like(data) 

for i in range(0,500):
    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            
                if data[i][j][k]>600:
                    binaryData[i][j][k] = 1
                
print(binaryData)
np.save('binary.npy',binaryData)
segmented = np.zeros_like(data) 

for i in range(0,300):
    for j in range(len(binaryData[i])):
        for k in range(len(binaryData[i][j])):
            
            
            if i!=0 and i!= len(binaryData)-1 and j!=0 and j!= len(binaryData[i])-1 and k!=0 and k!= len(binaryData[i][j])-1:
                
                neighbor=[binaryData[i+1][j][k],binaryData[i-1][j][k],binaryData[i][j][k-1],binaryData[i][j][k+1],binaryData[i][j-1][k],binaryData[i][j+1][k]]
                if binaryData[i][j][k]==1 and np.all(neighbor):
                    segmented[i][j][k] = 1

                
        
np.save('segmented.npy', segmented)
