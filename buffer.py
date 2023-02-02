# @dataclass czy można dodać deafult parametr?
class Buffer:
    # name:str
    # cipher:str
    # status:str
    # rot:str
    def __init__(self, name=None, status=None, rot=None) -> None:
        self.name = name
        self.status = status
        self.rot = rot


buffer1 = Buffer()  # czy tak ok?
