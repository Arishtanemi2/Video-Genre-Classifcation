import cv2     # for capturing videos
import math   # for mathematical operations
count = 1

import os
directory=input("Enter video directory: ")
destdir=input("Enter frames output directory: ")
framename=input("Enter frame name to save the frames as: ")
frameRate=int(input("Enter framerate to capture: "))
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".avi") or filename.endswith(".mp4"): 
        print("converting"+filename+" to frames")
        videoFile = directory+"/"+filename
        cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
        #frameRate = cap.get(5) #frame rate
        x=1
        while(cap.isOpened()):
            frameId = cap.get(1) #current frame number
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frameId % math.floor(frameRate) == 0):
                fname =destdir+'/'+framename+str(count)+".jpg"
                count+=1
                cv2.imwrite(fname, frame)
        cap.release()
        print ("Done!")

