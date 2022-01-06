from random import random

from Actions import ACTIONS


class Style:
    def __init__(self, player,  c: float = None) -> None:
        self.player = player
        self.cooperate = c

    def getAction(self):
        return ACTIONS.COOPERATE if random() < self.cooperate else ACTIONS.BETRAY