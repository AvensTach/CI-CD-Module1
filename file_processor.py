from abc import ABC, abstractmethod
from typing import Iterable


# --- Interfaces ---

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


class KeywordFilter(FilterStrategy):
    """Filters lines based on a specific keyword."""

    def __init__(self, keyword: str):
        self.keyword = keyword

    def is_match(self, item: str) -> bool:
        """Returns True if keyword is present in the item."""
        return self.keyword in item


class FileProcessor:
    """Processes files using provided reader, writer, and filter."""

    def __init__(
            self,
            reader: DataReader,
            writer: DataWriter,
            filter_strategy: FilterStrategy
    ):
        self.reader = reader
        self.writer = writer
        self.filter_strategy = filter_strategy

    def process(self) -> None:
        """Reads, filters, and writes data."""
        raw_data = self.reader.read()
        filtered_data = (line for line in raw_data if self.filter_strategy.is_match(line))
        self.writer.write(filtered_data)
