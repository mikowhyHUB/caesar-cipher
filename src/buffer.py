from datetime import datetime

import now as now


class Buffer:
    """Class storing list of cipher text"""

    def __init__(self):
        self.memory: list = []


DT_STRING: str = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


class Text:
    def __init__(self, name: str = None, status: str = None, rot: int = None) -> None:
        """Text object"""
        self.name = name
        self.status = status
        self.rot = rot

    @staticmethod
    def to_dct(name: str, memory: str, status: str, rot: int):
        return {name: memory, "created": DT_STRING, "status": status, "rot": rot}
