from TipoComponente import TipoComponente
from Componente import Componente



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tipo = TipoComponente.DTO
    nome = "UsuarioDTO"
    componente = Componente(tipo, nome)
    componente.gerar()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
