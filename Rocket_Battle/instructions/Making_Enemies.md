Making Enemies
--------------

Space Invaders wouldn't be much of a game without any invaders.
We will need to define WHAT an invader is, and WHERE it should be on the screen
and also how it will MOVE.

Defining An Invader
-------------------

To define what an Invader is, we will need a couple of things. 
Here's a list of things we need:
  - x_position
  - y_position
  - width
  - height
  - speed
  - image

To implement this, copy and paste this code right underneath the Ship class

    class Invader:
      def __init__(self, x_pos, y_pos, width, height):
          self.mX = x_pos
          self.mY = y_pos
          self.mWidth = width 
          self.mHeight = height 
          self.mSpeed = 1
          self.mImage = pygame.image.load('images/bronze.png')



Drawing An Invader
------------------

Now that we know WHAT an Invader is, we need to tell our program to MAKE and DRAW them.

Before we make a bunch of Invaders, we need a place for them to go.
Go ahead a make a list for our Invaders to be kept.
At the top of start.py just above the Ship class paste this:

    InvaderList = []


To make the Invaders copy and paste thie code right underneath the Invader class

    def make_invaders():
      if len(InvaderList) == 0:
          placeY = 5
          for i in range(3):
              for j in range(10):
                  invader = Invader(5 + j * (65 + 10), placeY, 65, 65)
                  InvaderList.append(invader)
              placeY += 65 + 10

Call this code by calling it at the end on the second to last line (right above mainLoop())

    make_invaders()

Now that we have MADE the Invaders and put them into our list, we can now DRAW them to the screen

Go ahead and make a function called draw_invaders() by pasting this code right 
under make_invaders function: 

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

Now call this code in the mainLoop right under drawShip(ship);

    draw_invaders()

