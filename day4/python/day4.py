#!/usr/bin/env python3
from os.path import dirname, realpath, join
import time, pytest, re

def find_key(line):
  key_len = 3
  space = line.find(' ')
  

def transform_input(input_):
  # custom transform for the day
  new_input = list()
  lines = input_.splitlines()
  passport = dict()
  key_len = 3
  for line in lines:
    if line == '':
      new_input.append(passport)
      passport = dict()
      continue

    index_list = [space.start() for space in re.finditer(' ', line)]
    index_list.append(len(line))
    i = 0
    for next_index in index_list:
      value_index = i+key_len+1
      key = line[i:i+key_len]
      value = line[value_index:next_index]
      passport.update({key:value})
      i = next_index + 1
  new_input.append(passport)

  return new_input


def read_input(file_name = '../data/input.txt'):
  dir_path = dirname(realpath(__file__))
  with open(join(dir_path,file_name), 'r') as f:
    input_ = transform_input(f.read())

  return input_

def solve_part1(input_):
  valid_count = 0
  valid_passports = list()
  for passport in input_:
    if len(passport.keys()) == 8:
      valid_count += 1
      valid_passports.append(passport)
    elif len(passport.keys()) == 7 and all (k in passport for k in ("byr","iyr","eyr","hgt","hcl","ecl","pid")):
      valid_count += 1
      valid_passports.append(passport)
   
  return valid_count, valid_passports


def solve_part2(input_):
  count = 0
  for passport in input_:
    byr = passport.get('byr')
    byr_ok = len(byr)==4 and int(byr)>=1920 and int(byr)<=2002

    iyr = passport.get('iyr')
    iyr_ok = len(iyr)==4 and int(iyr)>=2010 and int(iyr)<=2020

    eyr = passport.get('eyr')
    eyr_ok = len(eyr)==4 and int(eyr)>=2020 and int(eyr)<=2030

    hgt = passport.get('hgt')
    unit = hgt[-2:]
    hgt_ok = False
    if not unit.isnumeric():
      value = int(hgt[:-2])
      if unit == 'cm': 
        hgt_ok = value >= 150 and value <= 193
      elif unit == 'in': 
        hgt_ok = value >= 59 and value <= 76

    hcl = passport.get('hcl')
    hcl_ok = hcl[0] == '#' and len(hcl[1:])==6
    
    ecl = passport.get('ecl')
    accepted = ('amb','blu','brn','gry','grn','hzl','oth')
    ecl_ok = any(x in ecl for x in accepted)

    pid = passport.get('pid')
    pid_ok = len(pid) == 9 and pid.isnumeric()

    if byr_ok and eyr_ok and iyr_ok and hgt_ok and hcl_ok and ecl_ok and pid_ok:
      count += 1

  return count

def main():
  
  input_ = read_input()

  t0 = time.time()
  part1, valid_passports = solve_part1(input_)
  time_part1 = round((time.time()-t0)*1e3)
  print(f'Solution to part one: {part1} (time taken {time_part1}[ms])')

  t0 = time.time()
  part2 = solve_part2(valid_passports)
  time_part2 = round((time.time()-t0)*1e3)
  print(f'Solution to part two: {part2} (time taken {time_part2}[ms])')


if __name__ == '__main__':
  main()

@pytest.mark.parametrize("input1,output1", [
  ('../data/test_input0.txt', 1)
])

def test1(input1,output1):
  assert solve_part1(read_input(input1)) == output1

@pytest.mark.parametrize("input2,output2", [
  ('../data/test_input0.txt', 1)
])

def test2(input2,output2):
  assert solve_part2(read_input(input2)) == output2