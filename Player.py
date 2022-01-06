class Player:
    def __init__(self, index, game, style) -> None:
        self.index = index
        self.score = 0
        self.style = style(self)
        self.game = game
        self.action = None

    def __str__(self) -> str:
        return f"{self.score} points, {self.action}"
