from abc import ABC, abstractmethod
from typing import List


class Service(ABC):
    @abstractmethod
    def good(self, a: int, b: float) -> None:
        # ok: abstract-method-raise-not-implemented
        raise NotImplementedError

    @abstractmethod
    def still_okay(self):
        # ok: abstract-method-raise-not-implemented
        raise NotImplementedError

    @abstractmethod
    def bad(self, input_size: int) -> float:
        # ruleid: abstract-method-raise-not-implemented
        ...

    @abstractmethod
    def bad_but_with_pass(self):
        # ruleid: abstract-method-raise-not-implemented
        pass

    @abstractmethod
    def bad_because_of_implementation(self, something) -> List:
        # ruleid: abstract-method-raise-not-implemented
        result = [i * 2 for i in range(10)]
        return result
