# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:54:40 2016

@author: Javid
"""
from urllib.request import urlopen

def read_text():
    quotes=open("D:\Dropbox\Python Exercises\Course\movie_quotess.txt")
    contents_of_file=quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection=urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    print(output)
    connection.close()
    
    if output=="true":
        print("profanity detected")
    elif output=="false":
        print("no prfoanity")
    else:
        print("no document found")
        
read_text()