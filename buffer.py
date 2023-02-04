from dataclasses import dataclass
from datetime import datetime

""" chodzilo o to, zeby user mogl dodawac do buffera wiele slow/ zdan encrypted. i wtedsy moze sobie je zapisac """


class Buffer:
    """Class storing cipher text"""

    def __init__(self):
        self.memory = []

    # def peak_buffer(self):
    #     pass
    #
    # def add_to_buffer(self, obj: Text):
    #     if isinstance(obj, Text):
    #         pass


class Test:
    def __init__(self, name: str = None, status: str = None, rot: str = None) -> None:
        """Text object"""
        self.name = name
        self.status = status
        self.rot = rot
        self.created_at = datetime.now()

    def to_dct(self, status, rot):
        return {"name": input("test name dict: "), "status": status, "rot": rot}

    # -> buffer = ['text', text2, text3] {'name': 'xyz', 'rot': 13}
