class MancalaBoard:
    def __init__(self):
        
        self.board = {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4,
                     'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 4, 'L': 4,
                      1: 0, 2: 0}
        
        
        self.player_1_pits = ('A', 'B', 'C', 'D', 'E', 'F')
        
        
        self.player_2_pits = ('G', 'H', 'I', 'J', 'K', 'L')
        
        
        self.opposite_pit = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                         'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F'}
        

        self.next_pit = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 1,
                     1: 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G', 'G': 2, 2: 'A'}

    def possibleMoves(self, player):

        if player == 1:
            return [pit for pit in self.player_1_pits if self.board[pit] > 0]
        
        
        else:
            return [pit for pit in self.player_2_pits if self.board[pit] > 0]

    def doMove(self, player, pit):
        
        seeds = self.board[pit]
        self.board[pit] = 0
        
        
        while seeds > 0:
            pit = self.next_pit[pit]
            self.board[pit] += 1
            seeds = seeds-1
            
        
        if (pit == player):
            return player
          
        
        if (player == 1):
            player_fosses = self.player_1_pits
        else:
            player_fosses = self.player_2_pits
        
        if (self.board[pit] == 1 and pit in player_fosses):
            self.board[pit] = 0
            opposite = self.opposite_pit[pit]
            self.board[player] += (self.board[opposite]+1)
            self.board[opposite] = 0

        
        if (player == 1):
            return 2
        else:
            return 1