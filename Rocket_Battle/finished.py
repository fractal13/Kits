import pygame
from myLibrary import *
import time

## this will tell pygame to start
pygame.init()

## decide how big the window size will be
display_width = 800
display_height = 600
## this will keep track of time throughout the game
clock = pygame.time.Clock()

## this will make the screen display, you can also give your program a name
programName = "Your programs name here"
gameDisplay = start_display(display_width, display_height, programName)

InvaderList = []
BulletList = []

## this block of code defines our ship
class Ship:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height):
        self.mX = x_position 						# this sets where our x position will be
        self.mY = y_position 						# this sets where our y position will be
        self.mDX = delta_x							# this tells us how fast our ship moves
        self.mDY = delta_y							
        self.mWidth = width 						# this sets our ships width
        self.mHeight = height 						# this sets our ships height
        self.mImage = pygame.image.load('GC.jpg') 	# this tells us which picture to use for our ship

class Invader:
    def __init__(self, x_pos, y_pos, width, height):
        self.mX = x_pos
        self.mY = y_pos
        self.mWidth = width 
        self.mHeight = height 
        self.mSpeed = 1
        self.mImage = pygame.image.load('bronze.png')

class Bullet:
    def __init__(self, x_pos, y_pos, width, height, bulletSpeed):
        self.mX = x_pos - 25 /2
        self.mY = y_pos - 25
        self.mWidth = width 
        self.mHeight = height
        self.mSpeed = bulletSpeed
        self.mImage = pygame.image.load('d3.png')

def make_invaders():
  if len(InvaderList) == 0:
      placeY = 5
      for i in range(3):
          for j in range(10):
              invader = Invader(5 + j * (65 + 10), placeY, 65, 65)
              InvaderList.append(invader)
          placeY += 65 + 10

def makeShip():
	x_position = display_width * 0.45
	y_position = display_height * 0.85
	delta_x = 0
	delta_y = 0
	width = 100
	height = 88
	ship = Ship(x_position, y_position, delta_x, delta_y, width, height)
	return ship

def drawShip(ship):
	draw_image(gameDisplay, ship.mX, ship.mY, ship.mImage)

def moveShip(ship):
	ship.mX += ship.mDX
	ship.mY += ship.mDY
	if ship.mX < 0:
		ship.mX = 0
	if ship.mX + ship.mWidth > display_width:
		ship.mX = display_width - ship.mWidth
	if ship.mY + ship.mHeight > display_height:
		ship.mY = display_height - ship.mHeight

def draw_bullets():
    for bullet in BulletList:
        bullet.mY += bullet.mSpeed
        draw_image(gameDisplay, bullet.mX, bullet.mY, bullet.mImage)

def draw_invaders():
  for invader in InvaderList:
      invader.mX += invader.mSpeed
      if invader.mX < 0:
          for invader in InvaderList:
              invader.mSpeed = 1
              invader.mY += 1
      if invader.mX > display_width - 65:
          for invader in InvaderList:
              invader.mSpeed = -1
              invader.mY += 1
      draw_image(gameDisplay, invader.mX, invader.mY, invader.mImage)

def draw_bullets():
    for bullet in BulletList:
        bullet.mY += bullet.mSpeed
        draw_image(gameDisplay, bullet.mX, bullet.mY, bullet.mImage)

def check_remove_bullets():
	for bullet in BulletList:
		if bullet.mY < 0 - 25:
			BulletList.remove(bullet)

def check_bullet_collisions():
    for bullet in BulletList:
        for invader in InvaderList:
            if collide_rect(invader, bullet):
                BulletList.remove(bullet)
                InvaderList.remove(invader)

def check_invader_collision(ship):
	for invader in InvaderList:
		if collide_rect(invader, ship):
			return True
	return False


## this block is what calls the rest of our code 
def main_loop():
    gameOver = False 

    ship = makeShip() 			#this will make our ship
    ## this while loop will repeat over and over until the game ends
    while not gameOver:
    	## this for loop keeps track of all the keys that you push in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT: ## this would be the X button in the top right corner
                pygame.quit()
                quit()
            ## this if statement will keep track of all keys pressed DOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT:
                	# if the Left arrow key was pressed
                	ship.mDX = -3
                if event.key == pygame.K_RIGHT:
                	# if the Right arrow key was pressed
                	ship.mDX = 3
                if event.key == pygame.K_UP:
                	# if the Up arrow key was pressed
                	ship.mDY = -3
                if event.key == pygame.K_DOWN:
                	# if the Down arrow key was pressed
                	ship.mDY = 3
                if event.key == pygame.K_SPACE:
                	# if the Space key was pressed
                	print("space key pressed")
                	bullet = Bullet(ship.mX + ship.mWidth/2, ship.mY, 25, 25, -8)
                	BulletList.append(bullet)
                if event.key == pygame.K_r:
                	# if the R key was pressed
                	print("restart key pressed")
            ## this if statement will keep track of all keys RELEASED
            if event.type == pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 	ship.mDX = 0
                 if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 	ship.mDY = 0

        moveShip(ship)
        gameDisplay.fill(black) 									## set the background to be black (other colors available in myLibrary.py)
        drawShip(ship)										 		## this will draw our ship
        draw_invaders()
        draw_bullets()
        check_remove_bullets()
        check_bullet_collisions()
        if check_invader_collision(ship):
        	display_message(gameDisplay, "You Lose", 100)
        	time.sleep(2)
        	gameOver = True

        if len(InvaderList) == 0:
        	pygame.display.update()
        	display_message(gameDisplay, "You Win", 100)
        	time.sleep(2)
        	gameOver = True

        # this will refresh the screen and make updates
        pygame.display.update()
        clock.tick(60)
    while gameOver == True:
    	for event in pygame.event.get():
            if event.type == pygame.QUIT: ## this would be the X button in the top right corner
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                	for i in range(5):
                		for invader in InvaderList:
                			InvaderList.remove(invader)
                		for bullet in BulletList:
                			BulletList.remove(bullet)
                	make_invaders()
                	main_loop()

    	gameDisplay.fill(black)
    	display_message(gameDisplay, "Press R to play again", 50)
    	pygame.display.update()
    	clock.tick(60)
    

make_invaders()
main_loop()