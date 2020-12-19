with open('input.txt', 'r') as input_file:
    homework = [line.strip() for line in input_file.readlines()]

def replace_parentheses(line):
    line = line.replace('(', '((').replace(')', '))')
    line = line.replace('*', ') * (')
    line = '((' + line + '))'

    return line

print(sum([eval(replace_parentheses(line)) for line in homework]))