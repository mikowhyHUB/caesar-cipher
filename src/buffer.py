from datetime import datetime


class Buffer:
    """Class storing list of cipher text"""

    def __init__(self):
        self.memory: list = []


class Text:

    def __init__(self, status: str = None, rot: int = None) -> None:
        """Text object"""
        self.status = status
        self.rot = rot
        self.DT_STRING: str = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.buffer = Buffer()

    def to_dct(self, status: str, rot: int) -> dict:
        """Changing Text object to dict"""
        return {
            'text': self.buffer.memory,
            "created": self.DT_STRING,
            "status": status,
            "rot": rot,
        }
