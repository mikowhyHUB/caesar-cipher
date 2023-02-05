from datetime import datetime


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


class TextName:
    def __init__(self, name: str = None, status: str = None, rot: int = None) -> None:
        """Text object"""
        self.name = name
        self.status = status
        self.rot = rot
        self.created_at = datetime.now()

    def to_dct(self, name, status, rot):
        return {"name": name, "status": status, "rot": rot}

    # -> buffer = ['text', text2, text3] {'name': 'xyz','status:'encrypted' 'rot': 13}
