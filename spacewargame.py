import pygame
import random
import math
import time
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space War Game")
icon_logo=pygame.image.load('spaceship_logo.png')
pygame.display.set_icon(icon_logo)

welcome_screen=pygame.image.load('introspace.png')
'''dblespeed_img=pygame.image.load('C:\\Users\\one\\Downloads\\2xspeed.png')
slowdown_img=pygame.image.load('C:\\Users\\one\\Downloads\\slowdown.png')
dblespeed_img2=[dblespeed_img,slowdown_img]

dblespeed_img3 = random.choice(dblespeed_img2)'''

player_img=pygame.image.load('playerspace.png')


enemybullet_img=pygame.image.load('hot.png')
#global score
#highscore
global highscore
#highscore=0
enemy_img=pygame.image.load('alien.png')
global speedx

bullet_img = pygame.image.load("bulletimg.png")










def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y):

    screen.blit(enemy_img,(x,y))
def bullet(x,y):
    global bulletY,bulletY_chnge
    screen.blit(bullet_img,(x+15,y))
def enemy_attack(x,y):
    screen.blit(enemybullet_img,(x+15,y))

def calc_dist(x1,x2,y1,y2):
    return math.sqrt(math.pow((y2-y1),2)+math.pow((x2-x1),2))

def collide_distance(p1,p2,q1,q2):
    return math.sqrt(math.pow((q2-q1),2)+math.pow((p2-p1),2))

'''def scorerender(scre):
    fontstyle=pygame.font.Font('freesansbold.ttf',32)
    font=fontstyle.render(f'Score: {scre}',True,(255,0,0))
    font2=fontstyle.render(f'HighScore: {highscore}',True,(255,0,0))
    screen.blit(font,(40,60))
    screen.blit(font2,(510,60))'''



def music_loop(stop):  #background music loop
    if stop=='startmusic':
        mixer.init()
        mixer.music.load("bgsound.mp3")
        mixer.music.play(-1)
    else:
        mixer.music.stop()
        mixer.music.load('gameover.mp3')
        mixer.music.play()


def intro_Screen():
    while True:
        screen.blit(welcome_screen,(0,0))
        fontstyle=pygame.font.Font('freesansbold.ttf',32)
        font=fontstyle.render('Press Any Key To Start Your Game',True,(255,50,0))
        screen.blit(font,(170,530))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                return
            elif event.type==pygame.QUIT:
                pygame.quit()



intro_Screen()

