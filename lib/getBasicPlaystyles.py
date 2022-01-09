
from lib.json import readPlaystyles
from lib.createClass import createProbaClass, createSchemaClass


def getBasicPlaystyles(pathToJSON: str):
    """
        Create an object of {name: class} based on a .json
    """

    customStyles = readPlaystyles(pathToJSON)

    classes = {}

    if customStyles is not None:
        for name, value in customStyles.items():
            isValueNumeric = isinstance(value, (int, float))

            if isValueNumeric:
                classes[name] = createProbaClass(name, value)
                continue

            isValueAPlaystyle = all(
                l for l in value if l.upper() == "C" or l.upper() == "B")

            if isValueAPlaystyle:
                classes[name] = createSchemaClass(name, value)
                continue

    return classes
