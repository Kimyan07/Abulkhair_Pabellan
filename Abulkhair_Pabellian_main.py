import pygame
import math
import random
# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background


# title and icon
pygame.display.set_caption("way out")
icon = pygame.image.load('416034346_1426594797927676_8182486983181807346_n.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('423599974_3567411103574296_2719788159049267038_n.png')
playerX = 370
playerY = 530
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('403396287_874072994271834_1593678345164473224_n.png'))
    enemyX.append(random.randint(0, 600))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(20)

# Bullet
# Ready means you cannot see the bullet on the screen
# Fire means the bullet is currently moving

bulletImg = pygame.image.load('423599974_3567411103574296_2719788159049267038_n.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 1.5
bullet_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX,      2) ) +   (                math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:

    screen.fill((0, 0, 0))  # rgb color background
    screen.blit(background, (0, 0))  # background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check if it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # checking boundaries for player and enemy
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 750:
        playerX = 750

    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 750:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

     # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 530
            bullet_state = "ready"
            score += 1  # Increase the score by 1 everytime it hits an enemy
            print(score)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 530
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)

    pygame.display.update()
