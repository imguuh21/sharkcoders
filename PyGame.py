import pygame

pygame.init()
tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Minha primeira Janela Pygame")

fundo = (30, 30, 30)
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False


    tela.fill((0, 0, 0))
    pygame.draw.rect(tela,(250, 0, 0), (50, 50, 100, 80))
    pygame.draw.circle(tela, (0, 250, 0),(328,240),40)
    pygame.draw.line(tela,(0, 0, 250),(0, 0),(640,480), 3)
    pygame.display.flip()

#Teclas pressionadas
#keys = pygame.key.get_pressed()
#if keys[pygame.K_LEFT]:
 #   x -= velocidade
#if keys[pygame.K_RIGHT]:
  #  x -=

    tela.fill(fundo)
pygame.quit()