from Styles.Default import Style

from Actions import ACTIONS


class Copy(Style):
    """
        It will play the same action that the other player played last turn
    """

    def __init__(self, player) -> None:
        super().__init__(player)

    def getAction(self):
        # Copy playstyle always start with Cooperate
        if self.player.game.currentRound == 1:
            return ACTIONS.COOPERATE

        # -2 is because the round starts at 1 and not 0, and we want the round before the currentRound
        lastRound = self.player.game.history[self.player.game.currentRound - 2] 

        # index == 0 or 1, doing a "not 0" will return True and doing a "not 1" will return False
        # In python we can convert Bool to Int (False == 0 and True == 1)
        # So, "not 0" == True, "int(True)" == 1, that's how we get the other player index
        otherPlayerIndex = int(not self.player.index)

        otherPlayerAction = lastRound[otherPlayerIndex]["action"]

        return ACTIONS.COOPERATE if otherPlayerAction == ACTIONS.COOPERATE else ACTIONS.BETRAY

    def __str__(self) -> str:
        return "Copieur"
