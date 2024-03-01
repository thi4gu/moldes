from enum import Enum


class TipoComponente(Enum):
    DTO = 'dto'
    REPOSITORY = 'repository'
    SERVICE = 'service'
    RESOURCE = 'resource'