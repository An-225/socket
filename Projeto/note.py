from _typeshed import Self
from typing import Text


class Note:
    id = int()
    name = str()
    text = str()

    def __init__(self,) -> None:
        pass

    def fromTuple(self,data:tuple) -> None:
        self.id = int(data[0])
        self.name = data[1]
        self.text = data[2]

    