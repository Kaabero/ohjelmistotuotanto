class PlayerStats:
    def __init__(self, reader):
        self.players=reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):

        players=[]

        for player in self.players:
            if player.nationality==nationality:
                players.append(player)
        
        
        return sorted(players, key=lambda player: player.get_points(), reverse=True)


        
        
    
