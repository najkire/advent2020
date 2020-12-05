REQUIRED_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

passports = []
passport = []
for line in lines:
    if line == '' and passport:
        passports += [dict([f.split(':') for f in passport])]
        passport = []
        continue
    passport += line.split()
else:
    passports += [dict([f.split(':') for f in passport])]

valid_passports = [p for p in passports if set(p.keys()).issuperset(REQUIRED_FIELDS)]   

print(len(valid_passports))