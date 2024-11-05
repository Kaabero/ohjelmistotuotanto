class Player:
    def __init__(self, name, team, goals, assists, nationality, games):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.games = games
    
    def get_points(self):
        return self.goals+self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals:5} + {self.assists:2} = {self.get_points()}"
