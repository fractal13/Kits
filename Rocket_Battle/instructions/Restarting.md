Restarting
----------

Some users want to play again without having to re-open the program.
This a good idea.

Just after the "while not gameOver:" indentation insert another while loop for "while gameOver:"

Like this:

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


This loop will wait for the user to exit the program or press R to start again