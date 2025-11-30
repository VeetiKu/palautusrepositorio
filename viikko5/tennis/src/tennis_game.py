class TennisGame:
    SCORE_TERMS = ["Love", "Fifteen", "Thirty", "Forty"]
    ADVANTAGE_THRESHOLD = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.is_tied():
            return self.score_for_tied_game()

        if self.is_endgame():
            return self.score_for_endgame()

        return self.score_for_standard_game()

    def is_tied(self):
        return self.player1_score == self.player2_score

    def is_endgame(self):
        return (
            self.player1_score >= self.ADVANTAGE_THRESHOLD
            or self.player2_score >= self.ADVANTAGE_THRESHOLD
        )

    def score_for_tied_game(self):
        if self.player1_score < 3:
            return f"{self.SCORE_TERMS[self.player1_score]}-All"
        return "Deuce"

    def score_for_endgame(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        if score_difference == -1:
            return f"Advantage {self.player2_name}"
        if score_difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def score_for_standard_game(self):
        player1_term = self.SCORE_TERMS[self.player1_score]
        player2_term = self.SCORE_TERMS[self.player2_score]
        return f"{player1_term}-{player2_term}"
