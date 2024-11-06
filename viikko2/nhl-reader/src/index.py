from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print # type: ignore
from rich.table import Table # type: ignore
from rich.console import Console # type: ignore
import sys

console = Console()


def main():
    print('')
    console.print('[bold blue]NHL statistics by nationality[/bold blue]\n')

    
    while True:
        season=console.input('Select season [purple][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25]:[/purple]')
        if season=='':
            sys.exit()
        if season not in ['2018-19', '2019-20','2020-21', '2021-22', '2022-23', '2023-24', '2024-25']:
            console.print("[red]Invalid season. Please select from the available options or press Enter to stop.[/red]")
            continue
        if season in ['2018-19', '2019-20','2020-21', '2021-22', '2022-23', '2023-24', '2024-25']:
            break
        
        

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)


    while True:
        print('')
        nationality=console.input('Select nationality\n[bold purple][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR]:[/bold purple]')
        if nationality=='':
            sys.exit()
        if nationality not in ['AUT','CZE','AUS','SWE','GER','DEN','SUI','SVK','NOR','RUS','CAN','LAT','BLR','SLO','USA','FIN','GBR']:
            console.print("[red]Invalid nationality. Please select from the available options or press Enter to stop.[/red]")
            continue
        
        
        players = stats.top_scorers_by_nationality(nationality)
        print('')
        table = Table(title=f"Top scores of {nationality} season {season}")

        table.add_column("Name", style="cyan", justify="left")
        table.add_column("Team", style="magenta", justify="center")
        table.add_column("Goals", style="green", justify="center")
        table.add_column("Assists", style="green", justify="center")
        table.add_column("Points", style="bold green", justify="center")

        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.get_points())
            )

        console.print(table)


if __name__ == "__main__":
    main()
