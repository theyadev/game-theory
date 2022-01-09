import os 
import importlib

def getComplexPlaystyles():
    """
        Create an object of {name: class} based on the Styles directory.
    """

    playstyles = {}

    # Filenames in this list will be ignored
    __ignore__ = ["Default.py", "Template.py", "__init__.py"]

    # Get all .py files in the Styles directory
    files = [fileName for fileName in os.listdir(
        "./Styles") if not fileName in __ignore__ and fileName.endswith(".py")]

    for fileName in files:
        moduleName = fileName[:-3]
        
        playstyles[moduleName] = importlib.import_module("Styles." + moduleName).Name
    
    return playstyles
