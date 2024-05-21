import os
import csv


class FileProcessor:
    @staticmethod
    def read_files_from_folder(folder_path):
        file_data = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    reader = csv.reader(file, delimiter='\t')
                    next(reader)  # Skip header
                    for row in reader:
                        file_data.append(tuple(row))
        return file_data

    @staticmethod
    def process_data(data):
        unique_data = list(set(data))  # Remove duplicates
        return unique_data

    @staticmethod
    def calculate_footer(salaries):
        sorted_salaries = sorted(salaries, reverse=True)
        second_highest_salary = sorted_salaries[1] if len(sorted_salaries) > 1 else None
        average_salary = sum(salaries) / len(salaries) if salaries else None
        return {'2nd_highest_salary': second_highest_salary, 'average_salary': average_salary}

    @staticmethod
    def write_to_csv(output_file_path, data, footer):
        with open(output_file_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(
                ['id', 'first_name', 'last_name', 'email', 'job_title', 'basic_salary', 'allowances', 'Gross Salary'])
            for row in data:
                gross_salary = int(row[5]) + int(row[6])
                writer.writerow(list(row) + [gross_salary])
            writer.writerow([f'Second Highest Salary={footer["2nd_highest_salary"]}',
                             f'average salary = {footer["average_salary"]}'])
