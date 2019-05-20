import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my second game")

x = 0
y = 0
width = 50
height = 50
vol = 5
direct = "right"


run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x == 0:
        direct = "right"
        y += 25
    elif x == 450:
        direct = "left"
        y += 25
    if direct == "right":
        x += vol
    elif direct == "left":
        x -= vol

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
