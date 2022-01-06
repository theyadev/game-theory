from Styles.Default import Style

from Classes.Actions import ACTIONS


class UserInput(Style):
    """
        It will ask for user input to play
    """

    def __init__(self, player) -> None:
        super().__init__(player)

    def getAction(self):
        # TODO: Make it better, error handling, etc...

        userInput = input(
            f"\n\n1: {ACTIONS.COOPERATE}, 2: {ACTIONS.BETRAY} | ")
        return ACTIONS.COOPERATE if userInput == "1" else ACTIONS.BETRAY

    def __str__(self) -> str:
        return "Joueur"
