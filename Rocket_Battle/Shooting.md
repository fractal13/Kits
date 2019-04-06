Shooting
--------

This is a lot like makeing enemies. 
We need to define WHAT is being shot, and where it will be drawn on the screen.

Defining A Bullet
-----------------

To define what a Bullet is, we will need a couple of things. 
Here's a list of things we need:
  - x_position
  - y_position
  - width
  - height
  - speed
  - image

To implement this, copy and paste this code right underneath the Ship class.

class Bullet:
    def __init__(self, x_pos, y_pos, width, height, bulletSpeed):
        self.mX = x_pos - 25 /2
        self.mY = y_pos - 25
        self.mWidth = width 
        self.mHeight = height
        self.mSpeed = bulletSpeed
        self.mImage = pygame.image.load('d3.png')


Drawing An Invader
------------------

Now that we know WHAT an Invader is, we need to tell our program to MAKE and DRAW them

Before we make a bunch of Bullets, we need a place for them to go.
Go ahead a make a list for our Bullets to be kept.
At the top of start.py just above the Ship class paste this:

BulletList = []

We are going to decide that we only want to shoot a Bullet when the SPACE button is pressed.
In our mainLoop() find where it says "if event.key == pygame.K_SPACE:".
Right under there, paste this: 

bullet = Bullet(ship.mX + ship.mWidth/2, ship.mY, 25, 25, -8)
BulletList.append(bullet)

Now that we have made a bullet every time we press the SPACE button, we just need to draw them.
Make a function called draw_bullets() right under our moveShip() function.

def draw_bullets():
    for bullet in BulletList:
        bullet.mY += bullet.mSpeed
        draw_image(gameDisplay, bullet.mX, bullet.mY, bullet.mImage)

Now paste this code right under drawShip(ship) in our main loop to call it.

draw_bullets()

Before we are finished, we need to remove the bullets from our list as they move off of the screen.

Make a function below draw_bullets called checK_remove_bullets.

def check_remove_bullets():
	for bullet in BulletList:
		if bullet.mY < 0 - 25:
			BulletList.remove(bullet)

This code will check and see if any of the bullets in our list are out of bounds.  If they are, 
they will be removed from our list.

All that is left is to call this code in our main loop right below drawShip.

check_remove_bullets()