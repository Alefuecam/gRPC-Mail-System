from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RegistroUsuario(_message.Message):
    __slots__ = ("nombre", "contra")
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    CONTRA_FIELD_NUMBER: _ClassVar[int]
    nombre: str
    contra: int
    def __init__(self, nombre: _Optional[str] = ..., contra: _Optional[int] = ...) -> None: ...

class Usuario(_message.Message):
    __slots__ = ("nombre", "id")
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    nombre: str
    id: int
    def __init__(self, nombre: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class LoginUsuario(_message.Message):
    __slots__ = ("nombre", "contra")
    NOMBRE_FIELD_NUMBER: _ClassVar[int]
    CONTRA_FIELD_NUMBER: _ClassVar[int]
    nombre: str
    contra: int
    def __init__(self, nombre: _Optional[str] = ..., contra: _Optional[int] = ...) -> None: ...

class Correos(_message.Message):
    __slots__ = ("nombreDest", "contenido", "nombreRemitente", "estado", "tema", "id")
    NOMBREDEST_FIELD_NUMBER: _ClassVar[int]
    CONTENIDO_FIELD_NUMBER: _ClassVar[int]
    NOMBREREMITENTE_FIELD_NUMBER: _ClassVar[int]
    ESTADO_FIELD_NUMBER: _ClassVar[int]
    TEMA_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    nombreDest: str
    contenido: str
    nombreRemitente: str
    estado: bool
    tema: str
    id: int
    def __init__(self, nombreDest: _Optional[str] = ..., contenido: _Optional[str] = ..., nombreRemitente: _Optional[str] = ..., estado: bool = ..., tema: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
