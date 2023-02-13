import os
import openai

openai.organization = "org-mrxnAgaiysJ9WO4bQtgZvqrI"
openai.api_key = os.getenv("OPENAI_API_KEY")

model_engine = "text-davinci-003"
prompt =
"""
Write a rehome bulletin for a cat.
The cat's name is Meow-Meow.
She is a beautiful black and white Siberian cat.
Siberian cats shed less than a regular cat even though they have long fur.
She is an outdoors cat and initially extremely timid, but she has a social side and once she opens up she talks a lot.
Other cats can be mean to her, although Butch for example is oblivious and Meow-Meow hisses at him.
I've seen her interacting with a bunny fine, so she may get along with other pets though.
She needs shelter especially for the night sometimes and when the weather is bad.
Without that she sadly resort to hide under cars which is heart breaking.
She lived in the countryside and was a baarn cat for many years but due to life changing circumnstances the owner had to move so Meow-Meow lost her barn, and she is now around the apartment complex.
When she is inside she requests to be let outside when it's time to do her business.
Anyone interested can email asiandeltas@gmail.com.
Write the bulletin in first person and in a bubbly, friendly, affectionate tone.
"""
completion = openai.Completion.create(
  engine=model_engine,
  prompt=prompt,
  max_tokens=1576,
  n=1,
  stop=None,
  temperature=0.7
)
message = completion.choices[0].text
print(message)
