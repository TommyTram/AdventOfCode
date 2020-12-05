

with open('day2/input_day2.txt') as file:
    lines = file.read().splitlines()

rep_count = 0
pos_count = 0
for line in lines:
    div = line.find('-')
    min_rep = int(line[:div])
    space = line.find(' ')
    max_rep = int(line[div+1:space])
    letter = line[space+1]
    code = line[space+4:]

    rep = code.count(letter)

    if rep >= min_rep and rep <= max_rep:
        rep_count += 1

    if code[min_rep-1] == letter and code[max_rep-1] == letter:
        continue
    elif code[min_rep-1] == letter or code[max_rep-1] == letter:
        pos_count += 1

print('policy1 valid passwords: {}'.format(rep_count))
print('policy2 valid passwords: {}'.format(pos_count))