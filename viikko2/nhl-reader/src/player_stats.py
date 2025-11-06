# pylint: disable=too-few-public-methods
class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered = [p for p in self.players if p.nationality == nationality]
        filtered.sort(key=lambda p: p.points, reverse=True)
        return filtered
