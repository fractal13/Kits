Background Stars
----------------

A filled-black screen doesn't much seem like a space battle, so lets add a few stars to brighten up the scenery a little. Implement a drawStars() function just under the Ship class:

def drawStars():
 	for i in range(25):
 		x = random.randint(0, display_width)
 		y = random.randint(0, display_height)
 		color = white 
 		drawCircle(gameDisplay, x, y, color)

And to call this code, write this line just under the line that says "gameDisplay.fill(black)" in our main loop.

drawStars()

This will randomly draw very tiny circles that look like stars all over our display.