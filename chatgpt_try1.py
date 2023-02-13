import os
import openai

openai.organization = "org-mrxnAgaiysJ9WO4bQtgZvqrI"
openai.api_key = os.getenv("OPENAI_API_KEY")

model_engine = "text-davinci-003"
prompt = "Hello, how are you today?"
completion = openai.Completion.create(
  engine=model_engine,
  prompt=prompt,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.7
)
message = completion.choices[0].text
print(message)
