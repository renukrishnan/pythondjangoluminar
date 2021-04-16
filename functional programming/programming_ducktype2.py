class Pycharm:
    def open(self):
        print(" open method in pycharm")
    def run(self):
        print(" run functionality in pycharm")
    def debug(self):
        print(" debbugging using pycharm")
class Vscode:
    def open(self):
        print(" open method in VScode")
    def run(self):
        print(" run functionality in Vscode")
    def debug(self):
        print(" debbugging using Vscode")


class Programmer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debug()
py=Pycharm()
vsc=Vscode()
pg=Programmer()
pg.coding(py)
pg.coding(vsc)