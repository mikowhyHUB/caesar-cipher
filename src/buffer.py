from datetime import datetime



class Buffer:
    """Class storing list of cipher text"""

    def __init__(self):
        self.text = Text()
        self.memory: list = []


class Text:

    def __init__(self, name: str = None, status: str = None, rot: int = None) -> None:
        """Text object"""
        self.name = name
        self.status = status
        self.rot = rot
        self.memory: list = []
        self.DT_STRING: str = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def to_dct(self, name: str, memory: str, status: str, rot: int):
        """Changing Text object to dict"""
        return {
            name: memory,
            "created": self.DT_STRING,
            "status": status,
            "rot": rot,
        }
