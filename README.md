# CS Senior Capstone Group-19
# Vehicle Occupancy Detection Utilizing Time-of-flight Cameras

This project was created to explore methods for reliably detecting the presence of an object or person in a vehicle. Future use of this project would be used to determine if a baby was left in a car and alert the necessary groups such as the car owner or emergency services. The files in this repository only perform background segmentation on .png files. We used YOLO for training a model and object detection/classification. This process is not included in the repo.

Both files require several dependencies:
  1. PIL
  2. Matplotlib
  3. OpenCV

The imported library named "formats" is a private library of code that is currently not available for public use. The files will not compile without it. This formats library is used to open and parse through the capture files to get the distance values.

The capture files that are used by the python files are generated using a proprietary camera and software. However these files could be replicated by creating a file with pixel distance values.

The first file takes ten frames from a capture file and averages the distance values for each pixel. It outputs this into Newbase.npy. This is then used by backSegmentation.py as a baseline. Any difference in pixel distance above a certain threshold will show up as white. Currently the segmentation will not pick up an object that is placed in front of a larger object.

To generate the numpy array file:

```baseSegmentation.py full-path-to-capture-file```

To perform background segmentation on the capture using Newbase.npy as a baseline.

```backSegmentation.py full-path-to-capture-file```
