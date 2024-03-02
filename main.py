from TipoComponente import TipoComponente
from Componente import Componente



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    elementos = "Cidade,String.sigla,String.nome,Estado.estado.id_estado"

    componenteEntidade = Componente(TipoComponente.ENTITY, "Cidade", elementos)
    componenteEntidade.gerar()


    componenteRepository = Componente(TipoComponente.REPOSITORY, "Cidade", elementos)
    componenteRepository.gerar()


    componenteService = Componente(TipoComponente.SERVICE, "Cidade", elementos)
    componenteService.gerar()


    componenteResource = Componente(TipoComponente.RESOURCE, "Cidade", elementos)
    componenteResource.gerar()







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
