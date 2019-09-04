Making 2 Players
----------------

This game would be a lot more fun if it were multiplayer right? Let's make it work. First we will have to DEFINE a second Player, then Draw it, and finally be able to move it.

Defining Player 2
-----------------

In our main loop just under where we define player1, we must define player2 as so:

player2 = makeShip('images/ShipRight.png',display_width * .9, display_height * .7)


Drawing Player 2
----------------

To draw player 2, we will implement the following code just under the drawShip(player1) function in our main Loop:

drawShip(player2)

Since we already wrote the code to draw player1, we can simply use the same code to draw player2.

Moving Player 2
---------------

To allow player 2 to move like player 1, we will again follow the same routine. We want Player 2 to be able to use the Arrow keys to move around. In our main loop just under where it says ## Player 2 implement this:

if event.key == pygame.K_LEFT:
    # if the Left arrow key was pressed
    player2.mDX = -3
if event.key == pygame.K_RIGHT:
    # if the Right arrow key was pressed
    player2.mDX = 3
if event.key == pygame.K_UP:
    # if the Up arrow key was pressed
    player2.mDY = -3
if event.key == pygame.K_DOWN:
    # if the Down arrow key was pressed
    player2.mDY = 3

And just under the "if event.type == pygame.KEYUP:" code line, implement:

if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    player2.mDX = 0
if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
 	player2.mDY = 0

This will change our Ships position based on which keys player 2 uses.
Next, call this function just under the drawShip(player2) function in our main loop:

moveShip(player2)

This will simply draw all of these changed to the display