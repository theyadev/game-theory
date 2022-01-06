class Player:
    """
        Player class

        Keyword arguments:\n
        index -- 0 or 1\n
        game -- takes a Game, the Game instance where the Player is playing\n
        style -- takes a Style, the playstyle of the Player
    """

    def __init__(self, index, game, style) -> None:
        self.index = index
        self.score = 0
        self.style = style(self)
        self.game = game
        self.action = None

    def __str__(self) -> str:
        return f"{self.action}: {self.score} points !"
