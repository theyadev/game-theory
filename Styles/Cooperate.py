from Styles.Default import Style


class Cooperate(Style):
    def __init__(self, player) -> None:
        super().__init__(player, 1)

    def __str__(self) -> str:
        return "Cooperatif"
