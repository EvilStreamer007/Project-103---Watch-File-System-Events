from fileinput import filename
import sys
import time
import random

import os 
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from datetime import datetime

fromDir = '/Users/chaitalishah/'

dirTree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class fileMovement(FileSystemEventHandler):
    def on_created(self,event):
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        print("Hey",{event.src_path},"was created at",currentTime,"!")
    
    def on_modified(self, event):
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        print("Hey",{event.src_path},"was modified at",currentTime,"!")
    
    def on_moved(self, event):
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        print("Hey",{event.src_path},"was moved to a new location at",currentTime,"!")
    
    def on_deleted(self, event):
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        print("Hey",{event.src_path},"was deleted at",currentTime,"!")

eventHandler = fileMovement()
Observer1 = Observer()
Observer1.schedule(eventHandler,fromDir,recursive = True)
Observer1.start()

try:
    while True:
        time.sleep(3)
        print("Working..")
except KeyboardInterrupt:
    Observer1.stop()
    print("\nProgram Ended.")