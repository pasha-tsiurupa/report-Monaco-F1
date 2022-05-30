import unittest
from unittest import TestCase
from unittest.mock import patch
import report.report
from report.report import *
import os
from io import StringIO
import datetime


class TestReport(TestCase):
    def test_data_from_file(self):
        expected_result = {'SVF': datetime.datetime(2018, 5, 24, 12, 2, 58, 917000),
                           'NHR': datetime.datetime(2018, 5, 24, 12, 2, 49, 914000),
                           'FAM': datetime.datetime(2018, 5, 24, 12, 13, 4, 512000),
                           'KRF': datetime.datetime(2018, 5, 24, 12, 3, 1, 250000),
                           'SVM': datetime.datetime(2018, 5, 24, 12, 18, 37, 735000),
                           'MES': datetime.datetime(2018, 5, 24, 12, 4, 45, 513000),
                           'LSW': datetime.datetime(2018, 5, 24, 12, 6, 13, 511000),
                           'BHS': datetime.datetime(2018, 5, 24, 12, 14, 51, 985000),
                           'EOF': datetime.datetime(2018, 5, 24, 12, 17, 58, 810000),
                           'RGH': datetime.datetime(2018, 5, 24, 12, 5, 14, 511000),
                           'SSW': datetime.datetime(2018, 5, 24, 12, 16, 11, 648000),
                           'KMH': datetime.datetime(2018, 5, 24, 12, 2, 51, 3000),
                           'PGS': datetime.datetime(2018, 5, 24, 12, 7, 23, 645000),
                           'CSR': datetime.datetime(2018, 5, 24, 12, 3, 15, 145000),
                           'SPF': datetime.datetime(2018, 5, 24, 12, 12, 1, 35000),
                           'DRR': datetime.datetime(2018, 5, 24, 12, 14, 12, 54000),
                           'LHM': datetime.datetime(2018, 5, 24, 12, 18, 20, 125000),
                           'CLS': datetime.datetime(2018, 5, 24, 12, 9, 41, 921000),
                           'VBM': datetime.datetime(2018, 5, 24, 12, 0)}
        file_path = os.path.join(os.path.dirname(__file__), '../data_files/start.log')
        actual_result = data_from_file(file_path)
        self.assertEqual(actual_result, expected_result)

    def test_get_abbreviations(self):
        expected_result = {'DRR': ['Daniel Ricciardo', 'RED BULL RACING TAG HEUER'],
                           'SVF': ['Sebastian Vettel', 'FERRARI'],
                           'LHM': ['Lewis Hamilton', 'MERCEDES'],
                           'KRF': ['Kimi Räikkönen', 'FERRARI'],
                           'VBM': ['Valtteri Bottas', 'MERCEDES'],
                           'EOF': ['Esteban Ocon', 'FORCE INDIA MERCEDES'],
                           'FAM': ['Fernando Alonso', 'MCLAREN RENAULT'],
                           'CSR': ['Carlos Sainz', 'RENAULT'],
                           'SPF': ['Sergio Perez', 'FORCE INDIA MERCEDES'],
                           'PGS': ['Pierre Gasly', 'SCUDERIA TORO ROSSO HONDA'],
                           'NHR': ['Nico Hulkenberg', 'RENAULT'],
                           'SVM': ['Stoffel Vandoorne', 'MCLAREN RENAULT'],
                           'SSW': ['Sergey Sirotkin', 'WILLIAMS MERCEDES'],
                           'CLS': ['Charles Leclerc', 'SAUBER FERRARI'],
                           'RGH': ['Romain Grosjean', 'HAAS FERRARI'],
                           'BHS': ['Brendon Hartley', 'SCUDERIA TORO ROSSO HONDA'],
                           'MES': ['Marcus Ericsson', 'SAUBER FERRARI'],
                           'LSW': ['Lance Stroll', 'WILLIAMS MERCEDES'],
                           'KMH': ['Kevin Magnussen', 'HAAS FERRARI']}
        folder_path = os.path.join(os.path.dirname(__file__), '../data_files')
        actual_result = get_abbreviations(folder_path)
        self.assertEqual(actual_result, expected_result)

    def test_build_report(self):
        folder_path = os.path.join(os.path.dirname(__file__), '../data_files')
        actual_result = build_report(folder_path)
        expected_result = {'Sebastian Vettel': [1, 'FERRARI', '0:01:04.415000'],
                           'Valtteri Bottas': [2, 'MERCEDES', '0:01:12.434000'],
                           'Stoffel Vandoorne': [3, 'MCLAREN RENAULT', '0:01:12.463000'],
                           'Kimi Räikkönen': [4, 'FERRARI', '0:01:12.639000'],
                           'Fernando Alonso': [5, 'MCLAREN RENAULT', '0:01:12.657000'],
                           'Charles Leclerc': [6, 'SAUBER FERRARI', '0:01:12.829000'],
                           'Sergio Perez': [7, 'FORCE INDIA MERCEDES', '0:01:12.848000'],
                           'Romain Grosjean': [8, 'HAAS FERRARI', '0:01:12.930000'],
                           'Pierre Gasly': [9, 'SCUDERIA TORO ROSSO HONDA', '0:01:12.941000'],
                           'Carlos Sainz': [10, 'RENAULT', '0:01:12.950000'],
                           'Nico Hulkenberg': [11, 'RENAULT', '0:01:13.065000'],
                           'Brendon Hartley': [12, 'SCUDERIA TORO ROSSO HONDA', '0:01:13.179000'],
                           'Marcus Ericsson': [13, 'SAUBER FERRARI', '0:01:13.265000'],
                           'Lance Stroll': [14, 'WILLIAMS MERCEDES', '0:01:13.323000'],
                           'Kevin Magnussen': [15, 'HAAS FERRARI', '0:01:13.393000'],
                           'Daniel Ricciardo': [16, 'RED BULL RACING TAG HEUER', 'None'],
                           'Lewis Hamilton': [17, 'MERCEDES', 'None'],
                           'Esteban Ocon': [18, 'FORCE INDIA MERCEDES', 'None'],
                           'Sergey Sirotkin': [19, 'WILLIAMS MERCEDES', 'None']}
        self.assertEqual(actual_result, expected_result)

    def test_print_report(self):
        expected_result = (' 1.Sebastian Vettel  | FERRARI                   | 0:01:04.415000\n'
                           ' 2.Valtteri Bottas   | MERCEDES                  | 0:01:12.434000\n'
                           ' 3.Stoffel Vandoorne | MCLAREN RENAULT           | 0:01:12.463000\n'
                           ' 4.Kimi Räikkönen    | FERRARI                   | 0:01:12.639000\n'
                           ' 5.Fernando Alonso   | MCLAREN RENAULT           | 0:01:12.657000\n'
                           ' 6.Charles Leclerc   | SAUBER FERRARI            | 0:01:12.829000\n'
                           ' 7.Sergio Perez      | FORCE INDIA MERCEDES      | 0:01:12.848000\n'
                           ' 8.Romain Grosjean   | HAAS FERRARI              | 0:01:12.930000\n'
                           ' 9.Pierre Gasly      | SCUDERIA TORO ROSSO HONDA | 0:01:12.941000\n'
                           '10.Carlos Sainz      | RENAULT                   | 0:01:12.950000\n'
                           '11.Nico Hulkenberg   | RENAULT                   | 0:01:13.065000\n'
                           '12.Brendon Hartley   | SCUDERIA TORO ROSSO HONDA | 0:01:13.179000\n'
                           '13.Marcus Ericsson   | SAUBER FERRARI            | 0:01:13.265000\n'
                           '14.Lance Stroll      | WILLIAMS MERCEDES         | 0:01:13.323000\n'
                           '15.Kevin Magnussen   | HAAS FERRARI              | 0:01:13.393000\n'
                           '-----------------------------------------------------------------\n'
                           '16.Daniel Ricciardo  | RED BULL RACING TAG HEUER | None\n'
                           '17.Lewis Hamilton    | MERCEDES                  | None\n'
                           '18.Esteban Ocon      | FORCE INDIA MERCEDES      | None\n'
                           '19.Sergey Sirotkin   | WILLIAMS MERCEDES         | None\n')

        folder_path = os.path.join(os.path.dirname(__file__), '../data_files')
        with patch('sys.stdout', new=StringIO()) as output:
            print_report(folder_path, True)
            self.assertEqual(output.getvalue(), expected_result)

    def test_desc_report(self):
        expected_result = ('19.Sergey Sirotkin   | WILLIAMS MERCEDES         | None\n'
                           '18.Esteban Ocon      | FORCE INDIA MERCEDES      | None\n'
                           '17.Lewis Hamilton    | MERCEDES                  | None\n'
                           '16.Daniel Ricciardo  | RED BULL RACING TAG HEUER | None\n'
                           '-----------------------------------------------------------------\n'
                           '15.Kevin Magnussen   | HAAS FERRARI              | 0:01:13.393000\n'
                           '14.Lance Stroll      | WILLIAMS MERCEDES         | 0:01:13.323000\n'
                           '13.Marcus Ericsson   | SAUBER FERRARI            | 0:01:13.265000\n'
                           '12.Brendon Hartley   | SCUDERIA TORO ROSSO HONDA | 0:01:13.179000\n'
                           '11.Nico Hulkenberg   | RENAULT                   | 0:01:13.065000\n'
                           '10.Carlos Sainz      | RENAULT                   | 0:01:12.950000\n'
                           ' 9.Pierre Gasly      | SCUDERIA TORO ROSSO HONDA | 0:01:12.941000\n'
                           ' 8.Romain Grosjean   | HAAS FERRARI              | 0:01:12.930000\n'
                           ' 7.Sergio Perez      | FORCE INDIA MERCEDES      | 0:01:12.848000\n'
                           ' 6.Charles Leclerc   | SAUBER FERRARI            | 0:01:12.829000\n'
                           ' 5.Fernando Alonso   | MCLAREN RENAULT           | 0:01:12.657000\n'
                           ' 4.Kimi Räikkönen    | FERRARI                   | 0:01:12.639000\n'
                           ' 3.Stoffel Vandoorne | MCLAREN RENAULT           | 0:01:12.463000\n'
                           ' 2.Valtteri Bottas   | MERCEDES                  | 0:01:12.434000\n'
                           ' 1.Sebastian Vettel  | FERRARI                   | 0:01:04.415000\n')

        folder_path = os.path.join(os.path.dirname(__file__), '../data_files')
        with patch('sys.stdout', new=StringIO()) as output:
            print_report(folder_path, False)
            self.assertEqual(output.getvalue(), expected_result)

    def test_get_racer_info(self):
        testcases = [
            ('Daniel Ricciardo', 'Daniel Ricciardo | RED BULL RACING TAG HEUER | None'),
            ('Sebastian Vettel', 'Sebastian Vettel | FERRARI | 0:01:04.415000'),
            ('Lewis Hamilton', 'Lewis Hamilton | MERCEDES | None')
        ]
        path = os.path.join(os.path.dirname(__file__), '../data_files')
        for name, result in testcases:
            self.assertEqual(report.get_racer_info(path, name), result)


class TestParser(TestCase):

    def test_parse_files(self):
        path = os.path.join(os.path.dirname(__file__), '../data_files')
        args = report.parse_args(['--files', path])
        self.assertEqual(args.files, path)

    def test_parse_driver(self):
        args = report.parse_args(['--driver', 'Sergio Perez'])
        self.assertEqual(args.driver, 'Sergio Perez')

    def test_parse_asc(self):
        args = report.parse_args(['--asc'])
        self.assertEqual(args.order, 'asc')

    def test_parse_desc(self):
        args = report.parse_args(['--desc'])
        self.assertEqual(args.order, 'desc')


if __name__ == "__main__":
    unittest.main()
