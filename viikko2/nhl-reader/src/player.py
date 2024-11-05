class Player:
    def __init__(self, name, team, goals, assists, nationality, games):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality
        self.games = games
    
    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"
