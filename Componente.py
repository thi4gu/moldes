from TipoComponente import TipoComponente


class Componente:
    def __init__(self, tipo: TipoComponente, nome: str, elementos: str):
        self.tipo = tipo
        self.nome = nome
        self.elementos = elementos

    def gerar(self):
        #print(f"Gerando componente do tipo {self.tipo.value} com nome {self.nome}")
        if self.tipo == TipoComponente.ENTITY:
            self.gerarEntidade(atributosStr=self.elementos)
            self.gerarDTO(atributosStr=self.elementos)
        if self.tipo == TipoComponente.REPOSITORY:
            self.gerarRepository()
        if self.tipo == TipoComponente.SERVICE:
            self.gerarService(atributosStr=self.elementos)
        #if self.tipo == TipoComponente.resource:
        #    self.gerarResource()

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

        template = [linha.replace(";;;NOME_ENTIDADE;;;", "") for linha in template]
        template = [linha.replace(";;;ATRIBUTOS_INI;;;\n", "") for linha in template]
        template = [linha.replace(";;;ATRIBUTOS_FIM;;;\n", "") for linha in template]

        nomeArquivo = "saida/"+nomeEntidade + ".java"

        with open(nomeArquivo, 'w') as arquivo:
            arquivo.writelines(template)

    def gerarDTO(self, atributosStr: str):
        with open('TemplateDTO.txt', 'r') as arquivo:
            template = arquivo.readlines()

        listaAtributos = atributosStr.split(',')
        nomeEntidade   = listaAtributos.pop(0)

        template = [linha.replace(";;;NOME_ENTIDADE;;;", nomeEntidade) for linha in template]




        for atributo in listaAtributos:
            elementosAtributo = []
            elementosAtributo = atributo.split('.')
            tamanho = len(elementosAtributo)



            tipoAtributo = elementosAtributo[0]

            if tamanho == 3:

                indice_map = template.index(";;;IDX_MAP;;;\n")
                nomeAtributo = "id" + elementosAtributo[1].capitalize()
                textoAtributo = "\t\tthis." + nomeAtributo + " = obj.get" + tipoAtributo.capitalize() + "().getId();"
                template.insert(indice_map, f'{textoAtributo}\n')

                indice_atr = template.index(";;;IDX_ATR;;;\n")
                tipoAtributo = elementosAtributo[0]
                nomeAtributo = elementosAtributo[1]
                textoAtributo = "\tprivate " + tipoAtributo + " id" + nomeAtributo.capitalize() + ";"
                template.insert(indice_atr, f'{textoAtributo}\n')

            else:

                indice_map = template.index(";;;IDX_MAP;;;\n")
                nomeAtributo = elementosAtributo[1]
                textoAtributo = "\t\tthis." + nomeAtributo + " = obj.get" + tipoAtributo.capitalize() + "();"
                template.insert(indice_map, f'{textoAtributo}\n')

                indice_atr = template.index(";;;IDX_ATR;;;\n")
                tipoAtributo = elementosAtributo[0]
                nomeAtributo = elementosAtributo[1]
                textoAtributo = "\tprivate " + tipoAtributo + " " + nomeAtributo + ";"
                template.insert(indice_atr, f'{textoAtributo}\n')




        template = [linha.replace(";;;NOME_ENTIDADE;;;", "") for linha in template]
        template = [linha.replace(";;;IDX_MAP;;;\n", "") for linha in template]
        template = [linha.replace(";;;IDX_ATR;;;\n", "") for linha in template]

        nomeArquivo = "saida/"+nomeEntidade + "DTO.java"
        with open(nomeArquivo, 'w') as arquivo:
            arquivo.writelines(template)


    def gerarRepository(self):
        with open('TemplateRepository.txt', 'r') as arquivo:
            template = arquivo.readlines()

        template = [linha.replace(";;;NOME_ENTIDADE;;;", self.nome) for linha in template]

        nomeArquivo = "saida/" + self.nome + "Repository.java"
        with open(nomeArquivo, 'w') as arquivo:
            arquivo.writelines(template)


    def gerarService(self, atributosStr: str):
        with open('TemplateService.txt', 'r') as arquivo:
            template = arquivo.readlines()

        tipo_entidade = self.nome
        tipo_entidade = tipo_entidade.capitalize()

        template = [linha.replace(";;;NOME_ENTIDADE;;;", self.nome.lower()) for linha in template]
        template = [linha.replace(";;;TIPO_ENTIDADE;;;", tipo_entidade) for linha in template]



        nomeArquivo = "saida/" + self.nome + "Service.java"

        listaAtributos = atributosStr.split(',')
        nomeEntidade = listaAtributos.pop(0).lower()

        for atributo in listaAtributos:
            elementosAtributo = []
            elementosAtributo = atributo.split('.')
            tamanho = len(elementosAtributo)

            tipoAtributo = elementosAtributo[0]
            nomeAtributo = elementosAtributo[1].lower()

            if tamanho == 3:

                indice_map = template.index(";;;IDX_MAP;;;\n")
                textoAtributo = "\t\t" + nomeEntidade + ".set" + nomeAtributo.capitalize() + "(" + nomeAtributo + ");"
                template.insert(indice_map, f'{textoAtributo}\n')
                textoAtributo = "\t\t" + nomeAtributo.capitalize() + " " + nomeAtributo + " = find" + nomeAtributo.capitalize() + "ById(" + nomeAtributo + "DTO.getId"+nomeAtributo.capitalize()+"());"
                template.insert(indice_map, f'{textoAtributo}\n')
                indice_map = template.index(";;;IDX_REP;;;\n")
                textoAtributo = "\t" + nomeAtributo.capitalize() + "Repository " + nomeAtributo + "Repository;"
                template.insert(indice_map, f'{textoAtributo}\n')
                textoAtributo = "\t" + "@Autowired"
                template.insert(indice_map, f'{textoAtributo}\n')

                indice_map = template.index(";;;IDX_FBI;;;\n")
                textoAtributo = "\t\tobj.orElseThrow(() -> new ObjectNotFoundException(\"" + nomeAtributo.capitalize() + "\"+id+\" não encontrado!\" ));\n\t}"
                template.insert(indice_map, f'{textoAtributo}\n')
                textoAtributo = "\t\tOptional<"+nomeAtributo.capitalize()+"> obj = "+nomeAtributo+"Repository.findById(id);"
                template.insert(indice_map, f'{textoAtributo}\n')
                textoAtributo = "\tpublic " + nomeAtributo.capitalize()+ " find" + nomeAtributo.capitalize() + "ById(Long id) {"
                template.insert(indice_map, f'{textoAtributo}\n')



            else:

                indice_map = template.index(";;;IDX_MAP;;;\n")
                textoAtributo = "\t\t" + nomeEntidade + ".set" + nomeAtributo.capitalize() + "(" + nomeEntidade + "DTO.get" + nomeAtributo.capitalize() +"();"
                template.insert(indice_map, f'{textoAtributo}\n')

        template = [linha.replace(";;;NOME_ENTIDADE;;;", "") for linha in template]
        template = [linha.replace(";;;TIPO_ENTIDADE;;;", "") for linha in template]
        template = [linha.replace(";;;IDX_MAP;;;", "") for linha in template]
        template = [linha.replace(";;;IDX_REP;;;", "") for linha in template]
        template = [linha.replace(";;;IDX_FBI;;;", "") for linha in template]

        with open(nomeArquivo, 'w') as arquivo:
            arquivo.writelines(template)
