import pygame
pygame.init()
screen = pygame.display.set_mode([800, 500])
running = True
horizontal = 0
vertical = 0
while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      vertical -= 1
    if keys[pygame.K_DOWN]:
      vertical += 1
    if keys[pygame.K_LEFT]:
      horizontal -= 1
    if keys[pygame.K_RIGHT]:
      horizontal += 1
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (horizontal, vertical), 75)
    pygame.display.flip()
    
pygame.quit()
