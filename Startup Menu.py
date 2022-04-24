import pygame
from io import open

file = open("Virus Scape 1.2.5.py", "r")

#Window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Startup Menu')

#Loading Images
start = pygame.image.load('start_btn.png').convert_alpha()
exit = pygame.image.load('exit_btn.png').convert_alpha()

#Buttons class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #Get mouse pos
        pos = pygame.mouse.get_pos()
        
        #check mouse pos
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
              self.clicked = True  
              action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


#Create buttons
startbtn = Button(100, 200, start, 0.8)
exitbtn = Button(450, 200, exit, 0.8)


#Loop
run = True
while run:

    screen.fill((0, 0, 0))
    file = open("Virus Scape 1.2.5.exe")

    if startbtn.draw() == True:
        file
    if exitbtn.draw() == True:
        run = False


    #Event Handler
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()