from Player import Player
from Actions import ACTIONS


class Game:
    def __init__(self, firstPlayerStyle, secondPlayerStyle) -> None:
        self.players = (
            Player(0, self, firstPlayerStyle),
            Player(1, self, secondPlayerStyle)
        )

        self.rounds = 5
        self.currentRound = 1
        self.history = []

    def step(self):
        self.players[0].action = self.players[0].style.getAction()
        self.players[1].action = self.players[1].style.getAction()

        if self.players[0].action == ACTIONS.COOPERATE and self.players[1].action == ACTIONS.COOPERATE:
            self.players[0].score += 3
            self.players[1].score += 3

        elif self.players[0].action == ACTIONS.BETRAY and self.players[1].action == ACTIONS.BETRAY:
            self.players[0].score += 1
            self.players[1].score += 1

        else:
            self.players[0].score += 5 if self.players[0].action == ACTIONS.BETRAY else 0
            self.players[1].score += 5 if self.players[1].action == ACTIONS.BETRAY else 0

        self.history.append(
            [{"score": player.score, "action": player.action} for player in self.players])

        self.currentRound += 1

    def playEveryRound(self):
        while self.currentRound - 1 < self.rounds:
            self.step()

        return self
