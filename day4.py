from data.day4data import datastring
import re

data = [{y.split(':')[0]: y.split(":")[1] for y in x} for x in [re.split(' |\n', d) for d in datastring.split('\n\n')]]

fields = ["byr",
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid",
"cid"]

skipfield = "cid"
approved = 0
print(len(data))


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def validator(k, v) -> bool:

    if k == 'byr' and bool(re.match('[0-9]{4}$', v)) == True and 1920 <= int(re.sub("[^0-9]","", v)) <= 2002:
        return True
    elif k == 'iyr' and bool(re.match('[0-9]{4}$', v)) == True and 2010 <= int(re.sub("[^0-9]","", v)) <= 2020:
        return True
    elif k == 'eyr' and bool(re.match('[0-9]{4}$', v)) == True and 2020 <= int(re.sub("[^0-9]","", v)) <= 2030:
        return True
    elif k == 'hgt' and bool(re.match('\d+cm', v)) == True and 150 <= int(re.sub("[^0-9]","", v)) <= 193:
        return True
    elif k == 'hgt' and bool(re.match('\d+in', v)) == True and 59 <= int(re.sub("[^0-9]","", v)) <= 76:
        return True
    elif k == 'hcl' and bool(re.match('#[0-9a-f]{6}$', v)) == True:
        return True
    elif k == 'ecl' and bool(re.match('(amb|blu|brn|gry|grn|hzl|oth)', v)) == True:
        return True
    elif k == 'pid' and bool(re.match('^[0-9]{9}$', v)) == True:
        return True
    else:
        return False


#answer 2, I already overwrote answer 1..
for d in data:
    # check for fields that match the required fields.
    testlist = [f for f in fields if f != skipfield]
    for k, v in d.items():
        if validator(k, v) is True:
            testlist = [f for f in testlist if f != k]

    if len(testlist) == 0:
        approved += 1

print(approved)




