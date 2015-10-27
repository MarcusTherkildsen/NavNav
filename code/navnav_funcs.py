# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:54:15 2015

@author: Marcus Therkildsen
"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sys
import scipy.io
from PIL import Image
# import codecs
# import subprocess
# import os
# import win32api, win32con
# import time
# from pymouse import PyMouse
# from pykeyboard import PyKeyboard
# import pyscreenshot as ImageGrab


def navnav_extra(string, chosen_floor, navnav_coors, save_txt=0):

    # load string txt and plot the selected floor

    string_room = open(string+'.txt', 'r').read().split('\n')

    string_on_chosen_floor = []
    extra_text_on_chosen_floor = []
    # print string_room

    for ghj in xrange(len(string_room)):
        if string_room[ghj][1] == str(chosen_floor):
            string_on_chosen_floor.append(string_room[ghj][3:6])
            if string == 'print' or 'kitchen':
                extra_text_on_chosen_floor.append(string_room[ghj][9:-1])

    # print string_on_chosen_floor

    # Adjusting coordinates
    scaling, add_x, add_y = adjust_coors(chosen_floor)
    x_coor_room = add_x + scaling*navnav_coors[chosen_floor,
                                               string_on_chosen_floor, 0]
    y_coor_room = add_y+scaling*navnav_coors[chosen_floor,
                                             0,
                                             string_on_chosen_floor]

    # Correcting  placement of toilets
    if string == 'toilet':
        for vjk in xrange(len(string_on_chosen_floor)):
            if chosen_floor == 4 and string_on_chosen_floor[vjk] == '005':
                print 'Found it ! '
                x_coor_room[vjk] = x_coor_room[vjk]+30
                y_coor_room[vjk] = y_coor_room[vjk]-25
                string_on_chosen_floor[vjk] = '058'

            elif chosen_floor == 5 and string_on_chosen_floor[vjk] == '191':
                print 'Found it ! '
                x_coor_room[vjk] = x_coor_room[vjk]
                y_coor_room[vjk] = y_coor_room[vjk]-50
                string_on_chosen_floor[vjk] = '053'
    # getting an error here. It says that the data contains nans.
    # Does not make sense

    for fdc in xrange(len(x_coor_room)):
        x_coor_room[fdc] = int(float(x_coor_room[fdc]))
        y_coor_room[fdc] = int(float(y_coor_room[fdc]))
    if save_txt == 1:
        # Save these improved coordinates
        np.savetxt(str(chosen_floor)+'_'+string+'_coor_X.txt',
                   x_coor_room, fmt='%0.5f', delimiter=',')
        np.savetxt(str(chosen_floor)+'_'+string+'_coor_Y.txt',
                   y_coor_room, fmt='%0.5f', delimiter=',')

    print 'Now plotting '+str(string)+' on floor ' + str(chosen_floor)

    # Plotting dot in searched room
    fig, ax = plt.subplots()

    ax.scatter(x_coor_room, y_coor_room, color="#AA0000", vmin=0, vmax=250)
    man_leg_start = 980
    for fxc in xrange(len(x_coor_room)):

        if (extra_text_on_chosen_floor[fxc] == 'Stud.' or
            extra_text_on_chosen_floor[fxc] == 'Alle' or
                extra_text_on_chosen_floor[fxc] == 'AU'):

            # Manuel legend
            ax.plot(man_leg_start, 40+50*fxc, 'o', color='b',
                    markeredgecolor='b')
            ax.scatter(x_coor_room[fxc], y_coor_room[fxc], color='b',
                       vmin=0, vmax=250)

        else:
            # Manuel legend
            ax.plot(man_leg_start, 40+50*fxc, 'o', color="#AA0000",
                    markeredgecolor="#AA0000")

        # White numbers
        ax.annotate(str(fxc+1), (x_coor_room[fxc]-7, y_coor_room[fxc]+10),
                    color='w', fontsize=6)
        ax.annotate(str(fxc+1), (man_leg_start-6.5, 40+50*fxc+10),
                    color='w', fontsize=6)

        if extra_text_on_chosen_floor[fxc] == '':
            ax.annotate(string_on_chosen_floor[fxc], (man_leg_start+25,
                        40+50*fxc+10), color='k', fontsize=6)
        else:
            # print string_on_chosen_floor[fxc]#string_room[fxc][9:-1]
            # Room number
            ax.annotate(string_on_chosen_floor[fxc] + ', ' +
                        extra_text_on_chosen_floor[fxc],
                        (man_leg_start+25, 40+50*fxc+10),
                        color='k', fontsize=6)

    # ax.legend(scatterpoints=1)

    # Annotating room
    if string == 'kitchen':
        # The following lines are needed for the danish letter ø
        reload(sys)
        sys.setdefaultencoding('UTF-8')
        ax.annotate('0'+str(chosen_floor)+'.'+'køkken', (960, 0))
    else:
        ax.annotate('0'+str(chosen_floor)+'.'+str(string), (960, 0))

    ax.axis('off')

    # Loading map background
    maps = Image.open('../maps/final_png/'+str(chosen_floor)+'_png.png')

    # Plotting map background
    ax.imshow(maps, cmap='gray', vmin=0, vmax=255)

    # Saving final map
    plt.savefig('../maps/'+str(string)+'/'+str(chosen_floor)+'.jpg',
                dpi=400, bbox_inches='tight')

    print
    print 'Your map can be found in /maps/map_test.jpg'
    print 'Thank you for using NavNav'
    print

    return None


