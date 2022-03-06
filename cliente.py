
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # get e set ↓ linha 8-16
    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.nome.title() # .title serve para deixar a 1° letra maiúscula

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome