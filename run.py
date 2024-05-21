import os
from src.file_processor import FileProcessor

input_folder = 'input'
output_folder = 'output'

if __name__ == "__main__":
    file_data = FileProcessor.read_files_from_folder(input_folder)
    unique_data = FileProcessor.process_data(file_data)

    # Calculate gross salaries
    salaries = [int(row[5]) + int(row[6]) for row in unique_data]

    # Calculate footer details
    footer = FileProcessor.calculate_footer(salaries)

    # Write data and footer to CSV
    output_file_path = os.path.join(output_folder, 'RESULT_NEW.csv')
    FileProcessor.write_to_csv(output_file_path, unique_data, footer)
