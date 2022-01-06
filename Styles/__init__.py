from Styles.Copy import Copy
from Styles.User import UserInput

from utils.json import readCustomPlaystyles
from utils.createClass import createProbaClass, createSchemaClass

customStyles = readCustomPlaystyles()

if customStyles is not None:
    for name, value in customStyles.items():
        isValueNumeric = isinstance(value, (int, float))

        # TODO: Comment why did I use locals
        if isValueNumeric:
            locals()[name] = createProbaClass(name, value)
            continue

        isValueAPlaystyle = all(
            l for l in value if l.upper() == "C" or l.upper() == "B")

        if isValueAPlaystyle:
            locals()[name] = createSchemaClass(name, value)
            continue
