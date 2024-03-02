from TipoComponente import TipoComponente


class Componente:
    def __init__(self, tipo: TipoComponente, nome: str, elementos: str):
        self.tipo = tipo
        self.nome = nome
        self.elementos = elementos

    def gerar(self):
        print(f"Gerando componente do tipo {self.tipo.value} com nome {self.nome}")
        if self.tipo == TipoComponente.ENTITY:
            self.gerarEntidade(atributosStr=self.elementos)

    def gerarEntidade(self, atributosStr: str):
        with open('TemplateEntidade.txt', 'r') as arquivo:
            template = arquivo.readlines()

        listaAtributos = atributosStr.split(',')
        nomeEntidade   = listaAtributos.pop(0)

        template = [linha.replace(";;;NOME_ENTIDADE;;;", nomeEntidade) for linha in template]

        indice_ini = template.index(";;;ATRIBUTOS_INI;;;\n")
        indice_fim = template.index(";;;ATRIBUTOS_FIM;;;\n")



        for atributo in listaAtributos:
            elementosAtributo = []
            elementosAtributo = atributo.split('.')
            tamanho = len(elementosAtributo)
            tipoAtributo = elementosAtributo[0]
            nomeAtributo = elementosAtributo[1]
            textoAtributo = "\tprivate " + tipoAtributo + " " + nomeAtributo + ";"
            template.insert(indice_fim, f'{textoAtributo}\n\n')

            if tamanho == 3:
                mapAtributo = elementosAtributo[2]
                textoAtributo = "\t@JoinColumn(name=\""+ mapAtributo + "\")"
                template.insert(indice_fim, f'{textoAtributo}\n')
                textoAtributo = "\t@ManyToOne"
                template.insert(indice_fim, f'{textoAtributo}\n')




        nomeArquivo = nomeEntidade + ".java"

        with open(nomeArquivo, 'w') as arquivo:
            arquivo.writelines(template)






