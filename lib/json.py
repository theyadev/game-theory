import json


def readPlaystyles(path: str):
    """
        Read the json containing all basic playstyles
    """

    customStyles = None

    try:
        with open(path, "r") as f:
            customStyles = json.load(f)
    except FileNotFoundError:
        pass

    return customStyles
