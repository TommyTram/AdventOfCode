#!/usr/bin/env python3
from os.path import dirname, realpath, join
import time, pytest

def transform_input(input_):
  # custom transform for the day
  new_in = [int(line) for line in input_.splitlines()]
  return new_in


def read_input(file_name = '../data/input.txt'):
  dir_path = dirname(realpath(__file__))
  with open(join(dir_path,file_name), 'r') as f:
    input_ = transform_input(f.read())

  return input_

def get_valid(preamble):
  valid_list = []
  for i, num in enumerate(preamble):
    for rest in preamble[i+1:]:
      valid_list.append(num+rest)
  return valid_list

def solve_part1(input_):
  pre_size = 25
  for i in range(pre_size,len(input_)):
    num = input_[i]
    preamble = input_[i-pre_size:i]
    valid_list = get_valid(preamble)
    if num not in valid_list:
      return num

def get_contin_set(input_, invalid_num, start_set, index):
  for num in input_[index+len(start_set):]:
    start_set.append(num)
    if sum(start_set) >= invalid_num:
      return start_set
  

def solve_part2(input_, invalid_num):
  contin_set = []
  
  for i in range(len(input_)):

    contin_set = get_contin_set(input_, invalid_num, contin_set, i)
    if sum(contin_set) == invalid_num:
      break

    if sum(contin_set) > invalid_num:
      # move sliding window
      contin_set.pop(0)

      while sum(contin_set) > invalid_num:
        # remove all extensive numbers
        contin_set.pop()

      if sum(contin_set) == invalid_num:
        break

  weakness = min(contin_set) + max(contin_set)
  return weakness
    
def main():
  
  input_ = read_input()

  t0 = time.time()
  part1 = solve_part1(input_)
  time_part1 = round((time.time()-t0)*1e3)
  print(f'Solution to part one: {part1} (time taken {time_part1}[ms])')

  t0 = time.time()
  part2 = solve_part2(input_, part1)
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