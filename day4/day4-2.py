import re

def validate_passport(passport):
    try:
        assert 1920 <= int(passport['byr']) <= 2002
        assert 2010 <= int(passport['iyr']) <= 2020
        assert 2020 <= int(passport['eyr']) <= 2030

        height, unit = re.match(r'^(\d+)(cm|in)$', passport['hgt']).groups()
        if unit == 'cm':
            assert 150 <= int(height) <= 193
        if unit == 'in':
            assert 59 <= int(height) <= 76

        assert re.match(r'^#[a-f0-9]{6}$', passport['hcl'])
        assert passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        assert re.match(r'^\d{9}$', passport['pid'])
    except:
        return False

    return True


with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in  input_file.readlines()]

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

valid_passports = [p for p in passports if validate_passport(p)]   

print(len(valid_passports))