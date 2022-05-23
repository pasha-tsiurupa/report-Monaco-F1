import unittest
from unittest import TestCase
from unittest.mock import Mock, patch, mock_open
import report.report
from report.report import *
import os
from io import StringIO


class TestReport(TestCase):
    def test_data_from_file(self):
        mock = Mock()
        mock.data_from_file.return_value = {'SVF': datetime.datetime(2018, 5, 24, 12, 2, 58, 917000),
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
        file_path = os.path.join(os.path.dirname(__file__))
        with patch('builtins.open', mock_open(read_data='SVF2018-05-24_12:02:58.917\n'
                                                        'NHR2018-05-24_12:02:49.914\n'
                                                        'FAM2018-05-24_12:13:04.512\n'
                                                        'KRF2018-05-24_12:03:01.250\n'
                                                        'SVM2018-05-24_12:18:37.735\n'
                                                        'MES2018-05-24_12:04:45.513\n'
                                                        'LSW2018-05-24_12:06:13.511\n'
                                                        'BHS2018-05-24_12:14:51.985\n'
                                                        'EOF2018-05-24_12:17:58.810\n'
                                                        'RGH2018-05-24_12:05:14.511\n'
                                                        'SSW2018-05-24_12:16:11.648\n'
                                                        'KMH2018-05-24_12:02:51.003\n'
                                                        'PGS2018-05-24_12:07:23.645\n'
                                                        'CSR2018-05-24_12:03:15.145\n'
                                                        'SPF2018-05-24_12:12:01.035\n'
                                                        'DRR2018-05-24_12:14:12.054\n'
                                                        'LHM2018-05-24_12:18:20.125\n'
                                                        'CLS2018-05-24_12:09:41.921\n'
                                                        'VBM2018-05-24_12:00:00.000\n')):
            actual_result = data_from_file(file_path)
        self.assertEqual(actual_result, mock.data_from_file.return_value)

    def test_get_abbreviations(self):
        mock = Mock()
        mock.get_abbreviations.return_value = {'DRR': 'Daniel Ricciardo, RED BULL RACING TAG HEUER',
                                               'SVF': 'Sebastian Vettel, FERRARI',
                                               'LHM': 'Lewis Hamilton, MERCEDES',
                                               'KRF': 'Kimi Räikkönen, FERRARI',
                                               'VBM': 'Valtteri Bottas, MERCEDES',
                                               'EOF': 'Esteban Ocon, FORCE INDIA MERCEDES',
                                               'FAM': 'Fernando Alonso, MCLAREN RENAULT',
                                               'CSR': 'Carlos Sainz, RENAULT',
                                               'SPF': 'Sergio Perez, FORCE INDIA MERCEDES',
                                               'PGS': 'Pierre Gasly, SCUDERIA TORO ROSSO HONDA',
                                               'NHR': 'Nico Hulkenberg, RENAULT',
                                               'SVM': 'Stoffel Vandoorne, MCLAREN RENAULT',
                                               'SSW': 'Sergey Sirotkin, WILLIAMS MERCEDES',
                                               'CLS': 'Charles Leclerc, SAUBER FERRARI',
                                               'RGH': 'Romain Grosjean, HAAS FERRARI',
                                               'BHS': 'Brendon Hartley, SCUDERIA TORO ROSSO HONDA',
                                               'MES': 'Marcus Ericsson, SAUBER FERRARI',
                                               'LSW': 'Lance Stroll, WILLIAMS MERCEDES',
                                               'KMH': 'Kevin Magnussen, HAAS FERRARI'}
        folder_path = os.path.join(os.path.dirname(__file__))
        with patch('builtins.open', mock_open(read_data='DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER\n'
                                                        'SVF_Sebastian Vettel_FERRARI\n'
                                                        'LHM_Lewis Hamilton_MERCEDES\n'
                                                        'KRF_Kimi Räikkönen_FERRARI\n'
                                                        'VBM_Valtteri Bottas_MERCEDES\n'
                                                        'EOF_Esteban Ocon_FORCE INDIA MERCEDES\n'
                                                        'FAM_Fernando Alonso_MCLAREN RENAULT\n'
                                                        'CSR_Carlos Sainz_RENAULT\n'
                                                        'SPF_Sergio Perez_FORCE INDIA MERCEDES\n'
                                                        'PGS_Pierre Gasly_SCUDERIA TORO ROSSO HONDA\n'
                                                        'NHR_Nico Hulkenberg_RENAULT\n'
                                                        'SVM_Stoffel Vandoorne_MCLAREN RENAULT\n'
                                                        'SSW_Sergey Sirotkin_WILLIAMS MERCEDES\n'
                                                        'CLS_Charles Leclerc_SAUBER FERRARI\n'
                                                        'RGH_Romain Grosjean_HAAS FERRARI\n'
                                                        'BHS_Brendon Hartley_SCUDERIA TORO ROSSO HONDA\n'
                                                        'MES_Marcus Ericsson_SAUBER FERRARI\n'
                                                        'LSW_Lance Stroll_WILLIAMS MERCEDES\n'
                                                        'KMH_Kevin Magnussen_HAAS FERRARI')):
            actual_result = get_abbreviations(folder_path)
        self.assertEqual(actual_result, mock.get_abbreviations.return_value)

    def test_build_report(self):
        folder_path = os.path.join(os.path.dirname(__file__), '../data_files')
        actual_result = build_report(folder_path)
        expected_result = ['Sebastian Vettel  | FERRARI                   | 0:01:04.415000',
                           'Valtteri Bottas   | MERCEDES                  | 0:01:12.434000',
                           'Stoffel Vandoorne | MCLAREN RENAULT           | 0:01:12.463000',
                           'Kimi Räikkönen    | FERRARI                   | 0:01:12.639000',
                           'Fernando Alonso   | MCLAREN RENAULT           | 0:01:12.657000',
                           'Charles Leclerc   | SAUBER FERRARI            | 0:01:12.829000',
                           'Sergio Perez      | FORCE INDIA MERCEDES      | 0:01:12.848000',
                           'Romain Grosjean   | HAAS FERRARI              | 0:01:12.930000',
                           'Pierre Gasly      | SCUDERIA TORO ROSSO HONDA | 0:01:12.941000',
                           'Carlos Sainz      | RENAULT                   | 0:01:12.950000',
                           'Nico Hulkenberg   | RENAULT                   | 0:01:13.065000',
                           'Brendon Hartley   | SCUDERIA TORO ROSSO HONDA | 0:01:13.179000',
                           'Marcus Ericsson   | SAUBER FERRARI            | 0:01:13.265000',
                           'Lance Stroll      | WILLIAMS MERCEDES         | 0:01:13.323000',
                           'Kevin Magnussen   | HAAS FERRARI              | 0:01:13.393000',
                           'Daniel Ricciardo  | RED BULL RACING TAG HEUER | 0:02:47.987000',
                           'Sergey Sirotkin   | WILLIAMS MERCEDES         | 0:04:47.294000',
                           'Esteban Ocon      | FORCE INDIA MERCEDES      | 0:05:46.972000',
                           'Lewis Hamilton    | MERCEDES                  | 0:06:47.540000']
        self.assertEqual(actual_result, expected_result)

    def test_print_report(self):
        expected_result = ('1 Sebastian Vettel  | FERRARI                   | 0:01:04.415000\n'
                           '2 Valtteri Bottas   | MERCEDES                  | 0:01:12.434000\n'
                           '3 Stoffel Vandoorne | MCLAREN RENAULT           | 0:01:12.463000\n'
                           '4 Kimi Räikkönen    | FERRARI                   | 0:01:12.639000\n'
                           '5 Fernando Alonso   | MCLAREN RENAULT           | 0:01:12.657000\n'
                           '6 Charles Leclerc   | SAUBER FERRARI            | 0:01:12.829000\n'
                           '7 Sergio Perez      | FORCE INDIA MERCEDES      | 0:01:12.848000\n'
                           '8 Romain Grosjean   | HAAS FERRARI              | 0:01:12.930000\n'
                           '9 Pierre Gasly      | SCUDERIA TORO ROSSO HONDA | 0:01:12.941000\n'
                           '10 Carlos Sainz      | RENAULT                   | 0:01:12.950000\n'
                           '11 Nico Hulkenberg   | RENAULT                   | 0:01:13.065000\n'
                           '12 Brendon Hartley   | SCUDERIA TORO ROSSO HONDA | 0:01:13.179000\n'
                           '13 Marcus Ericsson   | SAUBER FERRARI            | 0:01:13.265000\n'
                           '14 Lance Stroll      | WILLIAMS MERCEDES         | 0:01:13.323000\n'
                           '15 Kevin Magnussen   | HAAS FERRARI              | 0:01:13.393000\n'
                           '-----------------------------------------------------------------\n'
                           '16 Daniel Ricciardo  | RED BULL RACING TAG HEUER | 0:02:47.987000\n'
                           '17 Sergey Sirotkin   | WILLIAMS MERCEDES         | 0:04:47.294000\n'
                           '18 Esteban Ocon      | FORCE INDIA MERCEDES      | 0:05:46.972000\n'
                           '19 Lewis Hamilton    | MERCEDES                  | 0:06:47.540000\n')
        folder_path = os.path.join(os.path.dirname(__file__), '../data_files')
        with patch('sys.stdout', new=StringIO()) as output:
            print_report(folder_path)
            self.assertEqual(output.getvalue(), expected_result)

    def test_desc_report(self):
        expected_result = ('19 Lewis Hamilton    | MERCEDES                  | 0:06:47.540000\n'
                           '18 Esteban Ocon      | FORCE INDIA MERCEDES      | 0:05:46.972000\n'
                           '17 Sergey Sirotkin   | WILLIAMS MERCEDES         | 0:04:47.294000\n'
                           '16 Daniel Ricciardo  | RED BULL RACING TAG HEUER | 0:02:47.987000\n'
                           '-----------------------------------------------------------------\n'
                           '15 Kevin Magnussen   | HAAS FERRARI              | 0:01:13.393000\n'
                           '14 Lance Stroll      | WILLIAMS MERCEDES         | 0:01:13.323000\n'
                           '13 Marcus Ericsson   | SAUBER FERRARI            | 0:01:13.265000\n'
                           '12 Brendon Hartley   | SCUDERIA TORO ROSSO HONDA | 0:01:13.179000\n'
                           '11 Nico Hulkenberg   | RENAULT                   | 0:01:13.065000\n'
                           '10 Carlos Sainz      | RENAULT                   | 0:01:12.950000\n'
                           '9 Pierre Gasly      | SCUDERIA TORO ROSSO HONDA | 0:01:12.941000\n'
                           '8 Romain Grosjean   | HAAS FERRARI              | 0:01:12.930000\n'
                           '7 Sergio Perez      | FORCE INDIA MERCEDES      | 0:01:12.848000\n'
                           '6 Charles Leclerc   | SAUBER FERRARI            | 0:01:12.829000\n'
                           '5 Fernando Alonso   | MCLAREN RENAULT           | 0:01:12.657000\n'
                           '4 Kimi Räikkönen    | FERRARI                   | 0:01:12.639000\n'
                           '3 Stoffel Vandoorne | MCLAREN RENAULT           | 0:01:12.463000\n'
                           '2 Valtteri Bottas   | MERCEDES                  | 0:01:12.434000\n'
                           '1 Sebastian Vettel  | FERRARI                   | 0:01:04.415000\n')
        folder_path = os.path.join(os.path.dirname(__file__), '../data_files')
        args = ['--files', folder_path, '--desc']
        with patch('sys.stdout', new=StringIO()) as output:
            report.report.main(args)
            self.assertEqual(output.getvalue(), expected_result)

    def test_driver_stats(self):
        testcases = [
            ('Daniel Ricciardo', 'Daniel Ricciardo  | RED BULL RACING TAG HEUER | 0:02:47.987000\n'),
            ('Sebastian Vettel', 'Sebastian Vettel  | FERRARI                   | 0:01:04.415000\n'),
            ('Lewis Hamilton', 'Lewis Hamilton    | MERCEDES                  | 0:06:47.540000\n')
        ]

        folder_path = os.path.join(os.path.dirname(__file__), '../data_files')
        for driver, expected_result in testcases:
            args = ['--files', folder_path, '--driver', driver]
            with patch('sys.stdout', new=StringIO()) as output:
                report.report.main(args)
                self.assertEqual(output.getvalue(), expected_result)


if __name__ == "__main__":
    unittest.main()
