import numpy as np
import matplotlib.pyplot as plt

binary = np.load("binary.npy")
segmented = np.load("segmented.npy")
erosed = np.load("erosed.npy")
data = np.load("data.npy")
dilated = np.load("dilated.npy")
labeled_array = np.load("labeled_array.npy")
num_features = np.load("num_features.npy")

unique_values, counts = np.unique(data, return_counts=True)

listofvalue = []
listofcount= []

# Print the results
for value, count in zip(unique_values, counts):
    #print(f"{value} occurs {count} times")
    listofvalue.append(value)
    listofcount.append(count)
    

unique_values_seg, counts_seg = np.unique(segmented, return_counts=True)

listofvalueseg = []
listofcountseg= []

# Print the results
for value, count in zip(unique_values_seg, counts_seg):
    #print(f"{value} occurs {count} times")
    listofvalueseg.append(value)
    listofcountseg.append(count)
    
print("count",len(listofcountseg)) 
print("value",len(listofvalueseg)) 


unique_values_erosed, counts_erosed = np.unique(erosed, return_counts=True)

listofvalueerosed = []
listofcounterosed= []

# Print the results
for value, count in zip(unique_values_erosed, counts_erosed):
    #print(f"{value} occurs {count} times")
    listofvalueerosed.append(value)
    listofcounterosed.append(count)
    
print("count",len(listofcounterosed)) 
print("value",len(listofvalueerosed)) 
unique_values_dilated, counts_dilated = np.unique(dilated, return_counts=True)

listofvaluedilated = []
listofcountdilated= []

# Print the results
for value, count in zip(unique_values_dilated, counts_dilated):
    #print(f"{value} occurs {count} times")
    listofvaluedilated.append(value)
    listofcountdilated.append(count)
    
print("count",len(listofcountdilated)) 
print("value",len(listofvaluedilated)) 

unique_values_labeled_array, counts_labeled_array = np.unique(labeled_array, return_counts=True)

listofvaluelabeled_array = []
listofcountlabeled_array= []

# Print the results
for value, count in zip(unique_values_labeled_array, counts_labeled_array):
    #print(f"{value} occurs {count} times")
    listofvaluelabeled_array.append(value)
    listofcountlabeled_array.append(count)
    
print("count",len(listofvaluelabeled_array)) 
print("value",len(listofvaluelabeled_array))


  

plt.title("histogramsegmented") 
# Adds a subplot at the 1sr position data
plt.subplot(521) 
# showing image data
plt.imshow(data[:, :, 99]) 
plt.title("data")

# Add a subplot at the 2nd position histogram data
plt.subplot(522) 
# showing image data
plt.bar(listofvalue,listofcount)
plt.title("histogram data")
 
# Adds a subplot at the 3nd position 
plt.subplot(523) 
# showing image segmented
plt.imshow(segmented[:, :, 99]) 

plt.title("Segmented") 
# Adds a subplot at the 4nd position histogram data
plt.subplot(524) 
# showing image data
plt.bar(listofvalueseg,listofcountseg)
plt.title("histogram segmented")

# Adds a subplot at the 5rd position 
plt.subplot(525) 
  
# showing image erosed
plt.imshow(erosed[:, :, 99]) 

plt.title("erosed") 

plt.subplot(526) 

# showing image data
plt.bar(listofvalueerosed,listofcounterosed)
plt.title("histogram erosed")



plt.subplot(527) 
plt.imshow(dilated[:, :, 99]) 

plt.title("dilated") 

# showing image data
plt.subplot(528) 

plt.bar(listofvaluedilated,listofcountdilated)
plt.title("histogram dilated")
plt.subplot(529) 
plt.imshow(labeled_array) 

plt.title("labeled_array")


plt.subplot(5, 2, 10)

plt.bar(listofvaluelabeled_array,listofcountlabeled_array) 
plt.title("histogram labilisation")


plt.show()