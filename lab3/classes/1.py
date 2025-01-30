class Text:
    def __init__(self,string):
        self.string =string
    def getString(self):
        self.string= input("enter your string:")

    def printString(self):
        print(self.string)

#test
t=Text("space")
t.getString
t.printString
