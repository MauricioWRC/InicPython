from lib2to3.pygram import python_grammar_no_print_statement
import pygame, os, sys, time
from random import randint, randrange
from time import sleep
pygame.init()

x = 600
y = 600

tela = pygame.display.set_mode((x,y))
pygame.display.set_caption('Jogo Py')

fundo = pygame.image.load('imagem/fundo.png').convert_alpha()
fundo = pygame.transform.scale(fundo, (x,y))

nave = pygame.image.load('imagem/nave.png').convert_alpha()
nave = pygame.transform.scale(nave, (100,100))

allien = pygame.image.load('imagem/allien.png').convert_alpha()
allien = pygame.transform.scale(allien, (100,100))

missil = pygame.image.load('imagem/missil.png').convert_alpha()
missil = pygame.transform.scale(missil, (30,30))

missil1 = pygame.image.load('imagem/missil.png').convert_alpha()
missil1 = pygame.transform.scale(missil1, (30,30))

Xallien = 500
Yallien = randrange(0,500,50)

Xnave = 300 
Ynave = 200

Xmissil = 350
Ymissil = 250
Vmissil = 0
tiro = False

Xmissil1 = 350
Ymissil1 = 221
Vmissil1 = 0

pontos = 3

rodando = True

nave_rect = pygame.draw.rect(tela, (0,255,0), (Xnave,Ynave, 50,50))
allien_rect = pygame.draw.rect(tela, (0,255,0), (Xallien,Yallien, 70,60))
missil_rect = pygame.draw.rect(tela, (0,255,0), (Xmissil,Ymissil, 40,10))
missil1_rect = pygame.draw.rect(tela, (0,255,0), (Xmissil1,Ymissil1, 40,10))

fonte = pygame.font.SysFont('arial', 40, True, True )

Vallien = 0.5
tempo = 1

Vale = 0.5

def Rmissil():
    tiro = False
    RmissilX = Xnave + 50
    RmissilY = Ynave + 50
    Vmissil = 0
    return[RmissilX, RmissilY, tiro, Vmissil]

def Rmissil1():
    tiro = False
    RmissilX1 = Xnave + 50
    RmissilY1 = Ynave + 21
    Vmissil1 = 0
    return[RmissilX1, RmissilY1, tiro, Vmissil1]

def colisao():
    global pontos
    if nave_rect.colliderect(allien_rect) or Xallien < -100:
        pontos -= 1
        return True
    elif missil_rect.colliderect(allien_rect) or missil1_rect.colliderect(allien_rect):
        pontos += 1
        return True
    else:
        return False

while rodando:
    
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, False, (255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
    tela.blit(fundo,(0,0))
    rel_x = x % fundo.get_rect().width
    tela.blit(fundo, (rel_x - fundo.get_rect().width,0))
    if rel_x < 600:
        tela.blit(fundo, (rel_x, 0))
    
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_w] and Ynave > 0:
        Ynave -= 1 + pontos/40
        if not tiro:
            Ymissil -= 1 + pontos/40
            Ymissil1 -= 1 + pontos/40

    if tecla[pygame.K_s] and Ynave <= 500:
        Ynave += 1 + pontos/40
        if not tiro:
            Ymissil += 1 + pontos/40
            Ymissil1 += 1 + pontos/40

    if tecla[pygame.K_a] and Xnave > 0:
        Xnave -= 1 + pontos/40
        if not tiro:
            Xmissil -= 1 + pontos/40
            Xmissil1 -= 1 + pontos/40

    if tecla[pygame.K_d] and Xnave <= 500:
        Xnave += 1 + pontos/40
        if not tiro:
            Xmissil += 1 + pontos/40
            Xmissil1 += 1 + pontos/40
        #////////colisao
    if Xallien < -101 or colisao():
        Xallien = 600
        Yallien = randint(0,y - 100)
        Vale = randint(5,10)
        
    if tecla[pygame.K_SPACE]:
        tiro = True
        Vmissil = 2 + pontos/20
        Vmissil1 = 2 + pontos/10
    if tecla[pygame.K_q]:
        sleep(0.005)

    if Xmissil > 600:
        Xmissil, Ymissil, tiro, Vmissil = Rmissil() 
    if Xmissil1 > 600:
        Xmissil1, Ymissil1, tiro, Vmissil1 = Rmissil1()

    if pontos < 1:
        rodando = False
    
    Xmissil += Vmissil  
    Xmissil1 += Vmissil1  

    x -= 0.2
    Xallien -=  Vale/10 + pontos/100

    nave_rect.y = Ynave + 25
    nave_rect.x = Xnave + 25

    allien_rect.y = Yallien + 20
    allien_rect.x = Xallien + 15

    missil_rect.y = Ymissil + 11
    missil_rect.x = Xmissil - 15

    missil1_rect.y = Ymissil1 + 11
    missil1_rect.x = Xmissil1 - 15

    #pygame.draw.rect(tela, (255,0,0), nave_rect, 4)
    #pygame.draw.rect(tela, (255,0,0), allien_rect, 4)
    pygame.draw.rect(tela, (255,0,0), missil_rect, 4)
    pygame.draw.rect(tela, (255,0,0), missil1_rect, 4)

    tela.blit(missil1, (Xmissil1 , Ymissil1))
    tela.blit(missil, (Xmissil , Ymissil))
    tela.blit(allien, (Xallien , Yallien))
    tela.blit(nave, (Xnave , Ynave))
    tela.blit(texto, (300,500))
    
    pygame.display.flip()