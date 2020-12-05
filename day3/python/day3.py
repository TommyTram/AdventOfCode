#!/usr/bin/env python3
from os.path import dirname, realpath, join
import time, pytest

def transform_input(input_):
  # custom transform for the day
  input_ = input_.splitlines()
  return input_


def read_input(file_name = '../data/input.txt'):
  dir_path = dirname(realpath(__file__))
  with open(join(dir_path,file_name), 'r') as f:
    input_ = transform_input(f.read())

  return input_

def solve_part1(input_, x_step = 3, y_step=1):
  pos = 0
  y = 0
  count = 0
  # check = list()
  # check.append(input_[0])
  for _ in range(len(input_)):
    y += y_step
    if y >= len(input_): break
    line = input_[y]
    eol = len(line)
    pos += x_step
    if pos >= eol:
      pos = pos - eol

    # tmp = list(line)

    if line[pos] == '#':
      count += 1
      # tmp[pos] = 'X'

    # else:
    #   tmp[pos] = 'O'
    # check.append("".join(tmp))

  return count


def solve_part2(input_):
  x = (1,3,5,7,1)
  y = (1,1,1,1,2)
  res = 1
  for x,y in zip(x,y):
    res *= solve_part1(input_,x,y)

  return res


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