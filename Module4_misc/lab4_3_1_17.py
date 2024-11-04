'''Lab for PCAP 4.3.1.17 @ 2024-10-25'''
class StudentsDataException(Exception):
    def __init__(self, message:str):
        super().__init__()
        self.message = message
        this_class = self.__class__
        if this_class is StudentsDataException:
            raise TypeError(f'Cannot instantiate abstract class {this_class}.')

class BadLine(StudentsDataException):
    def __init__(self, line:str, message:str=''):
        super().__init__(message)
        self.line = line
    def print_error(self) -> None:
        print(f'{self.message} Line:\n{self.line}')

class FileEmpty(StudentsDataException):
    def __init__(self, message:str=''):
        super().__init__(message)

def extract_file_contents(file_name:str) -> str:
    try:
        with open(file_name, mode='rt') as file_stream:
            file_contents = file_stream.read()
    except FileNotFoundError:
        with open(file_name, mode='wt') as file_stream:
            file_stream.write('')
        with open(file_name, mode='rt') as file_stream:
            file_contents = file_stream.read()
    finally:
        return file_contents

def process_line(line:str) -> tuple:
    words = line.split()
    try:
        assert len(words) == 3
        points = float(words[2])
        name = f'{words[0]} {words[1]}'
        return name, points
    except AssertionError:
        raise BadLine(line, 'Bad line: it should contain 3 entities separated by spaces.')
    except ValueError:
        raise BadLine(line, 'Bad line: contains invalid point value.')

def count_student_pts(file_data:str) -> dict:
    student_points = dict()
    lines = file_data.split('\n')
    if lines in [[], ['']]:
        raise FileEmpty('The file is empty.')
    for line in lines:
        name, points = process_line(line)
        student_points[name] = student_points.get(name,0) + points
    return student_points

def generate_report(data:dict) -> str:
    return '\n'.join([f'{name}\t{data[name]}' for name in sorted(data.keys())])

def main() -> None:
    try:
        file_name = input('Enter file name: ')
        contents = extract_file_contents(file_name)
        point_dict = count_student_pts(contents)
        report = generate_report(point_dict)
        print(report)
    except BadLine as e:
        e.print_error()
    except FileEmpty as e:
        print(e)

if __name__ == '__main__':
    main()
