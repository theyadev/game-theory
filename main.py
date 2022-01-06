import Styles

from Classes.Game import Game
from plot import showGraph

if __name__ == "__main__":
    newGame = Game(Styles.Test, Styles.Betray).playEveryRound()

    showGraph(newGame)
