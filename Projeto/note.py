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
    
    def toTuple(self) -> tuple:
        temp = (str(self.id),self.name,self.text)
        return temp
    
    def print(self) -> None:
        print(f"ID: {self.id} | Name: {self.name}\nText: {self.text}")