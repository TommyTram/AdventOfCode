
def find_nr(row_code, total_len):
    candidates = list(range(total_len))
    # BFBBBFF
    for code in row_code:
        split = int(len(candidates)/2)
        if code == 'F' or code == 'L':
            candidates = candidates[:split]
        elif code == 'B' or code ==  'R':
            candidates = candidates[split:]
    
    return candidates[0]

with open('day5/input_day5.txt') as file:
    lines = file.read().splitlines()

max_id = 0
candidate = list(range(928+1))
for code in lines:
    # input BFBBBFFLRL
    row_code = code[:-3] # BFBBBFF
    row = find_nr(row_code, 128)

    col_code = code[-3:] # LRL
    col = find_nr(col_code, 8)
    bording_id = row * 8 + col
    candidate[bording_id] = 0
    max_id = max(bording_id, max_id)
print(max_id)
missing_id = list(filter((0).__ne__, candidate))
print(missing_id)
