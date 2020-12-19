with open('input.txt', 'r') as input_file:
    homework = [line.strip() for line in input_file.readlines()]

def replace_parentheses(line):
    num = len([c for c in line if c in '+*'])
    line = line.replace('(', num * '(').replace(')', num * ')')
    line = line.replace('+', ') +').replace('*', ') *')
    line = num * '(' + line

    return line

print(sum([eval(replace_parentheses(line)) for line in homework]))