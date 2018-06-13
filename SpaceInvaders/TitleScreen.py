import pygame, sys, os, background, threading

def outputDirect():
    ''' Outputs the click space start line '''
    screen.blit(directions, (300,200))

def loop_play():
    is_playing = True
    start = True
    pygame.mixer.music.load("PaydayMusic.mp3")
    while is_playing:
        pygame.mixer.music.play()
        pygame.time.wait(194800)
        
def press_button_play():
    global is_playing
    global my_thread

    if not is_playing:
        is_playing = True
        my_thread = threading.Thread(target=loop_play)
        my_thread.start()

pygame.init()
pygame.mixer.init()
is_playing = False


window_width = 1280
window_height = 720

backgroundTitle = background.Background("TitleBack.jpg", (0,0),window_width, window_height)
baddieImage = pygame.image.load("Enemy2.png")
baddieImage = pygame.transform.scale(baddieImage, (300,300))
baddieImagechange = pygame.image.load("Enemy2change.png")
baddieImagechange = pygame.transform.scale(baddieImagechange, (300,300))

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.font.init()
myfont = pygame.font.SysFont("Courier New", 50)

background = background.Background("simpleback.jpeg", (0,0),window_width, window_height)

level = 3
score = 250
lives = 5

livesTitle = myfont.render("Lives", False, (255,255,255))
livesPrint = myfont.render(str(lives), False, (255,255,255))

scoreTitle = myfont.render("Score", False, (255,255,255))
scorePrint = myfont.render(str(score), False, (255,255,255))

levelTitle = myfont.render("Level", False, (255,255,255))
levelPrint = myfont.render(str(level), False, (255,255,255))
title = myfont.render("SPACE INVADERS", False, (255,255,255))
directions = myfont.render("<Press Space to Start>", False,(255,255,255))

directOn = True
screen = pygame.display.set_mode((window_width, window_height))
titleOn = True
while titleOn == True:
    if is_playing == False:
        press_button_play()
    screen.fill([0,0,0])
    screen.blit(backgroundTitle.image, backgroundTitle.rect)
    if directOn == True:
        outputDirect()
        screen.blit(baddieImage, (200,300))
        directOn = False
    elif directOn == False:
        screen.blit(baddieImagechange, (200,300))
        directOn = True
    screen.blit(title, (830, 460))
    pygame.time.wait(500)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space")
                titleOn = False
                break
        elif event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)

    pygame.display.update()

while True: # main game loopdirection = ''
    screen.fill([255,255,255])
    screen.blit(background.image, background.rect)
    screen.blit(scoreTitle,(0,0))
    screen.blit(scorePrint, (10,50))
    screen.blit(livesTitle, (0, 900))
    screen.blit(livesPrint, (175, 900))
    screen.blit(levelTitle, (window_width-200, 0))
    screen.blit(levelPrint, (window_width-150, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()
            os._exit(1)
    pygame.display.update() 

