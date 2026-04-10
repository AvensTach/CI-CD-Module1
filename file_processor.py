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


# --- Concrete Implementations ---

class TextFileReader(DataReader):
    """Reads lines from a text file."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> Iterable[str]:
        """Yields lines from the file one by one."""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line


class TextFileWriter(DataWriter):
    """Writes lines to a text file."""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def write(self, data: Iterable[str]) -> None:
        """Writes given iterable of strings to the file."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.writelines(data)


