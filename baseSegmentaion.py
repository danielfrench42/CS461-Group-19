#!/usr/bin/env python3

# This script will prepare a base image to be used with background segmentation
# 1.	Read in capture file
# 2.	Set to first frame where vehicle is empty
# 3.	loop through steps 4-6 for each frame (Approx 10 frames)
# 4.	Get indices where amplitude is less than 30
# 5.	Set distance values to 0 at found indices
# 6.	Add current frame to first_frame
# 7.	Divide first frame by number of frames used to get average distance
# 8.	Save first_frame as numpy array file


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
	return parser.parse_args()

def main():
	# get capture file
	args = parse_args()
	fileName = args.filename[0]
	print(fileName)
	
	#Read capture file
	captureReader = CaptureReader(fileName)
	captureReader.Seek(1778) #This is the index where the car is empty in person.capture
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
    
	first_frame = []
	
	# This will create an image for each frame. Appx 10 frames per second
	for i in range(10):
		#Frame iterator
		frameIndex, timestamp, integrationTime, statusFlags, frameData = captureReader.GetNextFrame()
		print("frameIndex: ", frameIndex)
		
		#Get distance and amplitude data
		dist_arr = phaseConverter.PhaseToDistance_meters(frameData[0])
		amp_arr = frameData[1]

		#Set value to 0 where amplitude is low
		#This helps clear up noise from outside vehicle
		low = amp_arr < 30
		dist_arr[low] = 0

		if(i==0):
			first_frame = dist_arr
		else:
			first_frame += dist_arr
		
			
	first_frame /= 10	
			
	content = str(first_frame)
	np.save("Newbase.npy", first_frame)		
	#frame = np.load("Newbase.npy", allow_pickle=True)
	#print(frame.shape)

if __name__ == '__main__':
	main()