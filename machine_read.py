import re
import os

def print_machine_read():
    for fil in os.listdir('Source/'):
        with open ('Source/' + fil) as f:
            line_number = 0
            for line in f:
                line_number += 1
                line = line.strip()
                pattern = re.compile(r'[a-zA-Z.-_]+@[a-zA-Z-]+\.\w\w\w?')
                matchers = pattern.finditer(line)
                for match in matchers:
                    file_name = fil
                    print(file_name,line_number,match.start(),match.group(0),sep=':')