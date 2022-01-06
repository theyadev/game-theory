class ACTIONS:
    """
        Contains Cooperate and Betray as classes variables\n
        Used in case I need to rename the string names
    """

    COOPERATE = "Cooperer"
    BETRAY = "Trahir"

    @classmethod
    def get(cls, l: str):
        if l.upper() == "C":
            return cls.COOPERATE
        if l.upper() == "B":
            return cls.BETRAY

        return None
