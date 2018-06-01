
import pygame, os,random, PlayerObject, EnemyObject, ItemObject

os.environ['SDL_VIDEO_CENTERED'] = '1'#centres the window
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0,32)
pygame.display.set_caption("1st Game")
enemies = []
items = []
startItems = []

#makes player
player = PlayerObject.Player()
player.rect.left = 450
player.rect.top = 0

#makes enemies
tempEnemy = EnemyObject.Enemy(5,0, 150, 200)#creates the enemy with an x Move amount of 5
tempEnemy.rect.left = tempEnemy.startLeft
tempEnemy.rect.top = tempEnemy.startTop
enemies.append(tempEnemy)

tempEnemy = EnemyObject.Enemy(5,0, 800, 600)
tempEnemy.rect.left = tempEnemy.startLeft
tempEnemy.rect.top = tempEnemy.startTop
enemies.append(tempEnemy)

tempEnemy = EnemyObject.Enemy(0,-5, 835, 50)
tempEnemy.rect.left = tempEnemy.startLeft
tempEnemy.rect.top = tempEnemy.startTop
enemies.append(tempEnemy)

tempEnemy = EnemyObject.Enemy(0,4, 55, 300)
tempEnemy.rect.left = tempEnemy.startLeft
tempEnemy.rect.top = tempEnemy.startTop
enemies.append(tempEnemy)

tempEnemy = EnemyObject.Enemy(2,2, 1, 1)
tempEnemy.rect.left = tempEnemy.startLeft
tempEnemy.rect.top = tempEnemy.startTop
enemies.append(tempEnemy)

tempEnemy = EnemyObject.Enemy(2,1, 1100, 100)
tempEnemy.rect.left = tempEnemy.startLeft
tempEnemy.rect.top = tempEnemy.startTop
enemies.append(tempEnemy)

tempEnemy = EnemyObject.Enemy(1,4, 1, 1)
tempEnemy.rect.left = tempEnemy.startLeft
tempEnemy.rect.top = tempEnemy.startTop
enemies.append(tempEnemy)

#makes items
tempItem = ItemObject.Item(1200, 650)#bottom right
tempItem.rect.left = tempItem.left
tempItem.rect.top = tempItem.top
items.append(tempItem)

tempItem = ItemObject.Item(100, 300)#far left
tempItem.rect.left = tempItem.left
tempItem.rect.top = tempItem.top
items.append(tempItem)

tempItem = ItemObject.Item(640, 450)#middle bottom
tempItem.rect.left = tempItem.left
tempItem.rect.top = tempItem.top
items.append(tempItem)

tempItem = ItemObject.Item(300, 580)#bottom left ish
tempItem.rect.left = tempItem.left
tempItem.rect.top = tempItem.top
items.append(tempItem)

tempItem = ItemObject.Item(1000, 100)#middle top right ish
tempItem.rect.left = tempItem.left
tempItem.rect.top = tempItem.top
items.append(tempItem)

while True:
    
    surface.fill((0,0,0))#makes the screen black

    #player movement
    player.movement(WINDOW_WIDTH, WINDOW_HEIGHT)#checks if player can move

    #enemy movement
    for i in range (len(enemies)):
        enemies[i].movement(WINDOW_WIDTH, WINDOW_HEIGHT)


    '''
    #collision and enemy death
        for i in range (len(enemies)):
            collision = player.collisionCheck(enemies[i])
            
            if player.collisionCheck(enemies[i]) == True:
                enemies[i].die()
    '''
    #collisions and player death
    for i in range(len(enemies)):
        if player.collisionCheck(enemies[i]) == True:
            pygame.time.wait(100)
            for i in range(len(enemies)):#resets location of all enemies
                enemies[i].restart()
            
            for i in range(len(items)):#resets all items
                items[i].restart()
                

            #resets player location
            player.rect.left = 450
            player.rect.top = 0
            break
            
            

    #Checks if player collects items
    for i in range (len(items)):
        collisionStatus = items[i].collectCheck(player)#checks if the item is being touched by the player
        '''if collisionStatus == True:#prevents error where item would be popped in the middle of the for loop and i would be higher than the length of the list for that loop
            break'''
            
        

    
    #makes objects appear
    surface.blit(player.image, player.rect)

    for i in range (len(enemies)):
        enemies[i].appear(surface)#blits the enemy only if alive

    for i in range (len(items)):
        items[i].appear(surface)#blits the item only if it has not been touched\


    #checks if the first screen is done
    for i in range(len(items)):#ends screen if all items are collected
        allCollected = True#stays true if all items are uncollected
        if items[i].status == "uncollected":
            allCollected = False
            break

    if allCollected == True:#ends game if all items are collected
        break

    pygame.display.update()
    pygame.time.wait(10)#10 millisecond pause


    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:#hit the x and ends game
            pygame.quit()
            os._exit(1)








