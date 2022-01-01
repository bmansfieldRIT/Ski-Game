"""	File: Blizzard.py
	Author: Brian Mansfield
	This file is the game loop, the main logic of the game and
	object interactions go here.
"""

import pygame, sys, getopt, time, math, random
from pygame.locals import *
from window_constants import *
from game_constants import *
from constructors import *


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

# Images representing the health of the player
ZEROHEARTSIMAGE = 'images/zerohearts.bmp'
ONEHEARTIMAGE = 'images/oneheart.bmp'
TWOHEARTSIMAGE = 'images/twohearts.bmp'
THREEHEARTSIMAGE = 'images/threehearts.bmp'

SNOWPILEOBSTACLEIMAGE = 'images/snowpile.bmp'

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

def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('BLIZZARD!')
    
    while True:
        runGame()

    DEBUG = false # change this variable to initialize debug mode

def runGame():
    global railImages, railPositions, railnumber
    
    # load the image files
    PLAYER_IMG = pygame.image.load(PLAYERIMAGE)
    RAIL_IMG = pygame.image.load(RAILIMAGE)
    LTREELINE_IMG = pygame.image.load(LTREELINEIMAGE)
    RTREELINE_IMG = pygame.image.load(RTREELINEIMAGE)
    TREE_IMG = pygame.image.load(TREEOBSTACLEIMAGE)
    SNOWPILE_IMG = pygame.image.load(SNOWPILEOBSTACLEIMAGE)
    ZEROHEARTS_IMG = pygame.image.load(ZEROHEARTSIMAGE)
    ONEHEART_IMG = pygame.image.load(ONEHEARTIMAGE)
    TWOHEARTS_IMG = pygame.image.load(TWOHEARTSIMAGE)
    THREEHEARTS_IMG = pygame.image.load(THREEHEARTSIMAGE)
    GAMEOVER_IMG = pygame.image.load(GAMEOVERIMAGE)
    
    
    # Initialize all data structs
    player = {'surface': pygame.transform.scale(PLAYER_IMG,
                                                (PLAYERWIDTH, PLAYERHEIGHT)),
        'x' : PLAYERSTARTX,
        'y' : PLAYERSTARTY,
        'width' : PLAYERWIDTH,
        'height' : PLAYERHEIGHT,
        'health' : STARTHEALTH }
    
    railImages = []
    for i in range(3):
        railImages.append(RAIL_IMG)
    railnumber = 1
    
    
    rails = []
    rails.append(createNewRail(LEFT_RAIL, RAIL_IMG))
    rails.append(createNewRail(CENTER_RAIL, RAIL_IMG))
    rails.append(createNewRail(RIGHT_RAIL, RAIL_IMG))

    # Trees alongside the edge of the screen
    treelines = []
    treelines.append(createNewTreeline(LTREELINE_IMG, 0))
    treelines.append(createNewTreeline(RTREELINE_IMG, WINWIDTH - 35))

    # Create Game Over Screen
    gameOverScreen = createGameOverScreen(GAMEOVER_IMG)
    
    # Create structure to hold types of obstacles
    Obstacles = []
    Obstacles.append("") # indexing for this structure starts at 1
    treeobj = { 'type' : 'tree',
                'image' : TREE_IMG}
    Obstacles.append(treeobj)
    snowpileobj = { 'type' : 'snow pile',
                    'image' : SNOWPILE_IMG}
    Obstacles.append(snowpileobj)
    numObstacles = 2

    # Structure to hold the current obstacles on the field
    obstaclesOnField = []
    numObstaclesOnField = 0

    # Structure to hold the player health UI
    Hearts = []
    Hearts.append(ZEROHEARTS_IMG)
    Hearts.append(ONEHEART_IMG)
    Hearts.append(TWOHEARTS_IMG)
    Hearts.append(THREEHEARTS_IMG)

    # Initialize player movement vars used in main game loop
    moveLeft = False
    moveRight = False
        
    ##### Main Game Loop #####

    # Initialize game-related incrementers
    railtick = 1
    obstacletick = 1
    obstgentick = 1
    gameOverStartTime = 0
    
    while True:
        
        # Display all images related to the main playing field
        DISPLAYSURF.fill(SNOWBACKGROUND)
        for treeline in treelines:
            DISPLAYSURF.blit(treeline['image'], treeline['rect'])
        for rail in rails:
            DISPLAYSURF.blit(rail['image'], rail['rect'])

        # Display player UI
        DISPLAYSURF.blit(Hearts[player['health']], pygame.Rect( (HEARTSXOFFSET,
                                                        HEARTSYOFFSET,
                                                        HEARTSWIDTH,
                                                        HEARTSHEIGHT) ))
        # Display obstacles on field
        for obst in obstaclesOnField:
            DISPLAYSURF.blit(obst['image'], obst['rect'])

        # Display player object
        DISPLAYSURF.blit(player['surface'], pygame.Rect( (player['x'], player['y'],
                                                          player['width'], player['height']) ))
        
        # Display Game Over screen if condition is reached
        # CAUTION:  GAME OVER SCREEN MUST ALWAYS BE LAST SURFACE DISPLAYED
        if player['health'] == 0:
            DISPLAYSURF.blit(gameOverScreen['image'], gameOverScreen['rect'])
            if time.time() - gameOverStartTime > GAMEOVERTIME:
                terminate()

        # Collision detector
        if numObstaclesOnField > 0:
            for obstacle in obstaclesOnField:
                if obstacle['x'] == player['x'] and (obstacle['y'] +
                                                 obstacle['height']) == player['y']:
                    player['health'] -= 1

        # Determine if game over condition is reached, set gameOverStartTime
        # to current time
        if player['health'] == 0 and gameOverStartTime == 0:
            gameOverStartTime = time.time()

        # Load next rail image for animated effect
        if railtick == RAILCHANGE:
            if railnumber == 9:
                railnumber = 1
            else:
                railnumber += 1
                
            railtick = 0 # reset the clock on moving rails
            
            for rail in rails:
                rail['image'] = pygame.image.load(RAILIMAGES % railnumber)

        # Delete obstacles off the screen
        i = 0
        for obst in obstaclesOnField:
            if obst['y'] > WINHEIGHT:
                obstaclesOnField.pop(i)
                numObstaclesOnField -= 1
            i += 1
                
        # Generate new obstacle
        if numObstaclesOnField < MAX_OBST_ON_FIELD:
            randobstgen = random.randint(MIN_OBST_GEN_TIME, MAX_OBST_GEN_TIME)
            if randobstgen == obstgentick:
                newobstacleobj = Obstacles[random.randint(1, numObstacles)]
                newobstacle = createNewObstacle(newobstacleobj['type'],
                                                newobstacleobj['image'])
                obstaclesOnField.append(newobstacle)
                numObstaclesOnField += 1
                obstgentick = 1

        # Move obstacle on field
        if obstacletick == OBSTACLECHANGE:
            for obstacle in obstaclesOnField:
                obstacle['y'] += 1
                obstacle['rect'] = pygame.Rect( (obstacle['x'],
                                                 obstacle['y'],
                                                 obstacle['width'],
                                                 obstacle['height']) )
            obstacletick = 0 # reset the clock on moving obstacles
            

        ##### EVENT HANDLING LOOP #####
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            # determine direction pressed by user
            elif event.type == KEYDOWN:
                if event.key in (K_LEFT, K_a):
                    if player['x'] != LEFT_RAIL + RAILWIDTH:
                        moveLeft = True
                        moveRight = False
                    else:
                        moveLeft = False
                        moveRight = False
                elif event.key in (K_RIGHT, K_d):
                    if player['x'] != RIGHT_RAIL + RAILWIDTH:
                        moveLeft = False
                        moveRight = True
                    else:
                        moveLeft = False
                        moveRight = False
                # Catch invalid keypress'
                elif event.key in (K_UP, K_w, K_DOWN, K_s):
                    moveLeft = False
                    moveRight = False

                # move player one rail over in direction of keypress
                if moveLeft:
                    player['x'] -= RAIL
                if moveRight:
                    player['x'] += RAIL            
                    
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        # Update clocks used by game
        if obstgentick == FPS:
            obstgentick = 1
        else:
            obstgentick += 1
        railtick += 1
        obstacletick += 1
            
def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
