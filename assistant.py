import openai

api_key = "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"
openai.api_key = api_key

with open('instructions', 'r') as file:
  instructions = file.read()

def get_response(character, context):
  response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
          {"role": "system", "content": character},
          {"role": "user", "content": context}
          ]
      )
  return response