# @dataclass czy można dodać deafult parametr?
class Buffer:
    """Class storing cipher text"""

    # name:str
    # cipher:str
    # status:str
    # rot:str
    def __init__(self, name: str = None, status: str = None, rot: str = None) -> None:
        """Cipher object"""
        self.name = name
        self.status = status
        self.rot = rot


buffer1 = Buffer()  # tutaj czy w mainie
