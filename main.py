"""
Nicholas Nicolaev
December 8, 2020
Avoiding Game
"""

# - - - - - - - - - - - - Imports - - - - - - - - - - - -
import pygame             # Allows access to turtle library
pygame.init()             # Pygame initiation
import random             # Allows access to random numbers module

wn = pygame.display.set_mode((400,600))                                   # Sets up window screen
pygame.display.set_caption("Simple Avoiding Game (Nicholas Nicolaev)")    # Sets python window name
bg = pygame.image.load("Sprites/Background.gif")                          # Imports background picture
char = pygame.image.load("Sprites/SpaceShip1(Sprite).png")                # Main character sprite
Fireball = pygame.image.load("Sprites/Fireball.png")                      # Fireball sprite for enemies

# - - - - - - - - - - - - Main Variables - - - - - - - - - - - -
listLife = []          # Declares empty list to store life points
listEnemies = []       # Declares empty list to store enemies
delay = 0              # Declares delay time for enemy spawn
global score           # Declares score as a global variable
score = 0              # Sets game score to 0
level = 1              # Sets starting level to 1
highscore = 0          # Sets highscore to 0
run = True             # Variable for main loop
# - - - - - - - - - - - - Functions - - - - - - - - - - - -
# Class containing info on main player
class player:           # Declares class to store player info
    def __init__(self,x,y,width,height,speed):      # Main attributes of player class
        self.x = x              # X coordinate
        self.y = y              # Y coordinate
        self.width = width      # Width
        self.height = height    # Height
        self.speed = speed      # Velocity
        self.hitboxBody = (self.x+12, self.y, 20, 40)   # Sets values for rectangular hit box around main body of spaceship
        self.hitboxWings = (self.x, self.y+20,45,15)    # Sets values for rectangular hit box around wings of spaceship

    # Method used to draw hitboxes around spaceship (ignore)
    def draw(self, wn):     # Declares draw method that draws hit box for debugging purposes
        #pygame.draw.rect(wn, (255,0,0), self.hitboxBody,2)
        #pygame.draw.rect(wn, (255, 0, 0), self.hitboxWings, 2)
        self.hitboxBody = (self.x + 12, self.y, 20, 40)
        self.hitboxWings = (self.x, self.y + 20, 45, 15)

# Class containing info on life points
class life:         # Declares class to store life point info
    def __init__(self,x,y):     # Main attributes of lifepoint class
        self.x = x              # X coordinate
        self.y = y              # Y coordinate

    # Method to display life point visuals
    def draw(self,wn):          # Declares method to display life points on main screen
        pygame.draw.circle(wn, (255,0,0), (self.x, self.y), 10)     # Draws a circle representing a life point

# Class containing info about enemy
class enemy:               # Declaration of enemy to story object info
    def __init__(self,x,y,width,height,speed):      # Main attributes of enemy
        self.x = x              # X coordinate
        self.y = y              # Y coordinate
        self.width = width      # Width
        self.height = height    # Height
        self.speed = speed      # Velocity
        self.hitbox = (self.x+5, self.y+10, 15, 40) # Rectangular hit box around enemy object

    # Method that draws a fireball as a representation of the enemy object
    def draw(self, wn):     # Method declaration
        wn.blit(Fireball, (self.x, self.y))            # Draws fireball
        #pygame.draw.rect(wn, (255, 0, 0), self.hitbox, 2)  # Used for debugging
        self.hitbox = (self.x+5, self.y+10, 15, 40)    # Sets hit box around enemy location

# Function used to update program window
def redrawGameWindow():             # Declares redrawGameWindow() function
    wn.blit(bg, (0,0))              # Draws background first
    scoretext = font.render("Score: " + str(score), 1, (0, 0, 0))   # Draws score
    wn.blit(scoretext, (20, 5))     # Sets location of score
    highscoretext = font.render("Highscore: " + str(highscore), 1, (0, 0, 0))   # Draws highscore
    wn.blit(highscoretext, (20, 22)) # Sets location of highscore
    leveltext = font.render("Level: " + str(level), 1, (0, 0, 0))   # Draws level
    wn.blit(leveltext, (20, 39))     # Sets location of level
    wn.blit(char, (nick.x,nick.y))   # Draws main character sprite over instance of player
    nick.draw(wn)                    # Used to draw hit box for debugging (ignore)

    # Draws current amount of life points
    for hp in listLife:    # Increments hp for representation of index of listLife
        hp.draw(wn)        # Draws all indexes in listLife (max 3 - min 0)

    # Draws enemies
    for comet in listEnemies:   # Increments comet for representation of index of listEnemies
        comet.draw(wn)          # Draws all indexes within listEnemies (w/ updated hit boxes and location)

    # Checks if player lost game
    if listLife == []:              # Checks if list containing life points is empty
        for comet in listEnemies:   # Increments comet to check all indexes within listEnemies
            listEnemies.pop(listEnemies.index(comet))   # Removes all enemies on field
        replaytext = font.render("Press space bar to play again! Or \"q\" to quit.", 1, (0, 0, 0))  # Displays game over message
        wn.blit(replaytext, (10, 300))  # Places text in middle of screen

    pygame.display.update()     # Updates window
