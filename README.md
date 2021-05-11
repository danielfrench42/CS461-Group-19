# CS Senior Capstone Group-19
# Vehicle Occupancy Detection Utilizing Time-of-flight Cameras

Both files require several dependencies:
  1. PIL
  2. Matplotlib
  3. OpenCV

They also require access to library of code named formats. This is for parsing through a capture file. The library is not included in the repository.

The capture files that are used by the python files are generated using a proprietary camera and software.

To run the background segmentation on a capture file:

```baseSegmentation.py full-path-to-capture-file```

This will produce a numpy array file named Newbase.npy which will be used by NewSeg.py. The script takes the first ten frames of the capture file and averages the distance values of each pixel together. This is used as the baseline for NewSeg.py.

```NewSeg.py full-path-to-capture-file```

This will then perform background segmentation on the capture using Newbase.npy as the baseline. Any difference in pixel distance will show up as white.

These files can be used for training a model.
