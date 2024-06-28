from openai import OpenAI
client = OpenAI(
    api_key="YE GAREEB KO $6 chaiye :("
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "what is the worlds highest peek"}
  ]
)

print(completion.choices[0].message.content)