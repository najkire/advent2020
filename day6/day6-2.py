def answers():
    with open('input.txt', 'r') as input_file:
        answers = [line.strip() for line in input_file.readlines()] + ['']

    group_answers = []
    for line in answers:
        if line:
            group_answers += [set(line)]
        if line == '' and group_answers:
            yield set.intersection(*group_answers)
            group_answers = []

count = sum(len(g) for g in answers())
print(count)