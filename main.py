# Imports
import pygame, sys
from tkinter import font
import pygame
import os
import time
import random
from pygame import display
from pygame.locals import *

# Center the Game Application


os.environ['SDL_VIDEO_CENTERED'] = '1'



#Text render


def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText



# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
grey=(64, 64, 64)



# Game Fonts
font = "RetronoidItalic-8Xg2.ttf"
font2 = "RetronoidItalic-8Xg2.ttf"




# Main Menu
# Main Menu
# Main Menu
def main1_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        main_menu()
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        WIN.fill(grey)
        title=text_format("Formula Invaders", font2, 77, black)
        if selected=="start":
            text_start=text_format("START", font2, 60, white)
        else:
            text_start = text_format("START", font2, 60, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font2, 60, white)
        else:
            text_quit = text_format("QUIT", font2, 60, black)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()





        #If the user clicks the start button it takes them to main_menu()
        if start_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                main_menu()




        # Main Menu Text
        WIN.blit(title, (WIDTH / 2 - (title_rect[2] / 2), 80))
        WIN.blit(text_start, (WIDTH / 2 - (start_rect[2] / 2), 300))
        WIN.blit(text_quit, (WIDTH / 2 - (quit_rect[2] / 2), 360))
        pygame.display.update()
        pygame.display.set_caption("Start Menu")

# Initializing
mainClock = pygame.time.Clock()
pygame.init()

# Width and height of the window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# App Captions
pygame.display.set_caption("F1 Invaders")

# Text Initialization
pygame.font.init()
font = pygame.font.SysFont('Corbel', 15)


# Buttons class
class button():
    # Setting the button
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    # Drawing the button to the window
    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        # Handles text if any
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 22)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    # Checks if certain coordinates are over the button
    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


# Draws Text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Main menu
def main_menu():
    WIN.fill((64, 64, 64))
    run = True
    draw_text(' ', font, (255, 255, 255), WIN, 20, 20)





    # Lewis Hamilton
    lewisX = 50
    lewisY = 50
    lewisButton = button((64, 64, 64), lewisX, lewisY, 100, 100)
    lewisButton.draw(WIN, (64, 64, 64))
    lewisPunk = pygame.image.load(os.path.join("FinalAssets", "LewisPUNK.png"))
    lewisPunk = pygame.transform.scale(lewisPunk, (100, 100))
    WIN.blit(lewisPunk, (lewisX, lewisY))

    # Max Verstappen
    verstappenX = 50
    verstappenY = lewisY + 150
    verstappenButton = button((64, 64, 64), verstappenX, verstappenY, 100, 100)
    verstappenButton.draw(WIN, (64, 64, 64))
    verstappenPunk = pygame.image.load(os.path.join("FinalAssets", "VerstappenPUNK.png"))
    verstappenPunk = pygame.transform.scale(verstappenPunk, (100, 100))
    WIN.blit(verstappenPunk, (verstappenX, verstappenY))

    # Charles Leclerc
    leclercX = 50
    leclercY = verstappenY + 150
    leclercButton = button((64, 64, 64), leclercX, leclercY, 100, 100)
    leclercButton.draw(WIN, (64, 64, 64))
    leclercPunk = pygame.image.load(os.path.join("FinalAssets", "LeclercPUNK.png"))
    leclercPunk = pygame.transform.scale(leclercPunk, (100, 100))
    WIN.blit(leclercPunk, (leclercX, leclercY))

    # Tatiana Calderon
    calderonX = lewisX + 150
    calderonY = lewisY
    calderonButton = button((64, 64, 64), calderonX, calderonY, 100, 100)
    calderonButton.draw(WIN, (64, 64, 64))
    calderonPunk = pygame.image.load(os.path.join("FinalAssets", "CalederonPUNK.png"))
    calderonPunk = pygame.transform.scale(calderonPunk, (100, 100))
    WIN.blit(calderonPunk, (calderonX, calderonY))

    # Lando Norris
    norrisX = calderonX
    norrisY = verstappenY
    norrisButton = button((64, 64, 64), norrisX, norrisY, 100, 100)
    norrisButton.draw(WIN, (64, 64, 64))
    norrisPunk = pygame.image.load(os.path.join("FinalAssets", "NorrisPUNK.png"))
    norrisPunk = pygame.transform.scale(norrisPunk, (100, 100))
    WIN.blit(norrisPunk, (norrisX, norrisY))

    # Credits Button
    creditButton = button((255, 0, 0), WIDTH - 150, 50, 100, 50, "Credits")
    creditButton.draw(WIN, (255, 255, 255))

    # Tutorial Button
    tutorialButton = button((255, 0, 0), WIDTH - 150, 150, 100, 50, "Tutorial")
    tutorialButton.draw(WIN, (255, 255, 255))

    # Event runner
    while run:
        # Updating the display
        pygame.display.update()

        # Checking for events
        for event in pygame.event.get():
            # Getting mouse coordinates
            pos = pygame.mouse.get_pos()

            # Quits the app if the user exits
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            # Handles button clicks
            global F1_CAR
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lewisButton.isOver(pos):
                    # If the user clicks Hamilton
                    F1_CAR = pygame.image.load(os.path.join("FinalAssets", "HamiltonCar.png"))
                    tire_menu()
                elif verstappenButton.isOver(pos):
                    # If the user clicks Verstappen
                    F1_CAR = pygame.image.load(os.path.join("FinalAssets", "VerstappenCar.png"))
                    tire_menu()
                elif leclercButton.isOver(pos):
                    # If the user clicks Leclerc
                    F1_CAR = pygame.image.load(os.path.join("FinalAssets", "LeclercCar.png"))
                    tire_menu()
                elif calderonButton.isOver(pos):
                    # If the user clicks Calderon
                    F1_CAR = pygame.image.load(os.path.join("FinalAssets", "CalderonCar.png"))
                    tire_menu()
                elif norrisButton.isOver(pos):
                    # If the user clicks Calderon
                    F1_CAR = pygame.image.load(os.path.join("FinalAssets", "NorrisCar.png"))
                    tire_menu()
                elif creditButton.isOver(pos):
                    credit_menu()
                elif tutorialButton.isOver(pos):
                    tutorial_menu()


