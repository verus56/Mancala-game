import sys
from mancalaBoard import MancalaBoard
import pygame
import time
import random
from play import Play
from game import Game
from Button import Button

# intilisation de la fentere ' jeu '
pygame.init()

# la taille de la fenetre
SCREEN_WIDTH, SCREEN_HEIGHT = (1280, 720)

# cela sera utile dans le drawing du rectagle qui correspand au Board
WIDTH, HEIGHT = (1100, 700)
Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# chargment de l'image qui servira comme un background du board
BG = pygame.image.load("assets/Background.jpg")

# charger le font en font arial ' pixel font '
font = pygame.font.Font('assets/abg.ttf', 20)
pygame.display.set_caption("Macala")

# configuration des couleurs
BROWN = (148, 120, 81)
LIGHT_GREEN = (20, 199, 109)
BLUE_A = (10, 36, 92)
ORANGE_BROWN = (161, 105, 59)
WHITE = (255, 255, 255)
LIGHT_GRAY = (150, 150, 150)
DARK_GRAY = (40, 40, 40)
BLACK = (0, 0, 0)




#  la configuration du Board

board_width = WIDTH - 20
board_height = HEIGHT - 150
board_color = DARK_GRAY
board_x = 80
board_y = 100


#  la configuration de la fosse

fosse_width = 55
fosse_color = BROWN
fosse_spacing = 65

#  la configuration du magasin

magasin_width = 80
magasin_height = HEIGHT - 400
magasin_color = ORANGE_BROWN
magasin1_x = 100
magasin1_y = 220
magasin2_x = WIDTH - 60
magasin2_y = 220

# Les variables de graine notamment , la largeur de la graine et ainsi les couleurs des granes
graine_width = 10
graine_color = [(255, 218, 10), (219, 35, 60), (55, 255, 0), ( 0, 106, 255)]


