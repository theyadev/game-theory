from Styles.Default import Style

from Classes.Actions import ACTIONS

from lib.getOtherPlayerActions import getOtherPlayerActions


class Playstyle(Style):
    """
        It will play the same action that the other player played last turn
    """

    def __init__(self, player) -> None:
        super().__init__(player)

    def getAction(self):
        otherPlayerActions = getOtherPlayerActions(self.player)

        if len(otherPlayerActions) == 0:
            return ACTIONS.COOPERATE

        return ACTIONS.COOPERATE if otherPlayerActions[-1] == ACTIONS.COOPERATE else ACTIONS.BETRAY

    def __str__(self) -> str:
        return "Copieur"
