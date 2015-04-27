# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:19:01 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sys
import subprocess
import os
from navnav_funcs import *
import time
import scipy.io
from PyPDF2 import PdfFileWriter, PdfFileReader


if __name__ == '__main__': 
    
    # Show full floor room layout
    #show_room_order(5) 
    
    
### NAVIGATE NAVITAS, AKA. NAVNAV
    run_navnav = 1
    if run_navnav == 1:
        # Getting user input
    
        print 'Which room do you want to go to? (e.g. 05.010)'
        user_input = raw_input()
        
        chosen_floor = int(user_input[0:2]) 
        room = int(user_input[3:])
        
        #print 'Which floor do you want to go to? (e.g. 5)'
        #chosen_floor = int(raw_input())
        
        if chosen_floor == 2 :
            print 
            sys.exit('No data available for this floor')
        elif chosen_floor > 5 or chosen_floor <0:
            print 
            sys.exit('Floor does not exist')
            
        #print 'Which room do you want to go to? (e.g. 104)'
        #room = int(raw_input())
        
        if room < 0 :
            print 
            sys.exit('Room does not exist')
        
        print 'Now locating floor ' + str(chosen_floor)+ ', room ' + str(room)
        
        # Now plotting location on map background
        search_room(chosen_floor,room)
        
        print 
        print 'Your map can be found in /maps/map_test.png'
        print 'Thank you for using NavNav'
    
    
    
    

    