# Tire menu
def tire_menu():
    run = True

    draw_text('Tire Selection Menu', font, (255, 255, 255), WIN, 20, 20)

    # Resetting the window
    WIN.fill((0, 0, 0))

    # Back button
    goBackButton = button((255, 255, 255), WIDTH - 150, 50, 100, 50, "Back")
    goBackButton.draw(WIN, (0, 0, 0))

    # Soft Tires
    softChoice = button((255, 255, 255), 50, 50, 100, 100, "Soft Tires")
    softChoice.draw(WIN, (0, 0, 0))

    # Medium Tires
    medChoice = button((255, 255, 255), 200, 50, 100, 100, "Medium Tires")
    medChoice.draw(WIN, (0, 0, 0))

    # Hard Tires
    hardChoice = button((255, 255, 255), 350, 50, 100, 100, "Hard Tires")
    hardChoice.draw(WIN, (0, 0, 0))

    # Event runner
    while run:
        # Updating the display
        pygame.display.update()

        # Checks for events
        for event in pygame.event.get():
            # Getting mouse coordinates
            pos = pygame.mouse.get_pos()

            # Quits the app if the user exits
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            # Handles the button clicks
            global playerLaser
            if event.type == pygame.MOUSEBUTTONDOWN:
                if softChoice.isOver(pos):
                    # If the user chooses soft tires
                    playerLaser = pygame.image.load(os.path.join("FinalAssets", "SoftTyre.png"))
                    game()
                elif medChoice.isOver(pos):
                    # If the users chooses medium tires
                    playerLaser = pygame.image.load(os.path.join("FinalAssets", "MedTire.png"))
                    game()
                elif hardChoice.isOver(pos):
                    # If the user chooses hard tires
                    playerLaser = playerLaser = pygame.image.load(os.path.join("FinalAssets", "HardTyres.png"))
                    game()
                elif goBackButton.isOver(pos):
                    main_menu()
                # if start_button is clicked go to main_menu()
                elif start_button.isOver(pos):
                    main_menu()








# Credits menu
def credit_menu():
    run = True

    draw_text('Credits Menu', font, (255, 255, 255), WIN, 20, 20)

    # Resetting the window
    WIN.fill((0, 0, 0))

    # Go back Button
    goBackButton = button((255, 0, 0), WIDTH - 150, 50, 100, 50, "Back")
    goBackButton.draw(WIN, (255, 255, 255))

    # Event runner
    while run:
        # Updates the displays
        pygame.display.update()

        # Checks for events
        for event in pygame.event.get():
            # Gets mouse coordinates
            pos = pygame.mouse.get_pos()

            # Quits the app if the user exits
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            # Handles button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if goBackButton.isOver(pos):
                    # If the user clicks the back button
                    main_menu()


# Tutorial Menu
def tutorial_menu():
    run = True

    WIN.fill((0, 0, 0))

    # Back Button
    goBackButton = button((255, 0, 0), WIDTH - 150, 50, 100, 50, "Back")
    goBackButton.draw(WIN, (255, 255, 255))

    # Event runner
    while run:
        # Updates the displays
        pygame.display.update()

        # Checks for events
        for event in pygame.event.get():
            # Gets mouse coordinates
            pos = pygame.mouse.get_pos()

            # Quits the app if the user exits
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            # Handles button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if goBackButton.isOver(pos):
                    # If the user clicks the back button
                    main_menu()


# Loading images
# Enemy Space Ships
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


# Lasers class
class Laser:
    # Initializion
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    # Draws the laser
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    # Moves the laser
    def move(self, vel):
        self.y += vel

    # Checks if the laser is off screen
    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    # Checks for collisions
    def collision(self, obj):
        return collide(self, obj)


# Ship class
class Ship:
    # Shooting cooldown
    COOLDOWN = 30

    # Initialization
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    # Draws the ship
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    # Moves the laser and handles collisions
    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    # Handles cooldown on lasers
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    # Handles shooting
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    # Gets the width of the ship
    def get_width(self):
        return self.ship_img.get_width()

    # Gets the height of the ship
    def get_height(self):
        return self.ship_img.get_height()


# User player class
class Player(Ship):

    # Initialization
    def __init__(self, x, y, health=101):
        super().__init__(x, y, health)
        self.ship_img = F1_CAR
        self.laser_img = playerLaser
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    # Handles player shooting
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    # Draws the users ship and health bar
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    # Handles the healthbar
    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (
            self.x, self.y + self.ship_img.get_height() + 10,
            self.ship_img.get_width() * (self.health / self.max_health),
            10))


# Enemey ships
class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }

    # Initializing
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    # Moves the enemy ships
    def move(self, vel):
        self.y += vel

    # Has the enemy ships shoot
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


# Checks for collisions
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


# Main game functions
def game():
    run = True
    FPS = 120
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 5

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    # Redraws the window
    def redraw_window():
        WIN.blit(BG, (0, 0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        pygame.display.update()

    # Event runner
    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),
                              random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        # Checks for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:  # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH:  # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:  # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT:  # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        # Handles the enemies
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

main1_menu()
main_menu()
