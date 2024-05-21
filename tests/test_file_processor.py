import os
import csv
import unittest
from src.file_processor import FileProcessor


class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        self.input_folder = 'input\\unittest'
        self.output_folder = 'input\\unittest'
        self.sample_data = [
            ('30462', 'Chaddy', 'Lassen', 'classen0@cocolog-nifty.com', 'Physical Therapy Assistant', '7958', '1502'),
            ('30563', 'Clarine', 'Denerley', 'cdenerley1@blogger.com', 'Senior Developer', '9024', '816'),
            ('30312', 'Christina', 'Geroldini', 'cgeroldini2@ca.gov', 'Occupational Therapist', '5476', '1252'),
            ('30449', 'Royall', 'Juza', 'rjuza3@nationalgeographic.com', 'Editor', '5380', '1821'),
            ('30826', 'Alaster', 'Bidnall', 'abidnall4@indiatimes.com', 'Data Coordiator', '3171', '1070'),
            ('30826', 'Adaline', 'Bowgen', 'abowgen5@stumbleupon.com', 'Cost Accountant', '5895', '1298')
        ]

    def test_read_files_from_folder(self):
        # This test requires the presence of actual files in the 'input/unittest' folder
        data = FileProcessor.read_files_from_folder(self.input_folder)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_process_data(self):
        unique_data = FileProcessor.process_data(self.sample_data)
        self.assertEqual(len(unique_data), 6)  # Ensure duplicates are removed

    def test_calculate_footer(self):
        salaries = [int(row[5]) + int(row[6]) for row in self.sample_data]
        footer = FileProcessor.calculate_footer(salaries)
        self.assertEqual(footer['2nd_highest_salary'], 9460)  # Second highest gross salary
        self.assertAlmostEqual(footer['average_salary'], 7443.83, places=2)  # Average gross salary

    def test_write_to_csv(self):
        output_file_path = os.path.join(self.output_folder, 'test_result.csv')
        footer = {'2nd_highest_salary': 9460, 'average_salary': 7443.83}
        FileProcessor.write_to_csv(output_file_path, self.sample_data, footer)

        with open(output_file_path, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            rows = list(reader)

        # Check the header
        self.assertEqual(rows[-1], [f'Second Highest Salary={footer["2nd_highest_salary"]}',
                                    f'average salary = {footer["average_salary"]}'])


if __name__ == '__main__':
    unittest.main()
