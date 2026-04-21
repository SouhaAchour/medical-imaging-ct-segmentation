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
np.save('data.npy', data)
erosed = np.load("erosed.npy")

dilated = np.zeros_like(data)


for i in range(0,300):
    for j in range(len(erosed[i])):
        for k in range(len(erosed[i][j])):
            
            
            if i!=0 and i!= len(erosed)-1 and j!=0 and j!= len(erosed[i])-1 and k!=0 and k!= len(erosed[i][j])-1:
                #neighbors.append(a[i+1],a[i-1],a[i][j+1],a[i][j-1],)
                neighbor=[erosed[i-1][j][k],erosed[i+1][j][k],erosed[i][j][k-1],erosed[i][j][k+1],erosed[i][j-1][k],erosed[i][j+1][k]]
                if erosed[i][j][k]==1:
                    dilated[i][j][k] = 1
                    dilated[i][j][k-1] = 1
                    dilated[i][j][k+1] = 1
                    
                    dilated[i][j+1][k] = 1
                    dilated[i][j-1][k] = 1

                    
np.save('dilated.npy', dilated)
