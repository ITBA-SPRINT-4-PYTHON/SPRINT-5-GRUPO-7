class Exitosas():
    def __init__(self,eventos):
        self.exitos = [ x for x in eventos if x['estado']== 'ACEPTADA']

    def allExitosas(self):
        for e in self.exitos:
            print(e) 