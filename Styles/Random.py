from Styles.Default import Style


class Random(Style):
    def __init__(self, player) -> None:
        super().__init__(player, 0.5)

    def __str__(self) -> str:
        return "Aléatoire"
