Asteroids
---------

Now that both players can move around and we have a lot of stars twinkling, let's add some Asteroids that the player will need to dodge.  Like before, we will need to Define, Make, Draw and Move our asteroids.  

Defining Asteroids
------------------

Let's use this Asteroids class to be our asteroids and place it just under our Ship class:

class Asteroid:
    def __init__(self, x_position, y_position, delta_x, delta_y, width, height, image):
        self.mX = x_position                        # this sets where our x position will be
        self.mY = y_position                        # this sets where our y position will be
        self.mDX = delta_x                          # this tells us how fast our asteroid moves
        self.mDY = delta_y                          
        self.mWidth = width                         # this sets our ships width
        self.mHeight = height                       # this sets our ships height
        self.mImage = pygame.image.load(image)  # this tells us which picture to use for our asteroid

Making Asteroids
----------------

Now that we have defined our asteroids, we can make as many as we like.  First we need to make a place to hold their data, so at the top of our file just under our gameDisplay, make a list for our asteroids:

asteroidList = []

Next let's implement our makeAsteroids function just below our asteroid class and choose to only have 15 asteroids in total and add them to our asteroid list:

def makeAsteroids(num):
    for i in range(num):
        asteroid = Asteroid(random.randint(0, display_width), random.randint(-900, -60), random.uniform(-1,1), 3, 60, 60, 'Asteroid.png')
        asteroidList.append(asteroid)

Now we just need to call this function, so in our main Loop just under where we define player2, write:

makeAsteroids(15)


Drawing and Moving Asteroids
----------------------------

Now to the third step: Drawing and Moving.  Since asteroids cannot be controlled by a user, we can draw and move our asteroids in one single step.  Let's write this function just below our makeAsteroids() function:

def draw_move_Asteroids():
    for asteroid in asteroidList:
        draw_object(gameDisplay, asteroid)
        asteroid.mX += asteroid.mDX
        asteroid.mY += asteroid.mDY
        if asteroid.mY > display_height:
            asteroid.mX = random.randint(0, display_width)
            asteroid.mY = random.randint(-900, -60)
            asteroid.mDX = random.uniform(-1,1)

And finally, let's call this function in our main loop just under where we call drawStars().

draw_move_Asteroids()

There you have it, Asteroids falling through space. 