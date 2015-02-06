"""
File: Constructors.py
Author: Brian Mansfield
Description: This file holds all the methods responsible for creating
new objects.
"""

import pygame, sys, time, math, random
from pygame.locals import *
from window_constants import *
from game_constants import *

def createNewRail( loc, image ):
    newrail = {}
    newrail['image'] = image
    newrail['width'] = RAILWIDTH
    newrail['height'] = RAILHEIGHT
    newrail['x'] = loc
    newrail['y'] = 0
    newrail['rect'] = pygame.Rect( (newrail['x'], newrail['y'],
                                    newrail['width'], newrail['height']) )
    return newrail

def createNewTreeline( treeimage, xcoord ):
    newtr = {}
    newtr['image'] = treeimage
    newtr['width'] = TREELINEWIDTH
    newtr['height'] = TREELINEHEIGHT
    newtr['x'] = xcoord
    newtr['y'] = 0
    newtr['rect'] = pygame.Rect( (newtr['x'], newtr['y'],
                                    newtr['width'], newtr['height']) )
    return newtr

def createGameOverScreen( image ):
    gameover = {}
    gameover['image'] = image
    gameover['width'] = WINWIDTH
    gameover['height'] = WINHEIGHT
    gameover['x'] = 0
    gameover['y'] = 0
    gameover['rect'] = pygame.Rect( (gameover['x'], gameover['y'],
                                    gameover['width'], gameover['height']) )
    return gameover

def createNewObstacle( type, image ):
    if type == 'tree':
        obstacle = {}
        obstacle['image'] = image
        obstacle['width'] = TREEWIDTH
        obstacle['height'] = TREEHEIGHT
        loc = random.randint(0,2)
        obstacle['x'] = RAILLOCATIONS[loc] + RAILWIDTH
        obstacle['y'] = 0 - TREEHEIGHT
        obstacle['rect'] = pygame.Rect( (obstacle['x'], obstacle['y'],
                                         obstacle['width'], obstacle['height']) )

    elif type == 'snow pile':
        obstacle = {}
        obstacle['image'] = image
        obstacle['width'] = SNOWPILEWIDTH
        obstacle['height'] = SNOWPILEHEIGHT
        loc = random.randint(0,2)
        obstacle['x'] = RAILLOCATIONS[loc] + RAILWIDTH
        obstacle['y'] = 0 - SNOWPILEHEIGHT
        obstacle['rect'] = pygame.Rect( (obstacle['x'], obstacle['y'],
                                         obstacle['width'], obstacle['height']) )
        print 'snow'
    
    return obstacle
