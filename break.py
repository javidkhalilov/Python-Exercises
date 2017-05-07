# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 23:05:24 2016

@author: Javid
"""
import webbrowser
import time

totalTimeCount=3
breakCount=0
print("This program started in "+time.ctime())
while breakCount<totalTimeCount:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=OT2bxfGC4UA")
    breakCount=breakCount+1