class Drawer:
    def __init__(self):
        # creation de la fentre
        # Screen = Screen/
        self.PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # mettre un background JPG dans la fenetre
        Screen.fill("black")
        # Donner un titre de fentr
        # intialisation du board 
        self.board = dict()
        # self.PLAY_BACK = Button(image=None, pos=(640, 680),
        #                     text_input="BACK", font= font, base_color="White", hovering_color="Green")
        #
        # self.PLAY_BACK.changeColor(self.PLAY_MOUSE_POS)
        # self.PLAY_BACK.update(Screen)
        # Dessiner le Board , les 12 fosses et les deux magasin dans la fenetre
        self.drawBoard()
        self.drawFosses()
        self.drawMagasin1()
        self.drawMagasin2()
        # mettre les graines dans les fosses
        for cle, valeur in self.board.items():
            self.drawGraine(valeur)
            self.drawGraine(valeur)
            self.drawGraine(valeur)
            self.drawGraine(valeur)
            '''if (cle in ["A", "B", "C", "D", "E", "F"]):
                self.PitValue(valeur, 4, -100)
            else:
                self.PitValue(valeur, 4, 100)'''
        # intialisation de score pour les deu joueurs
        self.PlayerScore(1, 0)
        self.PlayerScore(2, 0)
        # donner la main au premier joueur
        self.DisplayTurn(1)
        # chaque magasin ne contient aucune graine
        self.Magasin1 = 0
        self.Magasin2 = 0
        self.change = {"A": 4, "B": 4, "C": 4, "D": 4, "E": 4, "F": 4,
                       "G": 4, "H": 4, "I": 4, "J": 4, "K": 4, "L": 4}
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.PLAY_BACK.checkForInput(self.PLAY_MOUSE_POS):
                    self.main_menu()

        pygame.display.update()
    # la fonction pour dessiner le Board
    def drawBoard(self):
        pygame.draw.rect(Screen, board_color, (board_x, board_y,
                         board_width, board_height), width=0, border_radius=15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
        
    # la fonction pour dessiner le magasin du 1er joueur
    def drawMagasin1(self):
        pygame.draw.rect(Screen, magasin_color, (magasin1_x, magasin1_y,
                         magasin_width, magasin_height), width=0, border_radius=50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    # la fonction pour dessiner le magasin du 2eme joueur
    def drawMagasin2(self):
        pygame.draw.rect(Screen, magasin_color, (magasin2_x, magasin2_y,
                         magasin_width, magasin_height), width=0, border_radius=50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    # la fonction pour dessiner les fosses pour les deux joueurs 
    def drawFosses(self):
        
        mBoard = MancalaBoard()
        # recupere le nombre de fosse de chacun des deux joueurs
        fosse_1 = mBoard.player_1_pits
        fosse_2 = mBoard.player_2_pits
        fosse_y = HEIGHT - 200
        
        # placer les fosses du premier dans le board
        for i in range(len(fosse_1)):
            fosse_x = 300 + (i * (fosse_width + fosse_spacing))
            pygame.draw.circle(Screen, fosse_color,(fosse_x, fosse_y), fosse_width)
            self.board[fosse_1[i]] = (fosse_x, fosse_y)
        
        fosse_y = 300
        # placer les fosses du premier dans le board
        for i in range(len(fosse_2)):
            fosse_x = 300 + (i * (fosse_width + fosse_spacing))
            pygame.draw.circle(Screen, fosse_color,(fosse_x, fosse_y), fosse_width)
            self.board[fosse_2[i]] = (fosse_x, fosse_y)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
        
    # la fonction pour dessiner la premiere fosse qui correspond au 1er joueur
    def drawFosseP1(self, i):
        fosse_y = HEIGHT-200
        fosse_x = 300 + (i * (fosse_width + fosse_spacing))
        pygame.draw.circle(Screen, fosse_color,(fosse_x, fosse_y), fosse_width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
        
    # la fonction pour dessiner la premiere fosse qui correspond au 2eme joueur
    def drawFosseP2(self, i):
        fosse_y = 300
        fosse_x = 300 + (i * (fosse_width + fosse_spacing))
        pygame.draw.circle(Screen, fosse_color,(fosse_x, fosse_y), fosse_width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    # la fonction pour dessiner les graines dans les fosses
    def drawGraine(self, cor):
        x, y = cor
        x = x+random.randint(-29, 29)
        y = y+random.randint(-29, 29)
        pygame.draw.circle(Screen, random.choice(graine_color),(x, y), graine_width)
        pygame.draw.circle(Screen, BLACK,(x, y), graine_width, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    
        
        
    # la fonction qui met a jour les fosses lorsque l'un des joueurs fait son move
    def updateFosses(self, lettre):
        pygame.draw.circle(Screen, fosse_color,self.board[lettre], fosse_width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


    # la fonction qui affiche les score pour les deux joueurs
    def PlayerScore(self, Player, value):
        if (Player == 1):
            text = font.render(f"YOUR SCORE : {value}", True, (84, 180, 53), board_color)
            textRect = text.get_rect()
            textRect.center = WIDTH  - 60,190
        else:
            text = font.render(f"COMPUTER SCORE : {value}", True, (84, 180, 53), board_color)
            textRect = text.get_rect()
            textRect.center = 220, 190
            
        Screen.blit(text, textRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


    # la fonction qui donne la main au joueurs
    def DisplayTurn(self, Player):
        font = pygame.font.Font('./assets/abg.ttf', 20)
        if (Player == 2):
            text = font.render(f"COMPUTER TURN ", True,
                               WHITE, BLUE_A)
        else:
            text = font.render(f"   YOUR  TURN   ", True,
                               WHITE, BLUE_A)
        textRect = text.get_rect()
        textRect.center = WIDTH/2 +100, 180
        Screen.blit(text, textRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
    # la fonction pour dessiner les graines dans le magasin
    def drawGraineMagasin(self, value, player):
        if (player == 2):
            x, y = magasin1_x, magasin1_y
            n = value-self.Magasin1
            self.Magasin1 = value
        else:
            x, y = magasin2_x, magasin2_y
            n = value-self.Magasin2
            self.Magasin2 = value
        x = x+random.randint(22, magasin_width-22)
        y = y+random.randint(22, magasin_height-22)
        for i in range(n):
            pygame.draw.circle(Screen, random.choice(graine_color),
                               (x, y), graine_width)
            pygame.draw.circle(Screen, BLACK,
                               (x, y), graine_width, 1)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    # la fonction qui met a jour le nombre de graine dans ' les fosses et le magasin ' et le score des deux joueurs
    def Update1(self, board, player=1):
        liste = ["A", "B", "C", "D", "E", "F"]
        for i in liste:
            if (self.change[i] != board[i]):
                add = -100
                self.drawFosseP1(liste.index(i))
                for j in range(board[i]):
                    self.drawGraine(self.board[i])
                #self.PitValue(self.board[i], board[i], add)
                time.sleep(0.5)
            self.change[i] = board[i]
        self.PlayerScore(player, board[player])
        self.drawGraineMagasin(board[player], player)
        time.sleep(0.5)
        liste = ["L", "K", "J", "I", "H", "G"]
        l = ["G", "H", "I", "J", "K", "L"]
        for i in liste:
            if (self.change[i] != board[i]):
                add = 100
                self.drawFosseP2(l.index(i))
                for j in range(board[i]):
                    self.drawGraine(self.board[i])
                #self.PitValue(self.board[i], board[i], add)
                time.sleep(0.8)
            self.change[i] = board[i]
        time.sleep(0.5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def Update2(self, board, player=2):
        liste = ["L", "K", "J", "I", "H", "G"]
        l = ["G", "H", "I", "J", "K", "L"]
        for i in liste:
            if (self.change[i] != board[i]):
                add = 100
                self.drawFosseP2(l.index(i))
                for j in range(board[i]):
                    self.drawGraine(self.board[i])
                #self.PitValue(self.board[i], board[i], add)
                time.sleep(0.8)
            self.change[i] = board[i]
        self.PlayerScore(player, board[player])
        self.drawGraineMagasin(board[player], player)
        time.sleep(0.5)
        liste = ["A", "B", "C", "D", "E", "F"]
        for i in liste:
            if (self.change[i] != board[i]):
                add = -100
                self.drawFosseP1(liste.index(i))
                for j in range(board[i]):
                    self.drawGraine(self.board[i])
                #self.PitValue(self.board[i], board[i], add)
                time.sleep(0.8)
            self.change[i] = board[i]
        time.sleep(0.5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


    # Affichage du vainqeur
    def DisplayTheWinner(self, player, score):
        self.drawBoard()
        font = pygame.font.Font('abg.ttf', 40)
        if (player == 1):
            text = font.render(f"YOU WIN", True, WHITE, board_color)
        else:
            text = font.render(f"YOU LOST ", True, WHITE, board_color)

        text2 = font.render(f"Score:{score}", True, WHITE, board_color)
        textRect = text.get_rect()
        textRect.center = WIDTH/2, (HEIGHT/2-60)
        Screen.blit(text, textRect)
        textRect = text2.get_rect()
        textRect.center = WIDTH/2, (HEIGHT/2+60)
        Screen.blit(text2, textRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def DisplayPossibleMoves(self, liste):
        for i in liste:

            l = ["A", "B", "C", "D", "E", "F"]
            fosse_y = HEIGHT-200
            fosse_x = 300 + (l.index(i) * (fosse_width + fosse_spacing))

            pygame.draw.circle(Screen, LIGHT_GREEN,
                               (fosse_x, fosse_y), fosse_width, 5)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def RemovePossibleMoves(self, liste):
        for i in liste:

            l = ["A", "B", "C", "D", "E", "F"]
            fosse_y = HEIGHT-200
            fosse_x = 300 + (l.index(i) * (fosse_width + fosse_spacing))

            pygame.draw.circle(Screen, LIGHT_GRAY,
                               (fosse_x, fosse_y), fosse_width, 2)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
       
    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/abg.ttf", size)
    
    def start_game():
        draw = Drawer()
        running = True
        test = Play()
        game = Game(1)
        player = 1

        while (not game.gameOver() and running == True):

            
            pygame.display.update()
            if (player == 1):
                draw.DisplayPossibleMoves(game.state.possibleMoves(1))
                player = test.humanTurn(game)
                draw.RemovePossibleMoves(game.state.possibleMoves(1))
                draw.Update1(game.state.board)
                draw.DisplayTurn(player)
                pygame.display.update()
            else:
                player, game = test.computerTurn(game, test)
                time.sleep(1)
                draw.Update2(game.state.board)
                draw.DisplayTurn(player)
                pygame.display.update()
            
        player, score = game.findWinner()
        draw.DisplayTheWinner(player, score)
        time.sleep(15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if draw.PLAY_BACK.checkForInput(draw.PLAY_MOUSE_POS):
                    draw.main_menu()

        pygame.display.update()
 
    def main_menu(self):
        while True:
            Screen.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("Mancala", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                                text_input="Start", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")
            # OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                                # text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                                text_input="QUIT", font=self.get_font(50), base_color="#d7fcd4", hovering_color="White")

            Screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(Screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.start_game()
                    # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #     options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


