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


# --- Parametrized Tests ---

@pytest.mark.parametrize("keyword, expected_lines", [
    ("ERROR", ["ERROR: Database connection failed\n", "ERROR: Timeout occurred\n"]),
    ("INFO", ["INFO: Application started\n"]),
    ("WARNING", []),  # No matches
])
def test_keyword_filter(keyword, expected_lines):
    """Test the KeywordFilter logic directly."""
    # Arrange
    lines = [
        "INFO: Application started\n",
        "ERROR: Database connection failed\n",
        "DEBUG: Loading modules\n",
        "ERROR: Timeout occurred\n"
    ]
    filter_strategy = KeywordFilter(keyword)

    # Act
    filtered = [line for line in lines if filter_strategy.is_match(line)]

    # Assert
    assert filtered == expected_lines


def test_file_processor_integration(sample_input_file, output_file_path):
    """Test the entire FileProcessor workflow using fixtures."""
    # Arrange
    keyword = "ERROR"
    reader = TextFileReader(sample_input_file)
    writer = TextFileWriter(output_file_path)
    filter_strategy = KeywordFilter(keyword)
    processor = FileProcessor(reader, writer, filter_strategy)

    # Act
    processor.process()

    # Assert
    with open(output_file_path, 'r', encoding="utf-8") as f:
        result_lines = f.readlines()

    assert len(result_lines) == 2
    assert "ERROR: Database connection failed\n" in result_lines
    assert "ERROR: Timeout occurred\n" in result_lines