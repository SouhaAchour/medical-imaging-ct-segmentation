#  Medical Imaging - CT Scan Segmentation

##  Project Overview
This project focuses on CT scan segmentation using Python and basic image processing techniques.

The objective is to isolate meaningful anatomical structures from CT data using thresholding, neighborhood filtering, erosion, dilation, connected component labeling, and visualization.

---

##  Objectives
- Load and process CT scan data
- Perform threshold-based segmentation
- Apply erosion and dilation
- Label connected regions
- Visualize intermediate and final outputs
- Compare segmentation quality through histograms and image slices

---

##  Tools & Technologies
- Python
- NumPy
- SciPy
- Matplotlib
- scikit-image


---

##  Skills Demonstrated
- Medical image processing
- CT scan segmentation
- Thresholding
- Morphological operations
- Connected component labeling
- NumPy-based array manipulation
- Data visualization

---


## Workflow
Load CT data from MATLAB format
Apply thresholding to obtain a binary volume
Perform segmentation using neighborhood conditions
Apply erosion to remove noise
Apply dilation to reconnect structures
Label connected components
Visualize slices and histograms of intermediate outputs

---

## Results

The project demonstrates how classical image processing techniques can be applied to CT scan data to isolate relevant structures and analyze segmentation quality.

---

##  Data

Due to size limitations, the original CT dataset and intermediate results (.npy files) are not included in this repository.

The project was developed using CT scan data stored in `.mat` and `.npy` formats.

---

## Context

This is an academic project in medical imaging and image processing.

---

## Conclusion

This project highlights how Python can be used to process medical images through segmentation, morphological filtering, connected component labeling, and visualization
