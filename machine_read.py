import re
import os

def get_results_by_machine_read():
    results = ""
    file_names = os.listdir('Source/')
    file_names.sort()
    for fil in file_names:
        with open ('Source/' + fil) as f:
            line_number = 0
            for line in f:
                line_number += 1
                line = line.strip()
                pattern = re.compile(r'[a-zA-Z.-_]+@[a-zA-Z-]+\.\w\w\w?')
                matchers = pattern.finditer(line)
                for match in matchers:
                    file_name = fil
                    result = "{}:{}:{}:{}\n".format(file_name,line_number,match.start(),match.group(0))
                    results += result
    return results