letterH = pygame.image.load("LetterH.png")
letterH = pygame.transform.scale(letterH, (100,100))
letterHRect = letterH.get_rect()

letterE = pygame.image.load("LetterE.png")
letterE = pygame.transform.scale(letterE, (100,100))
letterERect = letterE.get_rect()

letterL = pygame.image.load("LetterL.png")
letterL = pygame.transform.scale(letterL, (100,100))
letterLRect = letterL.get_rect()

letterO = pygame.image.load("LetterO.png")
letterO = pygame.transform.scale(letterO, (100,100))
letterORect = letterO.get_rect()

qMark = pygame.image.load("QMark.jpg")
qMark = pygame.transform.scale(qMark, (100,100))
qMarkRect = qMark.get_rect()

surface.fill((0,0,0))
pygame.display.update()

for i in range(len(items)):
    items[i].image = pygame.transform.scale(items[i].image, (100,100))

left = 200
top = 360

items[0].rect.left = left
items[0].rect.top = top

surface.blit(items[0].image, items[0].rect)
pygame.display.update()

for i in range(1,5):
    left += 200

    items[i].rect.left = left
    items[i].rect.top = top

    surface.blit(items[i].image, items[i].rect)
    pygame.display.update()

currChar = 0


'''
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint (0,255)
'''

myfont = pygame.font.SysFont('Franklin Gothic Medium', 50)
textsurface = myfont.render('Decode The Message', False, (100, 0, 255))
surface.blit(textsurface, (430,50))
pygame.display.update()
while True:
    pygame.draw.rect(surface, (100,0,255), pygame.Rect(150,320, 1000, 200), 20)
    
    '''
    colorAdd = random.randint(random.randint(-255,0),random.randint(0,255))
    if r+colorAdd <= 255 and r+colorAdd >= 0:
        r += colorAdd
    
    colorAdd = random.randint(random.randint(-255,0),random.randint(0,255))
    if g+colorAdd <= 255 and g+colorAdd >= 0:
        g += colorAdd
    
    colorAdd = random.randint(random.randint(-255,0),random.randint(0,255))
    if b+colorAdd <= 255 and b+colorAdd >= 0:
        b += colorAdd
    '''
    
    pygame.display.update()
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            if currChar == 0:
                letterHRect.left = items[currChar].rect.left
                letterHRect.top = items[currChar].rect.top
                surface.blit(letterH, letterHRect)
                pygame.display.update()
                currChar+=1
                pygame.time.wait(250)

            elif currChar == 1:
                letterERect.left = items[currChar].rect.left
                letterERect.top = items[currChar].rect.top
                surface.blit(letterE, letterERect)
                pygame.display.update()
                currChar+=1
                pygame.time.wait(250)

            elif currChar == 2:
                letterLRect.left = items[currChar].rect.left
                letterLRect.top = items[currChar].rect.top
                surface.blit(letterL, letterLRect)
                pygame.display.update()
                currChar+=1
                pygame.time.wait(250)

            elif currChar == 3:
                letterORect.left = items[currChar].rect.left
                letterORect.top = items[currChar].rect.top
                surface.blit(letterO, letterORect)
                pygame.display.update()
                currChar+=1
                pygame.time.wait(250)

            elif currChar == 4:
                qMarkRect.left = items[currChar].rect.left
                qMarkRect.top = items[currChar].rect.top
                surface.blit(qMark, qMarkRect)
                pygame.display.update()
                currChar+=1
                pygame.time.wait(250)

        elif pressed[pygame.K_q]:
            pygame.quit()
            os._exit(1)


        

pygame.display.update()
for event in pygame.event.get():

    if event.type == pygame.QUIT:#hit the x and ends game
        pygame.quit()
        os._exit(1)