def adjust_coors(chosen_floor):

    # Negative x moves to the left, negative y moves upward

    if chosen_floor == 0:
        # Floor 0
        scaling = 1.28
        add_x = -380
        add_y = -160
    elif chosen_floor == 1:
        # Floor 1
        scaling = 1.35
        add_x = -410
        add_y = -238

    elif chosen_floor == 2:
        scaling = 1.59
        add_x = -590
        add_y = -410

    elif chosen_floor == 3:
        # Floor 3
        scaling = 1.282
        add_x = -680
        add_y = -160
        # chosen_floor = chosen_floor -1
    elif chosen_floor == 4:
        # Floor 4
        scaling = 1.28
        add_x = -388
        add_y = -166
        # chosen_floor = chosen_floor -1
    elif chosen_floor == 5:
        # Floor 5
        scaling = 1.217
        add_x = -430
        add_y = -114

    elif chosen_floor == 6:
        scaling = 1.75
        add_x = -660
        add_y = -244

    elif chosen_floor == 7:
        scaling = 1.75
        add_x = -660
        add_y = -244

    return scaling, add_x, add_y


def show_room_order(chosen_floor):

    if chosen_floor > 7 or chosen_floor < 0:
        print
        sys.exit('Floor does not exist')

    # Loading coordinates
    mat = scipy.io.loadmat('navnav_coors_improved.mat')
    navnav_coors = np.array(mat['coors'])

    # Adjusting coordinates
    scaling, add_x, add_y = adjust_coors(chosen_floor)

    # Preparing colorbar
    color_ = np.arange(len(navnav_coors[0, :, 0]))

    # Plotting all rooms on the selected floor
    plt.figure()
    plt.scatter(add_x+scaling*navnav_coors[chosen_floor, :, 0],
                add_y+scaling*navnav_coors[chosen_floor, 0, :],
                c=color_, vmin=0, vmax=250)
    plt.axis('off')
    cb = plt.colorbar()

    # Removes white lines in colorbar
    cb.solids.set_edgecolor("face")

    # Loading map background
    maps = Image.open('../maps/final_png/'+str(chosen_floor)+'_png.png')

    # Plotting map background
    plt.imshow(maps, cmap='gray', vmin=0, vmax=255)

    # Saving final map
    plt.savefig('../maps/map_test.jpg', dpi=400, bbox_inches='tight')

    print
    print 'Your map can be found in /maps/map_test.jpg'
    print 'Thank you for using NavNav'
    return None


def search_room(chosen_floor, room):

    # Loading coordinates
    mat = scipy.io.loadmat('navnav_coors_improved.mat')
    navnav_coors = np.array(mat['coors'])

    # Adjusting coordinates
    scaling, add_x, add_y = adjust_coors(chosen_floor)
    x_coor_room = add_x+scaling*navnav_coors[chosen_floor, room, 0]
    y_coor_room = add_y+scaling*navnav_coors[chosen_floor, 0, room]

    # Checking if room exist
    if np.isnan(x_coor_room) or np.isnan(y_coor_room):
        print
        sys.exit('Room does not exist')

    # Plotting dot in searched room
    plt.figure()
    plt.scatter(x_coor_room, y_coor_room, color="#AA0000", vmin=0, vmax=250)

    # Annotating room
    gsd = len(str(room))
    if gsd == 1:
        plt.annotate('0' + str(chosen_floor) + '.00' + str(room), (960, 0))
    if gsd == 2:
        plt.annotate('0' + str(chosen_floor) + '.0' + str(room), (960, 0))
    if gsd == 3:
        plt.annotate('0' + str(chosen_floor) + '.' + str(room), (960, 0))

    plt.axis('off')

    # Loading map background
    maps = Image.open('../maps/final_png/'+str(chosen_floor)+'_png.png')

    # Plotting map background
    plt.imshow(maps, cmap='gray', vmin=0, vmax=255)

    # Saving final map
    plt.savefig('../maps/map_test.jpg', dpi=400, bbox_inches='tight')

    return None


def search_room_web(chosen_floor, room, navnav_coors):

    # Adjusting coordinates
    scaling, add_x, add_y = adjust_coors(chosen_floor)
    x_coor_room = add_x+scaling*navnav_coors[chosen_floor, room, 0]
    y_coor_room = add_y+scaling*navnav_coors[chosen_floor, 0, room]

    # Checking if room exist
    if np.isnan(x_coor_room) or np.isnan(y_coor_room):
        print 'Room does not exist, will not be saving an image '
        return
    else:
        print 'Now plotting floor ' + str(chosen_floor)+', room ' + str(room)

    # Plotting dot in searched room
    plt.figure()
    plt.scatter(x_coor_room, y_coor_room, color="#AA0000", vmin=0, vmax=250)

    # Annotating room
    gsd = len(str(room))
    if gsd == 1:
        plt.annotate('0' + str(chosen_floor) + '.00' + str(room), (960, 0))
    if gsd == 2:
        plt.annotate('0' + str(chosen_floor) + '.0' + str(room), (960, 0))
    if gsd == 3:
        plt.annotate('0' + str(chosen_floor) + '.' + str(room), (960, 0))

    plt.axis('off')

    # Loading map background
    maps = Image.open('../maps/final_png/'+str(chosen_floor)+'_png.png')

    # Plotting map background
    plt.imshow(maps, cmap='gray', vmin=0, vmax=255)

    # Saving final map
    plt.savefig('../maps/navnav_web_jpg/' + str(chosen_floor) + '/' +
                str(room) + '.jpg', dpi=400, bbox_inches='tight')
    # plt.savefig('../maps/navnav_web_svg/' + str(chosen_floor) + '/' +
    #            str(room)+'.svg', bbox_inches='tight')
    plt.close('all')

    return None
