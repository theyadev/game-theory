from Styles.Default import Style

from Actions import ACTIONS


class Copy(Style):
    def __init__(self, player) -> None:
        super().__init__(player)

    def getAction(self):
        if self.player.game.currentRound == 1:
            return ACTIONS.COOPERATE

        lastRound = self.player.game.history[self.player.game.currentRound - 2]

        otherPlayerAction = lastRound[int(not self.player.index)]["action"]

        return ACTIONS.COOPERATE if otherPlayerAction == ACTIONS.COOPERATE else ACTIONS.BETRAY

    def __str__(self) -> str:
        return "Copieur"
