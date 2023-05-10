import os
import openai
openai.api_key_path = "env"
print(openai.Model.list())
from pdfminer.high_level import extract_text
def read_pdf_to_text(file_path):
  return extract_text(file_path).replace('\n','')

# pdf_text = extract_text('../sample.pdf').replace('\n','')

# return_obj = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "user", "content": "compress the below content. " + pdf_text},
#     ]
# )
# print(return_obj["choices"][0]["message"]["content"])
# print(return_obj["usage"])

# compressd_context = return_obj["choices"][0]["message"]["content"]
# return_obj = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role":"assistant", "content":"context of the paper is below." + compressd_context},
#         {"role": "user", "content": "tell me what is the new point of this paper" }
#     ]
# )
# print(return_obj["choices"][0]["message"]["content"])
# print(return_obj["usage"])
#%%

