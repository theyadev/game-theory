from Styles.Default import Style

from Classes.Actions import ACTIONS


def createProbaClass(name: str, number: float):
    """
        Create a Style class based on a probability of Cooperate
    """

    class newStyle(Style):
        def __init__(self, player) -> None:
            super().__init__(player, number)

        def __str__(self) -> str:
            return name

    return newStyle


def createSchemaClass(name: str, string: str):
    """
        Create a Style class based on a schema of Cooperate/Betray\n

        keyword arguments:\n
        name -- name of the class
        string -- schema of Cooperate/Betray (exemple: "BBCCB")
    """

    class newStyle(Style):
        def __init__(self, player) -> None:
            super().__init__(player)
            self.schema = list(string)

        def getAction(self):
            if len(self.schema) > 0:
                return ACTIONS.get(self.schema.pop(0))
            else:
                return ACTIONS.COOPERATE

        def __str__(self) -> str:
            return name

    return newStyle
