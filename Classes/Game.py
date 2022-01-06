from Classes.Player import Player
from Classes.Actions import ACTIONS

from settings import ROUNDS, Points


class Game:
    """
        Game class, used to run simulation between 2 players.

        Keyword arguments:\n
        firstPlayerStyle -- takes a Style, define the playstyle of the first player\n
        secondPlayerStyle -- takes a Style, define the playstyle of the second player
    """

    def __init__(self, firstPlayerStyle, secondPlayerStyle) -> None:
        self.players = (
            Player(0, self, firstPlayerStyle),
            Player(1, self, secondPlayerStyle)
        )

        self.rounds = ROUNDS
        self.currentRound = 1
        self.history = []

    def step(self):
        """
            Step one round into the simulation.\n

            returns None if max round reached
        """

        if self.currentRound - 1 > self.rounds:
            return None

        self.players[0].action = self.players[0].style.getAction()
        self.players[1].action = self.players[1].style.getAction()

        # TODO: Getting things done DRYer

        if self.players[0].action == ACTIONS.COOPERATE and self.players[1].action == ACTIONS.COOPERATE:
            self.players[0].score += Points.BOTH_COOPERATE
            self.players[1].score += Points.BOTH_COOPERATE

        elif self.players[0].action == ACTIONS.BETRAY and self.players[1].action == ACTIONS.BETRAY:
            self.players[0].score += Points.BOTH_BETRAY
            self.players[1].score += Points.BOTH_BETRAY

        else:
            self.players[0].score += Points.BETRAY_WHEN_COOPERATED if self.players[0].action == ACTIONS.BETRAY else Points.COOPERATE_WHEN_BETRAYED
            self.players[1].score += Points.BETRAY_WHEN_COOPERATED if self.players[1].action == ACTIONS.BETRAY else Points.COOPERATE_WHEN_BETRAYED

        self.history.append(
            [{"score": player.score, "action": player.action} for player in self.players])

        self.currentRound += 1

    def playEveryRound(self):
        """
            Runs step function until max round reached.
        """

        while self.currentRound - 1 < self.rounds:
            self.step()

        return self
