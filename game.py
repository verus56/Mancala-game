from mancalaBoard import MancalaBoard

class Game:
    def __init__(self, player):  
        self.state = MancalaBoard()
        self.playerSide = player


    def gameOver(self):  
        
        player_1_empty = all(self.state.board[x] == 0 for x in self.state.player_1_pits)
        player_2_empty = all(self.state.board[x] == 0 for x in self.state.player_2_pits)
        
        if player_1_empty:
            for x in self.state.player_2_pits:
                self.state.board[1] += self.state.board[x]
            return True
        
        
        elif player_2_empty:
            for x in self.state.player_1_pits:
                self.state.board[2] += self.state.board[x]
            return True
        
        
        return False

    def findWinner(self):
       
        score_player_1 = self.state.board[1]
        score_player_2 = self.state.board[2]
        
        
        if score_player_1 > score_player_2:
            return 1, score_player_1
        else:
            return 2, score_player_2

    def evaluate(self):
        return self.state.board[1] - self.state.board[2]

    def evaluate2(self):
        H1 = self.hoard_leftmost_pit()
        H2 = self.hoard_player_side()
        H3 = self.have_many_moves()
        H4 = self.proximity_to_winning()
        H5 = self.proximity_to_winning_2()

        return  0.2*H5 + 0.2*H4 + 0.2*H3 + 0.2*H2 + 0.2*H1

        


    #les heuristiques 
    #verifier gauche
    def hoard_leftmost_pit(self):
        leftmost_pit = self.state.board['G']
        return leftmost_pit
    
    #compter la somme total des gaines
    def hoard_player_side(self):
        sum_seeds = 0
        for x in self.state.player_1_pits:
            sum_seeds += self.state.board[x]
        return sum_seeds
    
    #le nombre des moves
    def have_many_moves(self):
        possible_moves = self.state.possibleMoves(2)
        return len(possible_moves)

    # how close the player to winning
    def proximity_to_winning(self):
        current_seeds = self.state.board[2]
        opponent_seeds = self.state.board[1]
        if current_seeds >= 1.5 * opponent_seeds and opponent_seeds > 5:
            return 1
        else:
            return 0
        
    #evaluate de madame
    def proximity_to_winning_2(self):
        return self.state.board[1] - self.state.board[2]