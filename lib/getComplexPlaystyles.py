import os
import importlib


def getComplexPlaystyles(pathToDirectory: str):
    """
        Create an object of {name: class} based on a directory.
    """

    playstyles = {}

    # Filenames in this list will be ignored
    __ignore__ = ["Default.py", "Template.py", "__init__.py"]

    # Get all .py files in the Styles directory
    files = [fileName for fileName in os.listdir(
        pathToDirectory) if not fileName in __ignore__ and fileName.endswith(".py")]

    for fileName in files:
        moduleName = fileName[:-3]

        playstyles[moduleName] = importlib.import_module(
            "Styles." + moduleName).Playstyle

    return playstyles
