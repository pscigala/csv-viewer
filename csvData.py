import csv
import unittest


class CSVData(object):

    def __init__(self, filepath, encoding='utf8', delimiter=';', quotechar='"') -> None:
        self.filepath = filepath
        self.encoding = encoding
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.rows = []

        lines = CSVData.read_file_lines(self.filepath, self.encoding)
        reader = csv.reader(lines, delimiter=self.delimiter, quotechar=self.quotechar)

        for i, row in enumerate(reader):
            row = list(map(lambda r: r.strip(), row))
            if i == 0:
                self.header = row
            else:
                self.rows.append(row)

    @staticmethod
    def read_file_lines(filepath, encoding):
        file = open(filepath, encoding=encoding)
        lines = file.readlines()
        file.close()
        return lines

    def get_column(self, header_name: str):
        index = self.header.index(header_name)
        cols = []
        for row in self.rows:
            cols.append(row[index])

        return cols

    def get_column_by_index(self, header_index: int):
        cols = []
        for row in self.rows:
            cols.append(row[header_index])

        return cols

    def pretty_print(self):
        longest = len(max(self.header, key=len))
        for row in self.rows:
            l = len(max(row, key=len))
            if longest < l:
                longest = l

        max_line = (longest + 3) * (len(self.header)) + 1

        pretty = "".rjust(max_line, '-')
        pretty += '\n'
        pretty += '| '
        pretty += '| '.join(list(map(lambda s: str(s).ljust(longest + 1), self.header)))
        pretty += '| '
        pretty += '\n'
        pretty += "".rjust(max_line, '-')
        pretty += '\n'
        for row in self.rows:
            pretty += '| '
            pretty += '| '.join(list(map(lambda s: str(s).ljust(longest + 1), row)))
            pretty += '| '
            pretty += '\n'
            pretty += "".rjust(max_line, '-')
            pretty += '\n'
        return pretty


class CSVDataTest(unittest.TestCase):
    TEST_FILE = 'testfile.csv'
    ENCODING = 'utf-8'

    def test_csv_parse_header(self):
        data = CSVData(filepath=self.TEST_FILE, encoding=self.ENCODING)
        header = data.header

        self.assertEqual('1', header[0])
        self.assertEqual('2', header[1])
        self.assertEqual('3', header[2])
        self.assertEqual('4', header[3])

    def test_csv_parse_rows(self):
        data = CSVData(filepath=self.TEST_FILE, encoding=self.ENCODING)
        rows = data.rows

        self.assertEqual('row1-col1', rows[0][0])
        self.assertEqual('row1-col2', rows[0][1])
        self.assertEqual('row1-col3', rows[0][2])
        self.assertEqual('row1-col4', rows[0][3])

        self.assertEqual('row4-col1', rows[3][0])
        self.assertEqual('row4-col2', rows[3][1])
        self.assertEqual('row4-col3', rows[3][2])
        self.assertEqual('row4-col4', rows[3][3])

    def test_csv_column_by_header_name(self):
        data = CSVData(filepath=self.TEST_FILE, encoding=self.ENCODING)
        column1 = data.get_column('1')
        column4 = data.get_column('4')

        self.assertEqual('row1-col1', column1[0])
        self.assertEqual('row2-col1', column1[1])
        self.assertEqual('row3-col1', column1[2])
        self.assertEqual('row4-col1', column1[3])

        self.assertEqual('row1-col4', column4[0])
        self.assertEqual('row2-col4', column4[1])
        self.assertEqual('row3-col4', column4[2])
        self.assertEqual('row4-col4', column4[3])

    def test_csv_column_by_header_index(self):
        data = CSVData(filepath=self.TEST_FILE, encoding=self.ENCODING)
        column1 = data.get_column_by_index(0)
        column4 = data.get_column_by_index(3)

        self.assertEqual('row1-col1', column1[0])
        self.assertEqual('row2-col1', column1[1])
        self.assertEqual('row3-col1', column1[2])
        self.assertEqual('row4-col1', column1[3])

        self.assertEqual('row1-col4', column4[0])
        self.assertEqual('row2-col4', column4[1])
        self.assertEqual('row3-col4', column4[2])
        self.assertEqual('row4-col4', column4[3])


if __name__ == '__main__':
    unittest.main()
