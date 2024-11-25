from player import Player
from scoring import OperationFactory



class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        
        if player_name == self.player1.name:
            self.player1.scores+=1
        elif player_name == self.player2.name:
            self.player2.scores+=1


    def get_score(self):
    
        return OperationFactory.create(self.player1.scores, self.player2.scores).calculate()
