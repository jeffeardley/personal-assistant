import subprocess
import openai
import re

WORKING_DIR = '/Users/jeffreyeardley/Desktop/Personal_Projects/personal-assistant'
api_key = "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"
openai.api_key = api_key

def get_response(usr_in, instructions):
  response = openai.ChatCompletion.create(
      model="gpt-4-1106-preview",
      messages=[
          {"role": "system", "content": instructions},
          {"role": "user", "content": usr_in}
          ]
      )
  output = response['choices'][0]['message']['content']
  return output

def continuous_response(instructions):
  response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
          {"role": "system", "content": instructions},
          ]
      )
  output = response['choices'][0]['message']['content']
  return output

def run_command(command):
  return subprocess.run(command, cwd=WORKING_DIR, stdout=subprocess.PIPE, universal_newlines=True)

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

def parse_commands(text):
  # Regex pattern to match '<some tag>some words</some tag>'
  # This pattern uses a non-greedy match (.*?) to capture the text inside the tag
  # and \1 to refer back to the captured tag name.
  pattern = r'<([^>]+)>.*?</\1>'

  # Find all matches and store them in a list
  commands = [match.group(0) for match in re.finditer(pattern, text)]
  return commands



def interpret_command(command):
  pattern = r'<([^>]+)>.*?</\1>'

  # Find all matches and store them in a list
  # re.findall will return only the contents of capturing groups, which in this case is the tag name.
  match = re.findall(pattern, command)[0]

  if match == 'command':
    pattern = r'<(?:[^>]+)>(.*?)</(?:[^>]+)>' # This pattern will match the text inside the tag
    command_text = re.findall(pattern, command)[0]
    run_command(command_text)

  elif match == 'sh':
    pattern = r'<(?:[^>]+)>(.*?)</(?:[^>]+)>'
    command_text = re.findall(pattern, command)[0]
    run_bash_script(command_text)

  elif match == 'python':
    pattern = r'<(?:[^>]+)>(.*?)</(?:[^>]+)>'
    command_text = re.findall(pattern, command)[0]
    run_python_script(command_text)

  elif match == 'get_python_files':
    return run_command(['ls', '-name', '*.py', WORKING_DIR + '/python_scripts'])
  
  elif match == 'get_python_file_doc':
    pattern = r'<(?:[^>]+)>(.*?)</(?:[^>]+)>'
    command_text = re.findall(pattern, command)[0]
    return get_python_documentation(command_text)
  
  elif match == 'get_sh_files':
    return run_command(['ls', '-name', '*.sh', WORKING_DIR + '/bash_scripts'])
  
  elif match == 'get_sh_file_doc':
    pattern = r'<(?:[^>]+)>(.*?)</(?:[^>]+)>'
    command_text = re.findall(pattern, command)[0]
    return get_bash_documentation(command_text)
  
  elif match == 'run_python_file':
    pattern = r'<(?:[^>]+)>(.*?)</(?:[^>]+)>'
    command_text = re.findall(pattern, command)[0]
    run_python_script(command_text)

  elif match == 'run_bash_file':
    pattern = r'<(?:[^>]+)>(.*?)</(?:[^>]+)>'
    command_text = re.findall(pattern, command)[0]
    run_bash_script(command_text)

  elif match == 'remember':
    pattern = r'<(?:[^>]+)>(.*?)</(?:[^>]+)>'
    command_text = re.findall(pattern, command)[0]
    return run_command(['echo', command_text, '>>', WORKING_DIR + '/instructions'])
  
  elif match == 'view_command_log':
    return run_command(['cat', WORKING_DIR + '/command_log'])
