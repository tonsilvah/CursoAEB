"""Jogo: Fuga Espacial
Descrição: Um grupo de diplomatas escapam de uma fortaleza estelar a bordo de uma nave danificada.
    A Nave precisa se desviar das ameaças e sobreviver até atingir a zona de segurança diplomática

"""

import pygame
import time
import random
import os
import sys

class Player:
    #definição do Jogador
    image = None
    x = None  
    y = None
    
    #inicializa os atributos do Jogador(player)
    def __init__(self, x, y):
        
        player_fig = pygame.image.load("Images/player.png")
        player_fig.convert()
        player_fig = pygame.transform.scale(player_fig,(90,90))
        self.image = player_fig
        self.x = x
        self.y = y
    
    #método que desenhar o Jogador (player)
    def draw(self, screen, x, y):
        screen.blit(self.image, (x,y))

class Background:
    image = None        
    margin_left = None
    margin_right = None
    
    def __init__(self):

        #definição da imagem
        background_fig = pygame.image.load("Images/background.png")
        background_fig = background_fig.convert()
        background_fig = pygame.transform.scale(background_fig,(800,602))
        self.image = background_fig
        
        #transformação das margens para resolução útil
        margin_left_fig = pygame.image.load("Images/margin_1.png")
        margin_left_fig.convert()
        margin_left_fig = pygame.transform.scale(margin_left_fig,(60,602))
        self.margin_left = margin_left_fig
        
        margin_right_fig = pygame.image.load("Images/margin_2.png")
        margin_right_fig.convert()
        margin_right_fig = pygame.transform.scale(margin_right_fig,(60,602))
        self.margin_right = margin_right_fig
    
    def update(self, dt):
        pass
    
    #renderiza a imagem
    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        #margens plano de fundo, move a imagem para o centro mostrando as bordas
        screen.blit(self.margin_left, (0, 0))
        screen.blit(self.margin_right, (740, 0))
    
    def move(self, screen, scr_height, movL_x, movL_y, movR_x, movR_y):
        for i in range(0,2):
            screen.blit(self.image,(movL_x,movL_y-i*scr_height))
            screen.blit(self.margin_left,(movL_x,movL_y-i*scr_height))
            screen.blit(self.margin_right,(movL_x,movL_y-i*scr_height))

    margin_left = None
    margin_right = None

class Hazard:
    image = None
    x= None
    y= None
    
    def __init__(self, img, x, y):
        hazard_fig = pygame.image.load(img)
        hazard_fig.convert()
        hazard_fig = pygame.transform.scale(hazard_fig,(130,130))
        self.image = hazard_fig
        self.x = x
        self.y = y
    
    def draw (self, screen, x, y):
        screen.blit(self.image,(x,y))

class Soundtrack:
    soundtrack = None
    sound = None
    
    def __init__(self, soundtrack):
        if os.path.isfile(soundtrack):
            self.soundtrack = soundtrack
        else:
            print(soundtrack+ " not found... ignoring", file=sys.stderr)
    
    def play(self):
        pygame.mixer.music.load(self.soundtrack)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)

    def set(self, soundtrack):
        if os.path.isfile(soundtrack):
            self.soundtrack = soundtrack
        else:
            print(soundtrack+" not found... ignoring", file=sys.stderr)

    def play_sound(self, sound):
        
        if os.path.isfile(sound):
            self.sound = sound
            pygame.mixer.music.load(self.sound)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
        else:
            print(sound+" file not found... ignoring", file=sys.stderr)
            
