import re
import os

def print_circumflex_under():
    for fil in os.listdir('Source/'):
        with open ('Source/' + fil) as f:
            line_number = 0
            for line in f:
                line_number += 1
                line = line.strip()
                pattern = re.compile(r'[a-zA-Z.-_]+@[a-zA-Z-]+\.\w.')
                matchers = pattern.finditer(line)
                for match in matchers:
                    file_name = fil
                    start_of_string = match.start()+len(file_name)-1
                    print(file_name, line, line_number,'\n',' '*start_of_string,'^')