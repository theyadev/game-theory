from Styles.Default import Style


class Betray(Style):
    def __init__(self, player) -> None:
        super().__init__(player, 0)

    def __str__(self) -> str:
        return "Traitre"
