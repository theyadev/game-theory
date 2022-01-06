from random import random

from Classes.Actions import ACTIONS


class Style:
    """
        The base for every playstyle\n

        keywords arguments:\n
        player -- a Player instance\n
        c -- Probability of choosing the action Cooperate (default: None)
    """

    def __init__(self, player, c: float = None) -> None:
        self.player = player
        self.cooperate = c

    def getAction(self):
        return ACTIONS.COOPERATE if random() < self.cooperate else ACTIONS.BETRAY
