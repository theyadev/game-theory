
from utils.json import readPlaystyles
from utils.createClass import createProbaClass, createSchemaClass


def createPlaystyles(path: str):
    """
        Create an object of {name: class} based on a .json
    """

    customStyles = readPlaystyles(path)

    classes = {}

    if customStyles is not None:
        for name, value in customStyles.items():
            isValueNumeric = isinstance(value, (int, float))

            # TODO: Comment why did I use locals
            if isValueNumeric:
                classes[name] = createProbaClass(name, value)
                continue

            isValueAPlaystyle = all(
                l for l in value if l.upper() == "C" or l.upper() == "B")

            if isValueAPlaystyle:
                classes[name] = createSchemaClass(name, value)
                continue

    return classes
