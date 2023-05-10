import openai
from pdfminer.high_level import extract_text

def read_pdf_to_text(file_path):
  return extract_text(file_path)

def access_to_GPT(messages=None):
  return_obj = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
  print(return_obj["choices"][0]["message"]["content"])
  print(return_obj["usage"])
  return return_obj



# pdf_text = extract_text('../sample.pdf').replace('\n','')



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

