import subprocess
import os
directory=input("Enter video directory: ")
destdir=input("Enter audio output directory: ")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".avi") or filename.endswith(".mp4"): 
        print("converting"+filename+" to WAV")
        command = "ffmpeg -i "+directory+"/" + filename +" -ab 160k -ac 2 -ar 44100 -vn "+ destdir+"/" + filename+".wav"
        subprocess.call(command, shell=True)
        print("done!")

