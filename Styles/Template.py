"""
    Use this template to create complex playstyles.

    What do you need to do:
        - Rename the name of the class and the name in the __str__
        - Add a little description
        - Create your playstyle in getAction method and return an action (ACTIONS.COOPERATE or ACTIONS.BETRAY)
        - Remove every comments unless the description
        - Import the playstyle in __init__.py
    
    What do you have access to:
        - actions done by the other player = getOtherPlayerActions(self.player)

        - current player = self.player
            - index = self.player.index
            - score = self.player.score

        - current game = self.player.game
            - players list = self.player.game.players
            - max rounds = self.player.game.rounds
            - current round = self.player.game.currentRound
            - history of rounds = self.player.game.history
"""

from typing import Literal
from Styles.Default import Style

from Classes.Actions import ACTIONS

# Import this only if you need the other player actions
# from utils.getOtherPlayerActions import getOtherPlayerActions

# Change the name of the class


class Name(Style):
    """
        Please describe what the playstyle do
    """

    def __init__(self, player):
        super().__init__(player)

    def getAction(self) -> Literal:
        pass

        # You must return ACTIONS.COOPERATE or ACTIONS.BETRAY

    def __str__(self) -> str:
        # Change the name of the class
        return "Name"
