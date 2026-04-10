from pathlib import Path
from file_processor import TextFileReader, TextFileWriter, KeywordFilter, FileProcessor

if __name__ == "__main__":

    folder = Path("Files")

    # Create the folder if it doesn't exist
    folder.mkdir(parents=True, exist_ok=True)

    input_file = str(folder / "input.txt")
    output_file = str(folder / "filtered.txt")
    search_keyword = "ERROR"

    reader = TextFileReader(input_file)
    writer = TextFileWriter(output_file)
    filter_strategy = KeywordFilter(search_keyword)

    processor = FileProcessor(reader, writer, filter_strategy)

    try:
        processor.process()
        print("File processing completed successfully.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
