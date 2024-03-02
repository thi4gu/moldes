from TipoComponente import TipoComponente
from Componente import Componente



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tipo = TipoComponente.ENTITY
    nome = "Cidade"
    elementos = "Cidade,String.sigla,String.nome,Estado.estado.id_estado"
    componente = Componente(tipo, nome, elementos)
    componente.gerar()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