class Game:
    # Inicializar atributos
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None
    player = None
    hazard = []
    render_text_bateuLateral = None
    render_text_perdeu = None
    
    #Movimentos do Jogador
    DIREITA = pygame.K_RIGHT
    ESQUERDA = pygame.K_LEFT
    mudar_x = 0.0
    
    # Operações
    def __init__(self, size, fullscreen):
        
        # Inicializa o pygame
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_size = self.screen.get_size()   # Definir tamanho da tela do jogo
        
        pygame.mouse.set_visible(0)     # Desabilitar o mouse
        pygame.display.set_caption('Fuga Espacial')     # Definir caption da janela do jogo

        my_font = pygame.font.Font("Fonts/Fonte4.ttf",100)
        
        self.render_text_bateuLateral = my_font.render("VOCÊ BATEU",0,(255,255,255))
        self.render_text_perdeu = my_font.render("GAME OVER",0,(255,0,0))
        
    def handle_events(self):
        # Trata a saída do jogo
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.run = False
        
            #QUANDO O TECLADO É ACIONADO, SELECIONA A POSIÇÃO DA NAVE"
            if event.type == pygame.KEYDOWN:
                
                if event.key == self.ESQUERDA:
                    self.mudar_x = -3
                    
                if event.key == self.DIREITA:
                    self.mudar_x = 3
            
            if event.type == pygame.KEYUP:
                if event.key == self.ESQUERDA or event.key == self.DIREITA:
                    self.mudar_x = 0
            
    def elements_update(self, dt):
        self.background.update(dt)   # Atualiza elementos

    def elements_draw(self):
        self.background.draw(self.screen)    # Desenhar elementos
    
    def play_soundtrack(self):
    #definicao do som de fundo
    
        if os.path.isfile('Sounds/song.wav'):
            pygame.mixer.music.load('Sounds/song.wav')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(loops=1)
        else:
            print("Sounds/song.mp3 not found... ignoring", file=sys.stderr)
    
    def play_sound(self, sound):
        if os.path.isfile(sound):
            pygame.mixer.music.load(sound)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()

        else:
            print("Sound file not found... ignoring", file=sys.stderr)
     
    def loop(self):
    #laço principal do jogo
        score = 0
        h_passou = 0
        
        velocidade_background = 10
        velocidade_hazard = 10
        
        #margem esquerda
        movL_x = 0
        movL_y = 0
        
        #margem direita
        movR_x = 740
        movR_y = 0
       
       #localização dos obstaculos 
        hzrd = 0
        h_x = 0
        h_y = -500
        
        #dimensoes dos obstaculos
        h_width = 100
        h_height = 100
        
        self.background = Background()  # Criar objeto background
        
        self.play_soundtrack()
        
        #criar os hazards - obstaculos
        self.hazard.append(Hazard("Images/satelite.png",h_x,h_y))
        self.hazard.append(Hazard("Images/nave.png",h_x,h_y))
        self.hazard.append(Hazard("Images/cometaVermelho.png",h_x,h_y))
        self.hazard.append(Hazard("Images/meteoros.png",h_x,h_y))
        self.hazard.append(Hazard("Images/buracoNegro.png",h_x,h_y))
        
        #criar trilha sonora
        self.soundtrack = Soundtrack('Sounds/song.wav')
        self.soundtrack.play()
        
        #Posição do Jogador
        x = (self.width-56)/2
        y = (self.height-125)
        
        #Criação do Jogador
        self.player = Player(x,y)
        
        clock = pygame.time.Clock()  # Inicializar relogio
        dt = 16
        
        # Loop principal do programa
        while self.run:
            clock.tick(1000/dt)
            self.handle_events()
            self.elements_update(dt)
            self.elements_draw()
            
            #adiciona movimento ao background
            self.background.move(self.screen,self.height,movL_x,movL_y,movR_x,movR_y)
            movL_y = movL_y + velocidade_background
            movR_y = movR_y + velocidade_background
            
            #caso a imagem ultrapasse a tela, ela volta ao topo, gera o loop infinito
            if movL_y > 600 and movR_y > 600:
                movL_y -=600
                movR_y -=600

            #MOVIMENTAÇÃO DO PLAYER
            x = x + self.mudar_x
            
            #desenhar player
            self.player.draw(self.screen,x,y)
            self.score_card(self.screen,h_passou,score)
            
            if x >760-92 or x<40+5:
                self.soundtrack.play_sound('Sounds/jump2.wav')
                
                self.screen.blit(self.render_text_bateuLateral,(80,200))            
                pygame.display.update()
                time.sleep(3)
                self.loop()
                #self.run = False
                
            
            #adicionando movimento ao hazard
            h_y = h_y + velocidade_hazard/4
            self.hazard[hzrd].draw(self.screen,h_x,h_y)
            h_y = h_y + velocidade_hazard
            
            if h_y > self.height:
                h_y = 0-h_height
                h_x = random.randrange(125,650-h_height)
                hzrd = random.randint(0,4)
                h_passou = h_passou+1
                score = h_passou*10
            
            pygame.display.update()

    def score_card(self, screen, h_passou, score):
        font = pygame.font.SysFont(None, 35)
        passou = font.render("Passou: " + str(h_passou), True, (255,255,128))
        score = font.render("Score: " + str(score), True, (253,231,32))
        screen.blit(passou,(0,50))
        screen.blit(score,(0,100))

# Instanciar o objeto do jogo após a definição da classe
game = Game("resolution", "fullscreen")
game.loop()  # Iniciar Jogo
