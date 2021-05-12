# CS Senior Capstone Group-19
# Vehicle Occupancy Detection Utilizing Time-of-flight Cameras

Both files require several dependencies:
  1. PIL
  2. Matplotlib
  3. OpenCV

The imported library named "formats" is a private library of code that is used with this project. The files will not compile without it. This formats library is used to open and parse through the capture files to get the distance values.

The capture files that are used by the python files are generated using a proprietary camera and software.

To run the background segmentation on a capture file:

```baseSegmentation.py full-path-to-capture-file```

This will produce a numpy array file named Newbase.npy which will be used by NewSeg.py. The script takes the first ten frames of the capture file and averages the distance values of each pixel together. This is used as the baseline for NewSeg.py.

```NewSeg.py full-path-to-capture-file```

This will then perform background segmentation on the capture using Newbase.npy as the baseline. Any difference in pixel distance above a certain threshold will show up as white.
