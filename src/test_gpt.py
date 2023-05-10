#%%
import os
import openai
openai.api_key_path = "../env"
print(openai.Model.list())
from pdfminer.high_level import extract_text

# make reaction
messages=[
        {"role": "system", "content": "あなたは親切なアシスタントです"},
        {"role": "user", "content": "こんにちは？"}
    ]

# input message
# new_message

# messages.append({"role": "user", "content": new_message})

response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)

print(response["choices"][0]["message"]["content"])

messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})


# PDFfile to text
# pdf_text = extract_text('../sample.pdf')
