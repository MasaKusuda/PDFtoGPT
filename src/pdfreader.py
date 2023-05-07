#%%
from pdfminer.high_level import extract_text
pdf_text = extract_text('../sample.pdf')

#%%
print("type  :"+ str(type(pdf_text)))
print("length:"+ str(len(pdf_text)))

#%%
print("最初の10行を出力")
for line in pdf_text[:10]:
    print(line)

print("最後の10行を出力")
for line in pdf_text[-10:]:
    print(line)
