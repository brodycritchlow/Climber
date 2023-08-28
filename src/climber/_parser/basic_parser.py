from typing import Optional, Callable, ParamSpec, TypeVar, Concatenate
from pydantic import field_validator
from base import BaseParser, ParserArgumentError

Param = ParamSpec("Param")
RetType = TypeVar("RetType")
OriginalFunc = Callable[Param, RetType]
DecoratedFunc = Callable[Concatenate[str, Param], RetType]

class Parser(BaseParser):
    name: str
    required: bool = Optional[bool]

    def arg(
        self, name: str = "", required: Optional[bool] = False
    ) -> Callable[[OriginalFunc], DecoratedFunc]:
        def inner(func: OriginalFunc) -> DecoratedFunc:
            anno = func.__annotations__

            def wrapper(*args, **kwargs) -> None:
                try:
                    __type = anno[self.name]
                    
                except KeyError as exc:
                    raise ParserArgumentError(
                        f"{repr(self.name)} is not a valid argument, valid names: {list(anno.keys())}"
                    ) from exc
            
            return wrapper
        return inner

    @field_validator('name')
    @classmethod
    def name_validator(cls, name: str) -> str:
        if name.strip() == '':
            raise ValueError('Name cannot be empty.')
        return name
    
