import json


def readCustomPlaystyles():
    """
        Read the json containing all basic playstyles
    """

    customStyles = None

    try:
        with open("./playstyles.json", "r") as f:
            customStyles = json.load(f)
    except FileNotFoundError:
        pass

    return customStyles
