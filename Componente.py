import TipoComponente


class Componente:
    def __init__(self, tipo: TipoComponente, nome: str):
        self.tipo = tipo
        self.nome = nome

    def gerar(self):
        # Aqui você implementaria a lógica para gerar o componente com base nos atributos
        print(f"Gerando componente do tipo {self.tipo.value} com nome {self.nome}")