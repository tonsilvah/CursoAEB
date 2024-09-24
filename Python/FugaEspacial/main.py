"""Jogo: Fuga Espacial
Descrição: Um grupo de diplomatas escapam de uma fortaleza estelar a bordo de uma nave danificada.
    A Nave precisa se desviar das ameaças e sobreviver até atingir a zona de segurança diplomática

"""

import pygame

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

class Game:
    # Inicializar atributos
    screen = None
    screen_size = None
    width = 800
    height = 600
    run = True
    background = None
    player = None
    
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
    
    def loop(self):
        
        velocidade_background = 10
        
        #margem esquerda
        movL_x = 0
        movL_y = 0
        
        #margem direita
        movR_x = 740
        movR_y = 0
        
        self.background = Background()  # Criar objeto background
        
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
            
            
            pygame.display.update()


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

# Instanciar o objeto do jogo após a definição da classe
game = Game("resolution", "fullscreen")
game.loop()  # Iniciar Jogo
