import re
import os

def get_results_basic_list():
    results = ""
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
                    result = "{} {} {}\n".format(file_name, line, line_number)
                    results += result
    return results