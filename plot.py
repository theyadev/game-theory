import numpy as np
import matplotlib.pyplot as plt
import matplotlib


import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from Actions import ACTIONS


def showGraph(game):
    rounds = np.arange(len(game.history))+1

    scores = [[round[i]['score'] for round in game.history] for i in range(2)]
    classes = [[1*(round[i]['action'] == ACTIONS.COOPERATE)
                for round in game.history] for i in range(2)]

    playerColors = ["orange", "blue"]
    dotColors = ['red', 'green']

    fig, axs = plt.subplots(2)
    fig.set_size_inches(10.5, 7)
    fig.suptitle('Theorie des jeux.')

    for i, ax in enumerate(axs):
        ax.plot(rounds, scores[i], color=playerColors[i])
        ax.scatter(rounds, scores[i], c=classes[i],
                   cmap=matplotlib.colors.ListedColormap(dotColors))

        ax.set(ylabel="Points")
        ax.grid()
        ax.legend()
        ax.set_ylim([0, np.max(scores)+5])
        ax.set_xticks(rounds)

        ax.set_title(game.players[i].style)

    plt.show()
