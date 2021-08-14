import re
import os

def print_line():
    for fil in os.listdir('Source/'):
        with open ('Source/' + fil) as f:
            line_number = 0
            list_of_results = []
            for line in f:
                line_number += 1
                line = line.strip()
                pattern = re.compile(r'[a-zA-Z.-_]+@[a-zA-Z-]+\.\w.')
                matchers = pattern.finditer(line)
                for match in matchers:
                    list_of_results.append((f.name, line, line_number))
                    print(f.name, line, line_number)