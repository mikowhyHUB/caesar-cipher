from dataclasses import dataclass
from datetime import datetime

""" chodzilo o to, zeby user mogl dodawac do buffera wiele slow/ zdan encrypted. i wtedsy moze sobie je zapisac """


class Buffer:
    """Class storing cipher text"""

    def __init__(self):
        self.buffer = []

    # def peak_buffer(self):
    #     pass
    #
    # def add_to_buffer(self, obj: Text):
    #     if isinstance(obj, Text):
    #         pass


class Text:
    """Class storing cipher text"""

    # name: str = None
    # status: str = None
    # rot: str = None

    def __init__(self, name: str = None, status: str = None, rot: str = None) -> None:
        """Text object"""
        self.name = name
        self.status = status
        self.rot = rot
        self.created_at = datetime.now()

    # def to_dct(self):
    #     return {'name': }

    # -> buffer = ['text', text2, text3] {'name': 'xyz', 'rot': 13}
