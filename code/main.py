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
#from PyPDF2 import PdfFileWriter, PdfFileReader


if __name__ == '__main__': 
    
    #### Show full floor room layout
    #show_room_order(5) 
    
    
    #### NAVIGATE NAVITAS, AKA. NAVNAV
    run_navnav = 1
    if run_navnav == 1:
        # Getting user input
    
        print 'Which room do you want to go to? (e.g. 05.010)'
        user_input = raw_input()
        
        chosen_floor = int(user_input[0:2]) 
        room = int(user_input[3:])
        

        if chosen_floor > 7 or chosen_floor <0:
            print 
            sys.exit('Floor does not exist')
            
        if room < 0 or room > 250:
            print 
            sys.exit('Room does not exist')
        
        print 'Now locating floor ' + str(chosen_floor)+ ', room ' + str(room)
        
        # Now plotting location on map background
        search_room(chosen_floor,room)
        
        print 
        print 'Your map can be found in /maps/map_test.png'
        print 'Thank you for using NavNav'
        
        
    #### Create maps for toilet and print rooms
    extras = 0
    if extras == 1:
        
        # Loading coordinates
        mat = scipy.io.loadmat('navnav_coors_improved.mat')
        navnav_coors = np.array(mat['coors'])
        
        for xkg in ['kitchen','print','toilet']:
            for cnv in xrange(8):
                extra(xkg,cnv,navnav_coors)
 
     
    #### Create maps for webpage
    run_navnav_web = 0
    if run_navnav_web == 1:
        
        # Loading coordinates
        mat = scipy.io.loadmat('navnav_coors_improved.mat')
        navnav_coors = np.array(mat['coors'])
                
        for chosen_floor in xrange(8): 
        
            for room in xrange(250):
    
                
                # Now plotting location on map background
                search_room_web(chosen_floor,room,navnav_coors)
        
        print 
        print 'Your map can be found in /maps/map_test.png'
        print 'Thank you for using NavNav'    