# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 23:44:22 2016

@author: Javid
"""
import os
from string import digits

def rename_files():
    file_list=os.listdir(r"D:\Dropbox\Python Exercises\Course\prank\prank")
    #print(file_list)
    saved_path=os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir("D:\Dropbox\Python Exercises\Course\prank\prank")
    remove_digits=str.maketrans('','',digits)
    for file_name in file_list:
        os.rename(file_name,file_name.translate(remove_digits))
    os.chdir(saved_path)
rename_files()

