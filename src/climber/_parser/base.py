from abc import ABC, abstractmethod
from typing import Callable, Concatenate, Optional, ParamSpec, TypeVar

from pydantic import BaseModel

Param = ParamSpec("Param")
RetType = TypeVar("RetType")
OriginalFunc = Callable[Param, RetType]
DecoratedFunc = Callable[Concatenate[str, Param], RetType]


class ParserArgumentError(Exception):
    """
    Error occured when trying to parse name
    """

ParserArgumentError.__module__ = "Climber"


class BaseParser(BaseModel, ABC):
    """
    The base pydantic model for parsers, provided for ease of use.
    Allows for the creation, and modification of more advanced models.
    """

    def parser(
        self, name: str = "", required: Optional[bool] = False
    ) -> Callable[[OriginalFunc], DecoratedFunc]:
        """
        Parser decorator, that creates the command line function.
        """

        def inner(func: OriginalFunc) -> DecoratedFunc:
            def wrapper(*args, **kwargs):
                annotations = func.__annotations__
                try:
                    __type = annotations[name]
                except KeyError as exc:
                    raise ParserArgumentError(
                        f"{repr(name)} is not a valid argument, valid names: {list(annotations.keys())}"
                    ) from exc

            return wrapper

        return inner


