from Styles.Default import Style
from Actions import ACTIONS


class UserInput(Style):
    def __init__(self, player, c: float = None) -> None:
        super().__init__(player)

    def getAction(self):
        userInput = input("\n\n1: Cooperer, 2: Trahir | ")
        return ACTIONS.COOPERATE if userInput == "1" else ACTIONS.BETRAY

    def __str__(self) -> str:
        return "Joueur"
