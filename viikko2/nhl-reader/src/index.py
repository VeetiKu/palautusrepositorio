from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats


console = Console()

def main():
    console.print("[bold underline]NHL Pelaajatilastot[/bold underline]\n")
    season = Prompt.ask("Anna kausi (esim. 2023-24 tai 2024-25)", default="2024-25")
    nationality = Prompt.ask("Anna maan lyhenne (esim. FIN, SWE, CAN, USA)", default="FIN")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    if not players:
        console.print(f"[red]Ei löytynyt pelaajia maalle {nationality} kaudelta {season}.[/red]")
        return

    table = Table(title=f"Pelaajat maasta {nationality} ({season})")

    table.add_column("Nimi", style="cyan", no_wrap=True)
    table.add_column("Joukkue", style="magenta")
    table.add_column("Maa", style="green")
    table.add_column("Maalit", justify="right", style="yellow")
    table.add_column("Syötöt", justify="right", style="bright_blue")
    table.add_column("Pisteet", justify="right", style="bold white")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            player.nationality,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    console.print()
    console.print(table)

if __name__ == "__main__":
    main()
