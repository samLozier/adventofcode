"""
Each line gives the password policy and then the password. 
The password policy indicates the lowest and highest number of 
times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at 
least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, 
cdefg, is not; it contains no instances of b, but needs at least 1.
 The first and third passwords are valid: they contain one a or nine c, 
 both within the limits of their respective policies.
"""
from data.day2data import datastring
data = [
    {
        "range": tuple(int(i) for i in d[0].split("-")),
        "letter": d[1].strip(":"),
        "pw": d[2],
    }
    for d in [d.split(" ") for d in datastring.split("\n")]
]

valid = 0
for d in data:
    if d["range"][0] <= d["pw"].count(d["letter"]) <= d["range"][1]:
        valid += 1
print(valid)


"""Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
"""
valid2 = 0
for d in data:
    if d["pw"][d["range"][0] - 1] != d["pw"][d["range"][1] - 1] and (
        d["pw"][d["range"][0] - 1] == d["letter"]
        or d["pw"][d["range"][1] - 1] == d["letter"]
    ):
        valid2 += 1

print(valid2)
