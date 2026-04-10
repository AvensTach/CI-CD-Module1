# File Filter Processor

A robust Python application designed to read a text file, filter lines based on specific keywords (e.g., "ERROR"), and output the results to a new file. This project is built with a strong emphasis on Object-Oriented Programming (OOP) and adheres strictly to **SOLID** principles.

## Features
* **Keyword Filtering**: Automatically scans text and extracts lines containing specified keywords.
* **SOLID Architecture**: Uses abstract base classes (`DataReader`, `DataWriter`, `FilterStrategy`) to ensure the code is modular, decoupled, and easy to extend.
* **Automated Testing**: Comprehensive unit and integration tests using `pytest` with fixtures and parametrization.
* **Continuous Integration**: Automated GitHub Actions workflow for linting (PEP8) and testing on every push and pull request.
* **HTML Test Reports**: Automatically generates self-contained HTML test reports locally and as CI workflow artifacts.

## Project Structure

```text
├── .github/workflows/
│   └── ci.yml                 # GitHub Actions pipeline configuration
├── Files/
│   ├── input.txt              # Directory for input data
│   └── filtered.txt           # Generated output file (after running)
├── Tests/
│   └── file_processor_test.py # Unit and integration tests (pytest)
├── .flake8                    # Flake8 linting configuration
├── .gitignore                 # Git ignore rules
├── file_processor.py          # Core logic, classes, and interfaces
├── main.py                    # Main execution script
├── requirements.txt           # Project dependencies
└── README.md
```

## Prerequisites

* **Python 3.10+** (The CI pipeline is tested against Python 3.14)
* **Git**

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **(Optional but recommended) Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have an `input.txt` file located inside the `Files/` directory.
2. Run the main script:
   ```bash
   python main.py
   ```
3. The script will process `Files/input.txt`, extract all lines containing the word `ERROR`, and save them to `Files/filtered.txt`.

## Testing

This project uses `pytest` for unit testing. 

To run the tests and generate an HTML report, execute the following command in your terminal:
```bash
pytest --html=report.html --self-contained-html
```
After the tests complete, open `report.html` in your web browser to view the detailed test results.

## Linting & Code Quality

The codebase enforces PEP8 standards using `flake8`. The maximum line length is set to 100 characters.

To run the linter manually:
```bash
flake8 . --show-source --statistics
```

## Continuous Integration (CI/CD)

This repository uses **GitHub Actions** to automate quality checks. On every push or pull request to the `main`, `master`, or `dev` branches, the CI pipeline will automatically:
1. Set up the Python environment.
2. Install all required dependencies.
3. Run `flake8` to check for PEP8 compliance.
4. Run `pytest` to execute all unit tests.
5. Upload the `report.html` test results as a downloadable artifact in the GitHub Actions tab.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.