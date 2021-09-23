class Note:
    __id = int()
    name = str()
    text = str()

    def __init__(self,) -> None:
        pass

    def fromTuple(self,data:tuple) -> None:
        self.__id = int(data[0])
        self.name = data[1]
        self.text = data[2]

    