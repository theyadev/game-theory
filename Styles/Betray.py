from Styles.Default import Style


class Betray(Style):
    """
        It will always betray the other player
    """

    def __init__(self, player) -> None:
        super().__init__(player, 0)

    def __str__(self) -> str:
        return "Traitre"
