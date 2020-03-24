import pygame
import sys
from tank_chars import *

#Variables
window_width= 965
window_height= 480

j=0
time_since_last_tank=0
kills=0
kills_to_next_level=4
lives=4
tank_speed=-3

#make lists & queues
tankList= []
tank_timer= [30, 70, 50]
bombList= []


#Initialize
pygame.init()

#Create display
screen= pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tank Defense")

background= pygame.image.load('bg.png').convert()

clock= pygame.time.Clock()

#Create characters
player= Plane(10, 60, 100, 20)

#Add characters to list
sprites_list= pygame.sprite.Group()
sprites_list.add(player)

#text for "lives remaining"
pygame.font.init()
myfont= pygame.font.Font('freesansbold.ttf', 20)



#Game Loop
while True:
    #set up background
    screen.blit(background, [0,0])

    #create tanks every few seconds
    time_since_last_tank += clock.tick()
    if time_since_last_tank > tank_timer[j]:
        newTank= Tank(window_width, window_height-50, 80, 40, tank_speed)
        tankList.append(newTank)
        sprites_list.add(newTank)
        time_since_last_tank=0
        if j==2:
            j=0
        else:
            j+=1


    #get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_SPACE):
                #make new bomb
                current_x= player.rect.centerx
                current_y= player.rect.bottom
                #make new bomb if not already 4
                if len(bombList) < 4:
                    newBomb= Bomb(current_x, current_y, 5, 5)
                    bombList.append(newBomb)
                    sprites_list.add(newBomb)

    #deal with bomb hitting tank or ground
    if len(bombList) != 0:
        #print(list(range(back, front)))
        for checkBomb in bombList:
            #check if bomb off screen
            if checkBomb.rect.top > window_height:
                checkBomb.kill()
                bombList.remove(checkBomb)

            #check all the tanks
            elif len(tankList) != 0:
                for checkTank in tankList:
                    #if bomb and tank collide, remove both
                    if pygame.sprite.collide_rect(checkTank, checkBomb):
                        checkTank.kill()
                        tankList.remove(checkTank)
                        checkBomb.kill()
                        bombList.remove(checkBomb)
                        kills += 1
                        #after certain number of kills, "level up" by moving
                        #   faster
                        if kills > kills_to_next_level:
                            kills=0
                            tank_speed -= 1
                            player.speed_up()

                    #if tank makes it all the way across (lose a life)
                    elif checkTank.rect.right < 0:
                        checkTank.kill()
                        lives -= 1
                        tankList.remove(checkTank)


    #update number of lives remaining
    livesText=myfont.render(('Lives Remaining: %s' % lives), True,(0,0,0))
    textRect= livesText.get_rect()
    textRect.center= (100,20)
    screen.blit(livesText, textRect)

    #game over if no more lives
    if lives == 0:
        gameOverText= myfont.render('GAME OVER', True, (0,0,0))
        gameOverTextRect= gameOverText.get_rect()
        gameOverTextRect.center= ((window_width / 2), (window_height / 2))
        screen.blit(gameOverText, gameOverTextRect)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()


    #update sprites
    for ent in sprites_list:
        ent.update()

    #draw, flip and wait for next frame
    sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(20)

