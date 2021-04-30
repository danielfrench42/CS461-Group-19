# CS Senior Capstone Group-19
# Vehicle Occupancy Detection Utilizing Time-of-flight Cameras

Both files require several dependencies:
  1. PIL
  2. Matplotlib
  3. OpenCV

They also require access to library of code named formats. This is for parsing through a capture file. The library is not included in the repository.


To run the background segmentation on a capture file:

```baseSegmentation.py full-path-to-capture-file```

This will produce a numpy array file named Newbase.npy which will be used by NewSeg.py.

```NewSeg.py full-path-to-capture-file```

This will then perform background segmentation on the capture and produce a .png file for every frame in the capture.  
