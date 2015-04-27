# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:54:15 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sys
#import subprocess
#import os
#import win32api, win32con
#import time
#from pymouse import PyMouse
#from pykeyboard import PyKeyboard
#import pyscreenshot as ImageGrab
import scipy.io
from PIL import Image

    

def show_room_order(chosen_floor):    
    
    if chosen_floor == 2 :
            print 
            sys.exit('No data available for this floor')
    elif chosen_floor > 5 or chosen_floor <0:
        print 
        sys.exit('Floor does not exist')    
    
    
    mat = scipy.io.loadmat('navnav_coors_improved.mat')
    # n_data contain [360,91,72] i.e. degrees, days, turbines
    navnav_coors = np.array(mat['coors'])
    
    
    if chosen_floor == 0:
    
        # Floor 0
        scaling = 2.4
        add_x = -610#-450
        add_y = -130
    elif chosen_floor == 1:
        # Floor 1
        scaling = 2.4
        add_x = -610#-450
        add_y = -130
    elif chosen_floor == 3:
        # Floor 3
        scaling = 2.4
        add_x = -600#-450
        add_y = -100
        #chosen_floor = chosen_floor -1
    elif chosen_floor == 4: 
        # Floor 4
        scaling = 2.4
        add_x = -600#-450
        add_y = -85
        #chosen_floor = chosen_floor -1
    elif chosen_floor == 5:
        # Floor 5
        scaling = 2.4
        add_x = -610#-450
        add_y = -100
        #chosen_floor = chosen_floor -1
        
    if chosen_floor > 2:
        chosen_floor_data = chosen_floor -1
    else:
        chosen_floor_data = chosen_floor



    
    color_ = np.arange(len(navnav_coors[0,:,0]))
    

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=False)#, axisbg='#d5de9c')
    sc = ax.scatter(add_x+scaling*navnav_coors[chosen_floor_data,:,0],add_y+scaling*navnav_coors[chosen_floor_data,0,:],c = color_,alpha = 0.8, vmin = 0, vmax = 250)# colors[xc], alpha = 0.8)    

    ax.axis('off')
    plt.colorbar(sc)
    
        
    maps = Image.open('../maps/png/'+str(chosen_floor)+'.png')
        
    
    
    plt.imshow(maps,cmap='gray',vmin=0,vmax=255)
    
    plt.savefig('../maps/map_test.png',dpi = 400)
    
    print 
    print 'Your map can be found in /maps/map_test.png'
    print 'Thank you for using NavNav'
    return None


    

def search_room(chosen_floor,room):
    # Now searching through list for location
    mat = scipy.io.loadmat('navnav_coors_improved.mat')
    # n_data contain [360,91,72] i.e. degrees, days, turbines
    navnav_coors = np.array(mat['coors'])
    
    if chosen_floor == 0:
    
        # Floor 0
        scaling = 2.4
        add_x = -610#-450
        add_y = -130
    elif chosen_floor == 1:
        # Floor 1
        scaling = 2.4
        add_x = -610#-450
        add_y = -130
    elif chosen_floor == 3:
        # Floor 3
        scaling = 2.4
        add_x = -600#-450
        add_y = -100
        #chosen_floor = chosen_floor -1
    elif chosen_floor == 4: 
        # Floor 4
        scaling = 2.4
        add_x = -600#-450
        add_y = -85
        #chosen_floor = chosen_floor -1
    elif chosen_floor == 5:
        # Floor 5
        scaling = 2.4
        add_x = -610#-450
        add_y = -100
        #chosen_floor = chosen_floor -1
    

    if chosen_floor > 2:
        chosen_floor_data = chosen_floor -1
    else:
        chosen_floor_data = chosen_floor

    
    x_coor_room = add_x+scaling*navnav_coors[chosen_floor_data,room,0]
    y_coor_room = add_y+scaling*navnav_coors[chosen_floor_data,0,room]
    
    # Checking if room exist
    if np.isnan(x_coor_room) or np.isnan(y_coor_room):
        print 
        sys.exit('Room does not exist')
    
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    
    ax.scatter(x_coor_room,y_coor_room,color = 'r',alpha = 0.8, vmin = 0, vmax = 250)    
    ax.annotate('Room ' + str(room), (x_coor_room+50,y_coor_room+50))
    ax.axis('off')
    

    maps = Image.open('../maps/png/'+str(chosen_floor)+'.png')
        
    
    plt.imshow(maps,cmap='gray',vmin=0,vmax=255)
    
    plt.savefig('../maps/map_test.png',dpi = 400)
    

    