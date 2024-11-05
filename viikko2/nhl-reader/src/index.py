import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists'], player_dict['nationality'], player_dict['games']  )
        players.append(player)

    print("Players from FIN:")

    finnish_players = sorted(list(filter(lambda player: player.nationality == 'FIN', players)), key=lambda player: player.get_points(), reverse=True)


    for player in finnish_players:
            print(player)

if __name__ == "__main__":
    main()
