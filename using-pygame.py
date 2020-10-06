import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode([800, 600])

red = (255, 0, 0)
green = (0, 255, 0)

centerx, centery = screen.get_rect().centerx, screen.get_rect().centery
deltaY = centery + 40


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.fill(0)
    #rect = pygame.draw.rect(screen, red, [100, 100, 600, 400], 10)
    font = pygame.font.SysFont('Courier', 30)
    msg = font.render("Hello World!!!", True, red)
    
    deltaY -= 0.5
    pos = msg.get_rect(center = (centerx, centery + deltaY))

    if (centery + deltaY < 0):
        running = False
    screen.blit(msg, pos)
    
    pygame.display.update()

pygame.quit()