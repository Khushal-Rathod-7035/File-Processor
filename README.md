# File-Processor
Back-end development task : File Processor

## Overview

This project is designed to read data from multiple files located in `input/` folder, process the data, and generate an output CSV file in `output/` folder. The output file will contain unique data entries and a footer with the second highest salary and the average salary.
- [Design Specification](https://github.com/Khushal-Rathod-7035/File-Processor/blob/master/documents/DesignSpecification.pdf)

## Project Structure

- `input/`: Folder containing input data files.
- `output/`: Folder where the output CSV file will be saved.
- `src/`: Source code for the file processor.
- `tests/`: Unit tests for the file processor.
- `.gitignore`: Git ignore file.
- `README.md`: Project documentation.
- `requirements.txt`: Dependencies required for the project.
- `run.py`: Script to run the file processor.
- `run_tests.py`: Script to run the tests.

## Running the Project

### Requirements
- Python 3.x
- Packages listed in requirements.txt

### Notes
- Ensure the input files are placed in the input/ folder.
- The output CSV file will be saved in the output/ folder as RESULT_NEW.csv.

1. Set up the virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

2. Install dependencies:
   ```sh
   pip install -r requirements.txt

3. Run the tests:
   ```sh
   python run_tests.py

4. Run the file processor:
   ```sh
   python run.py
