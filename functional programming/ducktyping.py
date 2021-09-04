#duck typing

class vscode:
    def compile(self):
        print("Compiling using vscode")
    def execute(self):
        print("execute using vscode")
    def debug(self):
        print("Debug using vscode")

class Pycharm:
    def compile(self):
        print("Compiling using pycharm")

    def execute(self):
        print("execute using pycharm")

    def debug(self):
        print("Debug using pycharm")

class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()

dev=Programmer()
pyc=Pycharm()
dev.coding(pyc)