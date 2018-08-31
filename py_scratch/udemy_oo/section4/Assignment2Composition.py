from abc import *
import datetime


class WriteFile:
    def __init__(self, writer_class, output_file_path):
        self.writer = writer_class(output_file_path)

    def write(self, x):
        self.writer.write(x)

    def close(self):
        self.writer.close()


class Base(ABC):
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


class LogFile(Base):
    def __init__(self, log_file_name):
        Base.__init__(self, log_file_name)

    def write(self, msg):
        ts = Base.timestamp()
        self.fh.write(f'{ts} {msg}')


class DelimFile(Base):
    def __init__(self, csv_file_name, delimiter=','):
        Base.__init__(self, csv_file_name)
        self.delimiter = delimiter

    def write(self, l):
        ts = Base.timestamp()
        msg = self.delimiter.join([
            self.correct_delim_field(e)
            for e in l
        ])
        self.fh.write(f'{ts} {msg}')

    def correct_delim_field(self, e):
        if self.delimiter in e :
            return f'"{e}"'
        else:
            return e

