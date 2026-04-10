from abc import ABC, abstractmethod
from typing import List, Iterable
from pathlib import Path

# --- Interfaces (ISP: Interface Segregation Principle) ---

class DataReader(ABC):
    """Abstract base class for reading data."""

    @abstractmethod
    def read(self) -> Iterable[str]:
        pass


class DataWriter(ABC):
    """Abstract base class for writing data."""

    @abstractmethod
    def write(self, data: Iterable[str]) -> None:
        pass


class FilterStrategy(ABC):
    """Abstract base class for filtering logic."""

    @abstractmethod
    def is_match(self, item: str) -> bool:
        pass


