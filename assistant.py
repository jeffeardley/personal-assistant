import assistant_helpers as helpers

with open('instructions', 'r') as file:
  instructions = file.read()


def main():
  usr_in = input("Enter your message: ")
  output = helpers.get_response(usr_in, instructions)
  commands = helpers.parse_commands(output)
  for command in commands:
    helpers.interpret_command(command)
  output = helpers.continuous_response('analyze your results', instructions)
  print(output)
  while True:
    output = helpers.continuous_response('continue helping', instructions)
    print(output)
main()
