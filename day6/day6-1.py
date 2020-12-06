def answers():
    with open('input.txt', 'r') as input_file:
        answers = [line.strip() for line in input_file.readlines()] + ['']

    group_answers = set()
    for line in answers:
        if line:
            group_answers.update(line)
        if line == '' and group_answers:
            yield group_answers
            group_answers = set()

count = sum(len(g) for g in answers())
print(count)