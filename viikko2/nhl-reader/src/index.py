import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = [Player(player_dict)for player_dict in response]
    players_FIN = [p for p in players if p.nationality == "FIN"]


    print("\nPlayers from FIN:\n")

    for player in players_FIN:
        print(player)
        
if __name__ == "__main__":
    main()