def gamestartloop():
    working=True
    music_loop('startmusic')
    backx=0
    backy=0
    back_velo=10
    back_velo2=1
    init_time=time.time()
    speedtime=random.randint(1,20)
    playerX = 350
    playerY = 500
    playerX_chnge = 0
    playerX_chnge2 = 1
    enemyX = random.randint(0, 800)
    enemyY = random.randint(50, 150)
    enemyX_chnge = 10
    enemyX_chnge2 = 1

    enemyY_chnge = 0
    enemybulletY = enemyY
    speedy = 0
    speedy_chnge = 0
    enemybulletX = 0
    enemybulletY_chnge = 0

    bulletX = 0
    bulletY = 500
    bulletX_chnge = 0
    bulletY_chnge = 0
    bullet_state = "ready"
    speedx=random.randint(10,650)
    score=0
    highscore=0
    dblespeed_img = pygame.image.load('2xspeed.png')
    slowdown_img = pygame.image.load('slowdown.png')
    dblespeed_img2 = [dblespeed_img, slowdown_img]

    dblespeed_img3 = random.choice(dblespeed_img2)
    #dblespeed_img2 = [dblespeed_img, slowdown_img]
    #dblespeed_img3 = random.choice(dblespeed_img2)

    def speeddouble(x, y):

        screen.blit(dblespeed_img3, (x, y))

    def scorerender(scre):
        fontstyle = pygame.font.Font('freesansbold.ttf', 32)
        font = fontstyle.render(f'Score: {scre}', True, (255, 0, 0))
        font2 = fontstyle.render(f'HighScore: {highscore}', True, (255, 0, 0))
        screen.blit(font, (40, 60))
        screen.blit(font2, (510, 60))

    while working:

        screen.fill((0, 0, 0))

        background_img=pygame.image.load("spacebg.png")

        if backy>=600:
            backy=0
        backy+=back_velo*back_velo2
        screen.blit(background_img,(backx,backy))
        screen.blit(background_img,(backx,backy-600))
        pygame.display.update()







        if (time.time() - init_time) > speedtime:
            if speedy<750:
                speedy += 40
                speeddouble(speedx, speedy)
            if speedy>=750:
                speedy=0
                speedx=random.randint(10,650)
                init_time=time.time()
                dblespeed_img3=random.choice(dblespeed_img2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
                playerX_chnge =-11*playerX_chnge2
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                playerX_chnge=11*playerX_chnge2
            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_chnge=0*playerX_chnge2


                    enemybulletY_chnge=40

            if event.type==pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key==pygame.K_5):
                bullet_state="fire"
                bullet_sound=mixer.Sound('bulletsound.wav')
                bullet_sound.play()
                bulletX=playerX
                bulletY_chnge=-50






        playerX+=playerX_chnge


        if playerX<=0:
            playerX=0*playerX_chnge2
        elif playerX>=745:
            playerX=745

        enemyX += enemyX_chnge



        if enemyX<=0:
            enemyX_chnge=12*enemyX_chnge2
        if enemyX>=740:
            enemyX_chnge=-12*enemyX_chnge2





        if enemybulletY<750:
            enemybulletY+=enemybulletY_chnge
            enemy_attack(enemyX, enemybulletY)
        if enemybulletY >= 750:

            enemybulletY = enemyY

        enemy(enemyX,enemyY)


        # if bulletY<=-600:
        #   bulletY=500
        if bullet_state=="fire":
            bulletY+=bulletY_chnge
            bullet(bulletX, bulletY)

        if bulletY<=-540:
            bulletY=500
            bullet_state="ready"

        player(playerX,playerY)
        distance= calc_dist(enemyX,bulletX,enemyY,bulletY)
        distance2=collide_distance(enemyX,playerX,enemybulletY,playerY)
        distance3=collide_distance(speedx,playerX,speedy,playerY)
        if distance <= 29:
            score+=10
            mixer.Sound('coinpick.wav').play()
            enemyX=random.randint(0,800)
            enemyY=random.randint(30,190)
        scorerender(score)

        if distance2 <=27:
            fontstyle=pygame.font.Font('freesansbold.ttf',65)
            font= fontstyle.render('Game Over ',True,(255,45,90))
            font2=fontstyle.render('Press y for Restart',True,(255,30,90))
            font3 = fontstyle.render('Press q for Quit', True, (255, 30, 90))
            explode_img=pygame.image.load('explode128.png')
            screen.blit(explode_img,(playerX-27,playerY-26))
            screen.blit(font,(240,250))
            screen.blit(font2,(160,330))
            screen.blit(font3,(160,390))
            music_loop('stopmusic')
            pygame.display.update()
            with open('highscores', 'w') as f:
                f.write(str(highscore))
            working=False


        if distance3<=27 and dblespeed_img3==dblespeed_img:
            mixer.Sound('speedup.wav').play()
            speedy=0
            enemyX_chnge*=2
            enemyX_chnge2+=1
            playerX_chnge*=2
            playerX_chnge2+=1
            back_velo2+=1
            dblespeed_img3=random.choice(dblespeed_img2)

        if distance3<=27 and dblespeed_img3==slowdown_img:
            mixer.Sound('speeddown.wav').play()
            speedy=0
            enemyX_chnge*=0.5
            enemyX_chnge2-=0.5
            playerX_chnge*=0.5
            playerX_chnge2-=0.5
            back_velo2-=0.5
            dblespeed_img3=random.choice(dblespeed_img2)



        pygame.display.update()

        with open('highscores','r') as f:
           highscore = f.read()

        if score>int(highscore):
            highscore=score


gamestartloop()
gameover=True
'''with open('C:\\Users\\one\\Downloads\\highscores','w') as f:
    f.write(str(highscore))'''
while gameover:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameover=False
        if event.type==pygame.KEYDOWN and (event.key == pygame.K_y or event.key == pygame.K_Y):
            gamestartloop()
        if event.type==pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_Q):
            pygame.quit()


