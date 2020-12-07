#!/usr/bin/env python3
from os.path import dirname, realpath, join
import time, pytest, copy

def transform_input(input_):
  # custom transform for the day

  lines = input_.splitlines()
  bag_lable = {}
  for line in lines:
    contain = {}
    words = line.split(' ')
    words_per_bag = 4
    if len(words)>7:
      for i in range(1,int(len(words[words_per_bag:])/words_per_bag+1)):
        bag = words[words_per_bag*i:words_per_bag*i+words_per_bag]
        contain.update({' '.join(bag[1:3]): int(bag[0])}) 
      bag_lable.update({' '.join(words[:2]):contain})
    else: # special case when no sub bags
      assert(words[-3] == 'no')
      bag_lable.update({' '.join(words[:2]):0})

  input_ = bag_lable
  return input_

def read_input(file_name = '../data/input.txt'):
  dir_path = dirname(realpath(__file__))
  with open(join(dir_path,file_name), 'r') as f:
    input_ = transform_input(f.read())

  return input_

def find_acceped_labes(input_, accepted_lables):
  
  for bag_lable, contain in input_.items():
    if contain == 0: continue
    if any(key in contain.keys() for key in accepted_lables):
      accepted_lables.append(bag_lable)

  return accepted_lables

def find_nr_bags(input_, bag_color):
  sum_bags = 0
  if isinstance(input_.get(bag_color),dict):
    for key, val in input_.get(bag_color).items():
      for _ in range(val):
        sum_bags += find_nr_bags(input_, key) + 1
  return sum_bags

def solve_part1(input_):
  accepted_lables = ['shiny gold']
  old_len = len(accepted_lables)
  new_len = old_len +1
  new_labels = []
  input_part1 = copy.deepcopy(input_)
  while old_len< new_len:
    old_len = len(accepted_lables)
    accepted_lables = find_acceped_labes(input_part1,accepted_lables)
    for lable in accepted_lables:
      if input_part1.get(lable):
        new_labels.append(input_part1.pop(lable))
    new_len = len(accepted_lables)

  return len(accepted_lables)-1

def solve_part2(input_):
  nr_bags = find_nr_bags(input_, 'shiny gold')
  return nr_bags


def main():
  
  input_ = read_input()

  t0 = time.time()
  part1 = solve_part1(input_)
  time_part1 = round((time.time()-t0)*1e3)
  print(f'Solution to part one: {part1} (time taken {time_part1}[ms])')

  t0 = time.time()
  part2 = solve_part2(input_)
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