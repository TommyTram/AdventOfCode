#!/usr/bin/env python3
from os.path import dirname, realpath, join
import time, pytest

def transform_input(input_):
  # custom transform for the day
  line = input_.splitlines()
  operations = {}
  for i, command in enumerate(line):
    action, value = command.split(' ')
    operations.update({i:[action, int(value)]})
  
  return operations


def read_input(file_name = '../data/input.txt'):
  dir_path = dirname(realpath(__file__))
  with open(join(dir_path,file_name), 'r') as f:
    input_ = transform_input(f.read())

  return input_
class Executer:
  def __init__(self, operations):
    self.op = operations
    self.accumulator = 0
    self.executed_commands = {}
    self.done = False

  def run(self, command_id):
    if command_id >= len(self.op):
      print('Done')
      self.done = True
      return 1000
    action, value = self.op.get(command_id)
    if action == 'nop':
      next_action = command_id + 1
    elif action == 'acc':
      self.accumulator += value
      next_action = command_id + 1
    elif action == 'jmp':
      next_action = command_id + value
    else:
      print('Done')
      self.done = True
      next_action = 1000

    self.executed_commands.update({command_id:next_action})
    return next_action

  def is_repeat(self, command_id):
    return True if self.executed_commands.get(command_id) else False

def solve_part1(input_):

  executer = Executer(input_)
  id_ = 0
  while 1: 
    
    if executer.is_repeat(id_) or executer.done:
      break
    else:
      id_ = executer.run(id_)

  return executer.accumulator, executer.done


def solve_part2(input_):

  for id_, command in input_.items():
    
    if command[0] == 'acc':
      continue
    elif command[0] == 'nop':
      input_.update({id_:['jmp',command[1]]})
      acc, done = solve_part1(input_)
      input_.update({id_:['nop',command[1]]})
    elif command[0] == 'jmp':
      input_.update({id_:['nop',command[1]]})
      acc, done = solve_part1(input_)
      input_.update({id_:['jmp',command[1]]})
    
    if done:
      return acc


def main():
  
  input_ = read_input()

  t0 = time.time()
  part1, done = solve_part1(input_)
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