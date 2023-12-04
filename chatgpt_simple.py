import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me the history of mammoths. "}])
print(completion.choices[0].message.content)