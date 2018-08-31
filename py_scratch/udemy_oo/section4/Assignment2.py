from abc import *
import datetime


class WriteFile(ABC):
    def __init__(self, output_file_name):
        self.fh = open(output_file_name, 'w')

    def close(self):
        self.fh.close()

    @staticmethod
    def timestamp():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    @abstractmethod
    def write(self, l):
        return


class LogFile(WriteFile):

    def write(self, msg):
        ts = WriteFile.timestamp()
        self.fh.write(f'{ts} {msg}')


class DelimFile(WriteFile):
    def __init__(self, csv_file_name, delimiter=','):
        WriteFile.__init__(self, csv_file_name)
        self.delimiter = delimiter

    def write(self, l):
        ts = WriteFile.timestamp()
        corrected = ( self.correct_delim_field(e) for e in l )
        msg = self.delimiter.join( corrected )
        self.fh.write(msg)

    def correct_delim_field(self, e):
        if self.delimiter in e:
            return f'"{e}"'
        else:
            return e

