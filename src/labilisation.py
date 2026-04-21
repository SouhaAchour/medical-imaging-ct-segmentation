import numpy as np
import matplotlib.pyplot as plt 
import math
from mpl_toolkits.mplot3d import Axes3D
import skimage as ski
import scipy.io as scio
from scipy import ndimage
from scipy.ndimage import binary_erosion

from skimage import measure
from scipy.ndimage import label, generate_binary_structure

data_array = scio.loadmat('data_matlab.mat')
print(data_array)
print(data_array['data_dicom'][0][0][1])
data = data_array['data_dicom'][0][0][1]
print(data.size)
print(type(data))
print(data.shape)
dilated = np.load("dilated.npy")
labeled_array = np.zeros_like(data)



labeled_array, num_features = label((dilated[:,:,90]) )

print("shapelabilistaion=",labeled_array.shape)
print("num_features=",num_features)

np.save('labeled_array.npy', labeled_array)
np.save('num_features.npy', num_features)

 