# - - - - - - - - - - - - Main Program - - - - - - - - - - - -
# Game prep
font = pygame.font.SysFont('TimesNewRoman', 20)     # Assigns values to font variable
nick = player(187,560,25,25,2)                      # Declares instance of main player
for i in range(3):                                  # Loops 3 times to add 3 lives
    listLife.append(life(300 + (i * 35), 20))       # Adds life

# Main loop containing game logic
while run:                      # Main loop
    pygame.time.delay(10)       # Sets frame-rate accordingly

    # Adds spawn delay based on level (higher level = less delay = more enemies)
    delay += 1                  # Increments delay each refresh
    if level == 1:              # Checks level
        delayTimer = 100        # Updates delay timer
    elif level == 2:            # Checks level
        delayTimer = 60         # Updates timer
    else:                       # Checks level
        delayTimer = 25         # Updates timer to hardest setting

    # Spawns enemies
    if delay == delayTimer:                     # Checks delay
        x = random.randint(0,400)               # Sets random spawn point
        listEnemies.append(enemy(x,0,10,10,1))  # Summons enemy fireball
        delay = 0                               # Sets delay back to 0

    # Class to update location of fireballs
    for comet in listEnemies:               # Checks through all indexes of listEnemies
        if comet.y >= 0 and comet.y < 600:  # Checks if fireball is on screen
            comet.y += comet.speed          # Moves fireball forward at set speed
        else:                               # Checks if fireball is off screen
            listEnemies.pop(listEnemies.index(comet))   # Removes that fireball from list
            score += 1                      # Increments score of player

    # Checks collision
    # Checks main body of player (excluding wings that protrude)
    for comet in listEnemies:    # For loop to check for all enemies on field
        if comet.hitbox[1] - comet.hitbox[3] < nick.hitboxBody[1] + nick.hitboxBody[3] and comet.hitbox[1] + comet.hitbox[3] > nick.hitboxBody[1]:  # Checks if fireball hits y coordinate of player
            if comet.hitbox[0] + comet.hitbox[2] > nick.hitboxBody[0] and comet.hitbox[0] - comet.hitbox[2] < nick.hitboxBody[0] + 5:               # Checks if fireball hits x coordinate of player
                listEnemies.pop(listEnemies.index(comet))   # Removes enemy that touched player from list
                for hp in listLife:                         # Checks first index of listLife
                    listLife.pop(listLife.index(hp))        # Removes first index of listLife
                    break                                   # Breaks loop to only remove one life
    # Checks wings of player (spaceship wings)
    for comet in listEnemies:     # For loop to check for all enemies on field
        if comet.hitbox[1] - comet.hitbox[3] < nick.hitboxWings[1] + nick.hitboxWings[3] and comet.hitbox[1] + comet.hitbox[3] > nick.hitboxWings[1]:   # Checks if fireball hits y coordinate of player
            if comet.hitbox[0] + comet.hitbox[2] > nick.hitboxWings[0]and comet.hitbox[0] - comet.hitbox[2] < nick.hitboxWings[0] + 32:                 # Checks if fireball hits x coordinate of player
                listEnemies.pop(listEnemies.index(comet))   # Removes enemy that touches player from list
                for hp in listLife:                         # Checks first index of listLife
                    listLife.pop(listLife.index(hp))        # Removes first index or listLife
                    break                                   # Breaks loop to only remove on life

    # Checks if user clicks exit
    for event in pygame.event.get():    # Checking events
        if event.type == pygame.QUIT:   # Checks if user quits
            run = False                 # Sets main loop to false

    # Updates and stores highscore
    if score > highscore:      # Checks if current score has beaten old highscore
        highscore = score      # Updates highscore value

    # Updates level based on score
    if score >= 0 and score <= 20:    # Checks if score is between 0 and 20
        level = 1                     # Sets level to 1
    elif score > 20 and score <= 50:  # Checks if score is betweem 21 and 50
        level = 2                     # Sets level to 2
    elif score > 50:                  # Checks if score is above 50
        level = 3                     # Sets to maximum level (3)

    # Listening for key events
    keys = pygame.key.get_pressed()         # Checking for key events
    if keys[pygame.K_LEFT] and nick.x > 0:  # Checks if user pressed left arrow key & sets boundary
        nick.x -= nick.speed                # Moves instance of main player left
    if keys[pygame.K_RIGHT] and nick.x < 382 - nick.width - nick.speed:     # Checks if user pressed right arrow key & sets boundary
        nick.x += nick.speed                # Moves instance of main player right
    if keys[pygame.K_q]:                    # Checks if user pressed q
        exit()                              # Ends program
    if keys[pygame.K_SPACE] and listLife == []: # Checks if user pressed space bar
        score = 0                           # Resets score
        for i in range(3):                             # For loop to reset life points
            listLife.append(life(300 + (i * 35), 20))  # Adds life point

    redrawGameWindow()      # Updates main program window
pygame.quit()               # Ends program


