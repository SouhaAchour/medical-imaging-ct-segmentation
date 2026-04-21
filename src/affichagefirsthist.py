import numpy as np
import matplotlib.pyplot as plt

data = np.load("data.npy")


unique_values, counts = np.unique(data, return_counts=True)

listofvalue = []
listofcount= []

# Print the results
for value, count in zip(unique_values, counts):
    #print(f"{value} occurs {count} times")
    listofvalue.append(value)
    listofcount.append(count)

plt.bar(listofvalue,listofcount)
plt.title("histogram data")
plt.show()