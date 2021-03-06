import pygame, sys, os, background


#Initiats the game and sprites
pygame.init()
playerPNG = pygame.image.load("Player.png")
playerPNG = pygame.transform.scale(playerPNG, (200,200))
trash = pygame.image.load("trash.png")
trash = pygame.transform.scale(trash, (400,400))
#Centres the screen
os.environ["SDL_VIDEO_CENTERED"] = "1"
#Assigns the window parameters
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 900

#Creates interface for the screen
backgroundTitle = background.Background("TitleBack.jpg", (0,0),WINDOW_WIDTH, WINDOW_HEIGHT)
pygame.font.init()
myfont = pygame.font.SysFont("Courier New", 50)
gameOverText = myfont.render("Game Over " +" " +"Git Gud", False, (255,255,255))
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)
pygame.mixer.music.load("gameoverbad.mp3")
pygame.mixer.music.play()
#Loops The game over screen

while True:
    #Outputs the screen overlay
    screen.fill([0,0,0])
    screen.blit(backgroundTitle.image, backgroundTitle.rect)
    screen.blit(playerPNG, (500,300))
    screen.blit(trash, (400, 400))
    screen.blit(gameOverText, (200,200))
    
    for event in pygame.event.get():
        #Exits the program
        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)

    pygame.display.update()
