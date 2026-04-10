import pytest
from file_processor import (
    TextFileReader,
    TextFileWriter,
    KeywordFilter,
    FileProcessor
)


# --- Fixtures ---

@pytest.fixture
def sample_input_file(tmp_path):
    """Fixture to create a temporary input file with sample data."""
    file_path = tmp_path / "test_input.txt"
    content = (
        "INFO: Application started\n"
        "ERROR: Database connection failed\n"
        "DEBUG: Loading modules\n"
        "ERROR: Timeout occurred\n"
    )
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)


@pytest.fixture
def output_file_path(tmp_path):
    """Fixture to provide a path for the temporary output file."""
    return str(tmp_path / "test_output.txt")

