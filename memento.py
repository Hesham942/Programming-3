class Memento:
    def __init__(self,content):
        self.content=content

class x:
    def __init__(self,content):
        self.content=""
    def write(self,string):
        self.content+=string
    def save(self):
        return Memento(self.content)
    def undo(self,memento):
        self.content=memento.content

class y:
    def save(self,writer):
        self.mem=writer.save()

    def undo(self,writer):
        writer.undo(self.mem)


if __name__=="__main__":
    c=y()

    writer=x("h.txt")

    writer.write("first version of data\n")
    print(writer.content+"\n\n")

    c.save(writer)
    writer.write("second version of data\n")
    print(writer.content+"\n\n")
    writer.write("second version of data\n")
    print(writer.undo())