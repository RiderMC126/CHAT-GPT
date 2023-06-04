import openai


openai.api_key = 'API-KEY'
engine = "text-davinci-003"

prompt = 'QUESTION'

completion = openai.Completion.create(engine=engine,
                                     prompt=prompt,
                                     temperature=1,
                                     max_tokens=1000)

print(f'ANSWER: {completion.choices[0]["text"]}')
