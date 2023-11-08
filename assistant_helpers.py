import subprocess

WORKING_DIR = '/Users/jeffreyeardley/Desktop/Personal_Projects/personal-assistant'

def run_command(command):
  subprocess.run(command, cwd=WORKING_DIR)

def create_python_script(name, content, documentation):
  comments = '# Start of a new Python program'
  with open(WORKING_DIR + '/python_scripts/' + name + '.py', 'w') as f:
    f.write(comments + '\n' + content)
  f.close()
  with open(WORKING_DIR + '/python_scripts/' + name + '.txt', 'w') as f:
    f.write(comments + '\n' + documentation)
  f.close()

def get_python_documentation(name):
  with open(WORKING_DIR + '/python_scripts/' + name + '.txt', 'r') as f:
    return f.read()

def create_bash_script(name, content, documentation):
  comments = '#!/bin/bash'
  with open(WORKING_DIR + '/bash_scripts/' + name + '.sh', 'w') as f:
    f.write(comments + '\n' + content)
  f.close()
  with open(WORKING_DIR + '/python_scripts/' + name + '.txt', 'w') as f:
    f.write(comments + '\n' + documentation)
  f.close()

def get_bash_documentation(name):
  with open(WORKING_DIR + '/bash_scripts/' + name + '.txt', 'r') as f:
    return f.read()

def run_python_script(name):
  run_command(['python3', WORKING_DIR + '/python_scripts/' + name + '.py'])

def run_bash_script(name):
  run_command([WORKING_DIR + '/bash_scripts/' + name + '.sh'])