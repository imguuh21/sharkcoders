import pygame
import random

pygame.init()

LARGURA = 640
ALTURA = 480

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Circulo que move")

fundo = (200, 0, 200)

CORES = [
    (0, 255, 0),    # Verde
    (255, 255, 0),  # Amarelo
    (0, 255, 255),  # Ciano
    (255, 0, 0),    # Vermelho
    (255, 255, 255) # Branco
]
cor_atual = CORES[0]

x = LARGURA // 2
y = ALTURA // 2

tamanho = 50

velocidade = 1

relogio = pygame.time.Clock()

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocidade
    if keys[pygame.K_RIGHT]:
        x += velocidade
    if keys[pygame.K_UP]:
        y -= velocidade
    if keys[pygame.K_DOWN]:
        y += velocidade

    if x < tamanho:
        x = tamanho
    if x > LARGURA - tamanho:
        x = LARGURA - tamanho
    if y < tamanho:
        y = tamanho
    if y > ALTURA - tamanho:
        y = ALTURA - tamanho
    tela.fill(fundo)
    pygame.draw.circle(tela,(cor_atual),(0, 255, 0),( x, y), 25)
    pygame.display.flip()

pygame.quit()
