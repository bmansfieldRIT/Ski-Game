"""
File: Constructors.py
Author: Brian Mansfield
Description: This file holds all the methods responsible for creating
new objects.
"""

import pygame, sys, time, math, random
from pygame.locals import *

import game_constants
from window_constants import *

def createNewRail( loc, image ):
    newrail = {}
    newrail['image'] = image
    newrail['width'] = game_constants.RAILWIDTH
    newrail['height'] = game_constants.RAILHEIGHT
    newrail['x'] = loc
    newrail['y'] = 0
    newrail['rect'] = pygame.Rect( (newrail['x'], newrail['y'],
                                    newrail['width'], newrail['height']) )
    return newrail

def createNewTreeline( treeimage, xcoord ):
    newtr = {}
    newtr['image'] = treeimage
    newtr['width'] = game_constants.TREELINEWIDTH
    newtr['height'] = game_constants.TREELINEHEIGHT
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
        obstacle['width'] = game_constants.TREEWIDTH
        obstacle['height'] = game_constants.TREEHEIGHT
        loc = random.randint(0,2)
        obstacle['x'] = game_constants.RAILLOCATIONS[loc] + game_constants.RAILWIDTH
        obstacle['y'] = 0 - game_constants.TREEHEIGHT
        obstacle['rect'] = pygame.Rect( (obstacle['x'], obstacle['y'],
                                         obstacle['width'], obstacle['height']) )

    elif type == 'snow pile':
        obstacle = {}
        obstacle['image'] = image
        obstacle['width'] = game_constants.SNOWPILEWIDTH
        obstacle['height'] = game_constants.SNOWPILEHEIGHT
        loc = random.randint(0,2)
        obstacle['x'] = game_constants.RAILLOCATIONS[loc] + game_constants.RAILWIDTH
        obstacle['y'] = 0 - game_constants.SNOWPILEHEIGHT
        obstacle['rect'] = pygame.Rect( (obstacle['x'], obstacle['y'],
                                         obstacle['width'], obstacle['height']) )
        print ('snow')
    
    return obstacle
