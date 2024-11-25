class OperationFactory:
    @staticmethod
    def create(scores1, scores2,):
        if scores1 == scores2:
            return SameScores(scores1)
        elif scores1 >= 4 or scores2 >= 4:
            return WinOrAdvantage(scores1 - scores2)

        return OngoingScores(scores1, scores2)



class OngoingScores:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, score1, score2):
        self.score1 = score1
        self.score2 = score2

    def calculate(self):
        return f"{self.SCORE_NAMES[self.score1]}-{self.SCORE_NAMES[self.score2]}"

class SameScores():

    def __init__(self, scores):
        self.scores=scores

    def calculate(self):
        if self.scores == 0:
            return "Love-All"
        elif self.scores == 1:
            return "Fifteen-All"
        elif self.scores == 2:
            return "Thirty-All"
        else:
            return "Deuce"
        
class WinOrAdvantage():

    def __init__(self, difference):
        self.difference = difference
    
    def calculate(self):
        if self.difference == 1:
            return "Advantage player1"
        elif self.difference == -1:
            return "Advantage player2"
        elif self.difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
