import math
from copy import deepcopy
import pygame


def getPitFromPos(pos):
    pit_index = None
   
    if (335 - 55 <= pos[0] <= 335+55) and (500-55 <= pos[1] <= 500+55):
        pit_index = "A"
    elif (460 - 55 <= pos[0] <= 460 + 55) and (500-55 <= pos[1] <= 500+55):
        pit_index = "B"
    elif (585 - 55 <= pos[0] <= 585 + 55) and (500-55 <= pos[1] <= 500+55):
        pit_index = "C"
    elif (710 - 55 <= pos[0] <= 710 + 55) and (500-55 <= pos[1] <= 500+55):
        pit_index = "D"
    elif (835 - 55 <= pos[0] <= 835 + 55) and (500-55 <= pos[1] <= 500+55):
        pit_index = "E"
    elif (960 - 55 <= pos[0] <= 960 + 55) and (500-55 <= pos[1] <= 500+55):
        pit_index = "F"
    return pit_index


class Play:

    def humanTurn(self, game):
        
        move_made = False
        
        
        while not move_made:
           
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    
                    pos = pygame.mouse.get_pos()
                    pit = getPitFromPos(pos)
                    
                    if pit in game.state.possibleMoves(1):
                        curent_player = game.state.doMove(1, pit)
                        move_made = True
                        break
            
            pygame.time.delay(50)
            
        
        return curent_player


    def computerTurn(self, game, play, depth = 8):
        
        if len(game.state.possibleMoves(2)) > 0:
           
            
            player_1_four = all(game.state.board[x] == 4 for x in game.state.player_1_pits)
            player_2_four = all(game.state.board[x] == 4 for x in game.state.player_2_pits)
            
            if player_1_four and player_2_four:
              curent_player = game.state.doMove(2, 'J')
            
            else:  
              best_node = play.minmaxAlphaBetaPruning( game, 2, depth, -math.inf, math.inf)
              
              curent_player = game.state.doMove(2, best_node[1])
            
       
        return curent_player, game

    def minmaxAlphaBetaPruning(self, game, player, depth, alpha, beta):
        # Si la profondeur de recherche atteint zéro ou si le jeu est terminé, 
        # retourner la valeur d'évaluation du jeu et aucun mouvement (None)
        if depth == 0 or game.gameOver():
            return game.evaluate2(), None

        # Si c'est au tour du joueur 1 de jouer
        if player == 1:
            # Initialiser la meilleure valeur et le meilleur mouvement
            best_value = -math.inf
            best_move = None
            
            # Pour chaque mouvement possible
            for move in game.state.possibleMoves(player):
                # Créer une copie profonde du jeu
                new_game = deepcopy(game)
                # Jouer le coup sur la copie du jeu
                new_game.state.doMove(player, move)
                
                # Utiliser récursivement l'algorithme Minimax avec élagage alpha-beta
                # pour trouver la valeur du meilleur coup
                value, _ = self.minmaxAlphaBetaPruning(new_game, 2, depth - 1, alpha, beta)
                
                # Si la valeur du coup est supérieure à la meilleure valeur actuelle, 
                # mettre à jour la meilleure valeur et le meilleur mouvement
                if value > best_value:
                    best_value = value
                    best_move = move
                    
                # Mettre à jour alpha en prenant la valeur maximale entre alpha et la meilleure valeur actuelle
                alpha = max(alpha, best_value)
                
                # Si alpha est supérieur ou égal à beta, interrompre l'exécution de la boucle grâce à l'élagage alpha-beta
                if alpha >= beta:
                    break
                  
            # Retourner la meilleure valeur et le meilleur mouvement
            return best_value, best_move
        else:
            # Initialiser la meilleure valeur et le meilleur mouvement
            best_value = math.inf
            best_move = None
            
            # Pour chaque mouvement possible
            for move in game.state.possibleMoves(player):
              # Créer une copie profonde du jeu
                new_game = deepcopy(game)
                # Jouer le coup sur la copie du jeu
                new_game.state.doMove(player, move)
                
                # Utiliser récursivement l'algorithme Minimax avec élagage alpha-beta
                # pour trouver la valeur du meilleur coup
                value, _ = self.minmaxAlphaBetaPruning(new_game, 1, depth - 1, alpha, beta)
                
                # Si la valeur du coup est inférieure à la meilleure valeur actuelle, 
                # mettre à jour la meilleure valeur et le meilleur mouvement
                if value < best_value:
                    best_value = value
                    best_move = move
                
                # Mettre à jour beta en prenant la valeur minimale entre beta et la meilleure valeur actuelle
                beta = min(beta, best_value)
                
                # Si alpha est supérieur ou égal à beta, interrompre l'exécution de la boucle grâce à l'élagage alpha-beta
                if alpha >= beta:
                    break
            
            # Retourner la meilleure valeur et le meilleur mouvement
            return best_value, best_move