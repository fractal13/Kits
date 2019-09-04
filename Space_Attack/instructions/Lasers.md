Lasers
------

It just wouldn't be a space ship without lasers that the ship could shoot, right? Let's implement this. 

Like before we will need to Define, Make, Draw, and Move our lasers.

Defining Lasers
---------------

Let's use this Laser class to be our lasers. Implement this just below our Asteroid class: 

class Laser:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height, image, damage):
        self.mX = x_position                        # this sets where our x position will be
        self.mY = y_position                        # this sets where our y position will be
        self.mDX = delta_x                          # this tells us how fast our laser moves
        self.mDY = delta_y                          
        self.mWidth = width                         # this sets our ships width
        self.mHeight = height                       # this sets our ships height
        self.mImage = pygame.image.load(image)  # this tells us which picture to use for our laser
        self.mDamage = damage



Making Lasers
-------------

Now that we know what a Laser is, we need to make one each time a user presses their trigger key.  We must do this for player1 and player2.  
Before me make the lasers, we must make a place to hold all of their data, so a the top of the file, just under the asteroid list, write:

player1Lasers = []
player2Lasers = []

Next we must make a function that will actually make the lasers, such as:

def makePlayer1Laser(player1):
    if len(player1Lasers) < 5:
        laser = Laser(player1.mX + player1.mWidth, player1.mY + player1.mHeight / 2, 5, 0, 50, 16, 'images/Laser1.png', 1)
        player1Lasers.append(laser)

and for player2:

def makePlayer2Laser(player2):
    if len(player2Lasers) < 5:
        laser = Laser(player2.mX - 50, player2.mY + player2.mHeight / 2, -5, 0, 50, 16, 'images/Laser2.png', 1)
        player2Lasers.append(laser)

So in our main loop, just under where it says "## Player1", add this code:

if event.key == pygame.K_SPACE:
    # if the Space key was pressed
    makePlayer1Laser(player1)


And just under where is says "## Player 2", add this:

if event.key == pygame.K_RETURN:
    # if the Space key was pressed
    makePlayer2Laser(player2)


Now we have made it so that when player 1 presses the SPACE key, it will make a laser and when player 2 presses the ENTER key, it will also make a laser.

Drawing Lasers
--------------

Third, we must Draw the lasers to the display. We must again make a function for player1 and player2.

For player1: 

def drawPlayer1Lasers():
    for laser in player1Lasers:
        draw_object(gameDisplay, laser)

And for player2:

def drawPlayer2Lasers():
    for laser in player2Lasers:
        draw_object(gameDisplay, laser)


To call these functions, write these two lines just under our moveShip() functions in our main loop:

drawPlayer1Lasers()
drawPlayer2Lasers()


Moving Lasers
-------------

Last but not least, we need to move our lasers. Let's write our move laser functions, once again, for player1:

def movePlayer1Lasers():
    for laser in player1Lasers:
        laser.mX += laser.mDX
        if out_of_bounds(laser):
            player1Lasers.remove(laser)

And for player2:

def movePlayer2Lasers():
    for laser in player2Lasers:
        laser.mX += laser.mDX
        if out_of_bounds(laser):
            player2Lasers.remove(laser)


There you have it. Lasers that you can fire.