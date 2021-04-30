#!/usr/bin/env python3
import os
import sys
import numpy as np
from formats.capture import CaptureReader
from formats.create_csv import CreateCsv 
from formats.utility.files import GetPostFileName, GetCaptureFiles
from formats.post_settings import GetPostSettingsFromFile
from formats.utility.version import Version
from PIL import Image as im
import matplotlib.pyplot as plt
import cv2 as cv
import argparse


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', nargs=1, help='name of file to process')
	#parser.add_argument('baseimg', nargs=1, help='name of image to be the reference')
	return parser.parse_args()

def main():
	print("Starting segmentation")
	# get capture files
	args = parse_args()
	print(f'process {args.filename[0]}')
	fileName = args.filename[0]
	print(fileName)
	
	#Get name for images
	idx = fileName.index(".")
	name = fileName[:idx]
	print("name: ", name)
	
	#get base image 
	first_frame = np.load("Newbase.npy", allow_pickle=True)
	
	#Read capture file
	captureReader = CaptureReader(fileName)
	captureReader.Seek(0)
	captureSettings = captureReader.GetCaptureSettings()

	# Load PostSettings sidecar file
	postSettings = GetPostSettingsFromFile(
		fileName,
		captureSettings.sensorSettings.modulationFrequencyDivider,
		Version(0, 0, 0))

	# Get capture information
	frameWidth = captureReader.GetCapturedWidth()
	frameHeight = captureSettings.sensorSettings.GetCapturedHeight()
	frameCount = int(captureReader.GetFrameCount())

	phaseConverter = postSettings.filterSettings.phaseConverter
    

	# This will create an image for each frame. Appx 10 frames per second
	for i in range(frameCount):
		#Frame iterator
		frameIndex, timestamp, integrationTime, statusFlags, frameData = captureReader.GetNextFrame()
		
		dist_arr = phaseConverter.PhaseToDistance_meters(frameData[0])
		amp_arr = frameData[1]

		#find amplitude spots that are too low
		low = amp_arr < 30

		dist_arr[low] = 0

		dif = np.absolute(dist_arr - first_frame)
			
		#avg = np.mean(dif)
			
		delta = 0.1 #value in meters when using distance
		change = dif >= delta
		remove = dif <= delta
		dif[change] = 255
		dif[remove] = 0
		pic = np.fliplr(dif)

		blur = cv.blur(pic,(5,5))
		img_name = name + "_" + str(i) + ".png"
			
		data = im.fromarray(blur.astype(np.ubyte))
		data.save(img_name)

if __name__ == '__main__':
	main()