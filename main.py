from Styles import playstyles

from Classes.Game import Game
from plot import showGraph


def main():
    availablePlaystyles = [name for name in playstyles.keys()]

    print(f"List of playstyles: {', '.join(availablePlaystyles)}")

    firstPlaystyle = input("Please choose the first playstyle: ")
    if not firstPlaystyle in availablePlaystyles:
        return print("Not a valid playstyle !!!")

    secondPlaystyle = input("Please choose the second playstyle: ")
    if not secondPlaystyle in availablePlaystyles:
        return print("Not a valid playstyle !!!")

    newGame = Game(playstyles[firstPlaystyle], playstyles[secondPlaystyle]).playEveryRound()

    showGraph(newGame)


if __name__ == "__main__":
    main()
