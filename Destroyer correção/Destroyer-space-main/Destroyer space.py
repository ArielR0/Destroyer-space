 
import pygame

import random

pygame.init ()

x = 1280
y= 720

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Destroier Space')

img = pygame.image.load('imagens./ng.png')

game_over_img = pygame.image.load('imagens/game.png').convert_alpha()
game_over_img = pygame.transform.scale(game_over_img, (600, 200))

alien = pygame.image.load('imagens/aliensp.png').convert_alpha()
alien = pygame.transform.scale(alien, (60,50))

alien = pygame.image.load('imagens/alien2.png').convert_alpha()
alien = pygame.transform.scale(alien, (60,50))

alien = pygame.image.load('imagens/alien3.png').convert_alpha()
alien = pygame.transform.scale(alien, (60,50))


playerimg = pygame.image.load('imagens/nave.png').convert_alpha()
playerimg = pygame.transform.scale(playerimg, (50,50)) #tamanho da nave
playerimg = pygame.transform.rotate(playerimg, -90)

missil = pygame.image.load('imagens/missile.png').convert_alpha()
missil = pygame.transform.scale(missil, (25,25))
missil = pygame.transform.rotate(missil, -45)

pos_alien_x= 500
pos_alien_y= 360

pos_playerimg_x= 200
pos_playerimg_y= 300

vel_x_missil = 0
pos_x_missil = 200
pos_y_missil = 300

pontos = 3

triggered = False

rodando = True

font = pygame.font.SysFont('arial', 50)


playerimg_rect = playerimg.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()


#funções
def respanw():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respanw_missil():
   triggered = False
   respanw_x_missil = pos_playerimg_x
   respanw_y_missil = pos_playerimg_y
   vel_x_missil = 0
   return [respanw_x_missil, respanw_y_missil, triggered, vel_x_missil]

def colisions():
   global pontos
   if playerimg_rect.colliderect(alien_rect) or alien_rect.x == 60:
      pontos -=1
      return True
   elif missil_rect.colliderect(alien_rect):
      pontos +=1
      return True
   else:
      return False





while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         rodando = False
    
    
    screen.blit(img, (0, 0))

    rel_x = x % img.get_rect().width
    screen.blit(img, (rel_x - img.get_rect().width,0)) #criar backgroud
    if rel_x < 1280:
       screen.blit(img, (rel_x, 0))



    #Teclas

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_playerimg_y > 1:
     pos_playerimg_y -=8
     
     if not triggered:
          pos_y_missil -=8
     
    if tecla[pygame.K_DOWN] and pos_playerimg_y < 665:
     pos_playerimg_y +=8
     
     if not triggered:
          pos_y_missil +=8

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_missil = 8

    if pontos == -1:
         pygame.display.update()
         pygame.time.delay(3000)
         rodando = False
    #Respanw 

    if pos_alien_x == 50:
        pos_alien_x = respanw()[0]
        pos_alien_y = respanw()[1]

    if pos_x_missil == 1080:
       pos_x_missil, pos_y_missil, triggered, vel_x_missil = respanw_missil() 

    if pos_alien_x == 50 or colisions():
        pos_alien_x = respanw()[0]
        pos_alien_y = respanw()[1]

    #posição rect

    playerimg_rect.y = pos_playerimg_y
    playerimg_rect.x = pos_playerimg_x

    missil_rect.x = pos_x_missil
    missil_rect.y = pos_y_missil

    alien_rect.x = pos_alien_x
    alien_rect.y = pos_alien_y


    #movimento
    x-=6
    pos_alien_x-=4
    
    pos_x_missil += vel_x_missil

    pygame.draw.rect(screen, (0, 0, 0), playerimg_rect, 1)
    pygame.draw.rect(screen, (0, 0, 0), missil_rect, 1)
    pygame.draw.rect(screen, (0, 0, 0), alien_rect, 1)

    score = font.render(f' Pontos: {int(pontos)} ', True, (244,244,244))
    screen.blit(score, (50,50))

    #imagens do jogo
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_x_missil,pos_y_missil))
    screen.blit(playerimg, (pos_playerimg_x, pos_playerimg_y))

    print(pontos)

    pygame.display.update()