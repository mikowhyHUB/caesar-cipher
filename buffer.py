from datetime import datetime

import now as now


class Buffer:
    """Class storing list of cipher text"""

    def __init__(self):
        self.memory = []

    # def peak_buffer(self):
    #     pass
    #
    # def add_to_buffer(self, obj: Text):
    #     if isinstance(obj, Text):
    #         pass


DT_STRING = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


class Text:
    def __init__(self, name: str = None, status: str = None, rot: int = None) -> None:
        """Text object"""
        self.name = name
        self.status = status
        self.rot = rot

    @staticmethod
    def to_dct(name, memory, status, rot):
        return {name: memory, "created": DT_STRING, "status": status, "rot": rot}

    # -> buffer = ['text', text2, text3] {'name': 'xyz','status:'encrypted' 'rot': 13}
    # {'users name': [lsita textow], 'created': ...., 'status:'encrypted' 'rot': 13}
