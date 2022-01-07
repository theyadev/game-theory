def getOtherPlayerActions(player):
    """
        Create a list of actions done by the other player
    """

    # index == 0 or 1, doing a "not 0" will return True and doing a "not 1" will return False
    # In python we can convert Bool to Int (False == 0 and True == 1)
    # So, "not 0" == True, "int(True)" == 1, that's how we get the other player index
    otherPlayerIndex = int(not player.index)

    otherPlayerActions = [round[otherPlayerIndex]["action"]
                          for round in player.game.history]

    return otherPlayerActions
