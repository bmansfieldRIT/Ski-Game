"""
File: constants.py
Author: Brian Mansfield
Description:Holds all game-related constants. All constants related to running
the main game window are held in blizzard.py, the main module
"""

from window_constants import *

# Color constants
SNOWBACKGROUND = (255, 255, 255) # white
BLUE = (0, 0, 255)

"""
These constants represent the relative path of the
images from the working directory.
"""
# The player image
PLAYERIMAGE = 'images/skiman.bmp'

# The initial rail image, and a variable path for animation
RAILIMAGE = 'images/rail.bmp'
RAILIMAGES = 'images/rail%s.bmp'

# Treeline images
LTREELINEIMAGE = 'images/lefttreeline1.bmp'
RTREELINEIMAGE = 'images/righttreeline.bmp'

# Images for surfaces other than the main display
GAMEOVERIMAGE = 'images/gameover.bmp'

# Obstacle images
TREEOBSTACLEIMAGE = 'images/treeobstacle.bmp'
SNOWPILEOBSTACLEIMAGE = 'images/snowpile.bmp'

# Images representing the health of the player
ZEROHEARTSIMAGE = 'images/zerohearts.bmp'
ONEHEARTIMAGE = 'images/oneheart.bmp'
TWOHEARTSIMAGE = 'images/twohearts.bmp'
THREEHEARTSIMAGE = 'images/threehearts.bmp'

# Dimensions of the main field objects
PLAYERWIDTH = 40
PLAYERHEIGHT = 60
RAILWIDTH = 10
RAILHEIGHT = 480
TREELINEWIDTH = 50
TREELINEHEIGHT = WINHEIGHT

# Game Over Time
GAMEOVERTIME = 6

# Dimensions of the player UI
HEARTSHEIGHT = 25
HEARTSWIDTH = 83

# Dimensions of obstacles
TREEHEIGHT = 63
TREEWIDTH = 43
SNOWPILEWIDTH = 49
SNOWPILEHEIGHT = 19

# Attributes of the player
STARTHEALTH = 3

# Locations to place player and obstacles
RAIL = (WINWIDTH) / 4 # separate the screen into 4 sections
LEFT_RAIL = RAIL * 1
CENTER_RAIL = RAIL * 2
RIGHT_RAIL = RAIL * 3

RAILLOCATIONS = []
RAILLOCATIONS.append(LEFT_RAIL)
RAILLOCATIONS.append(CENTER_RAIL)
RAILLOCATIONS.append(RIGHT_RAIL)

# Location to place the player object
PLAYERSTARTX = CENTER_RAIL + RAILWIDTH
PLAYERSTARTY = WINHEIGHT - PLAYERHEIGHT

# Locations to place the player UI
HEARTSXOFFSET = TREELINEWIDTH
HEARTSYOFFSET = WINHEIGHT - HEARTSHEIGHT - 20

# Rate of change for animations
RAILCHANGE = FPS/30 # rail moves 10 times every second
OBSTACLECHANGE = FPS/30

# Boundary values for random obstacle generation
MIN_OBST_GEN_TIME = FPS/5
MAX_OBST_GEN_TIME = FPS * 5

# Max number of obstacles on field
MAX_OBST_ON_FIELD = 10
