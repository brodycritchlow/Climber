from abc import ABC, abstractmethod
from typing import Callable, Concatenate, Optional, ParamSpec, TypeVar, Any, List
from typing_extensions import Self

from pydantic import BaseModel

RT = TypeVar('RT', bound=Any)  # return type

class ParserArgumentError(Exception):
    """
<<<<<<< HEAD
    Error occured when trying to parse name
    """
=======
    Error occured while Parsing.
    """
    ...
>>>>>>> db5ac55 (Fix Typehinting)

ParserArgumentError.__module__ = "Climber"


class BaseParser(BaseModel, ABC):
    """
    The base pydantic model for parsers, provided for ease of use.
    Allows for the creation, and modification of more advanced models.
    """

    def parser(
        self, name: str = "", all_required: Optional[bool] = False
    ) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
        """
        Parser decorator, that creates the command line function.
        """

        def inner(func: Callable[..., RT]) -> Callable[..., RT]:
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                annotations = func.__annotations__

                try:
                    __type = annotations[name]
                except KeyError as exc:
                    raise ParserArgumentError(
                        f"{repr(name)} is not a valid argument, valid names: {list(annotations.keys())}"
                    ) from exc

                return (__type )

            return wrapper

        return inner


