import re
from PyPDF2 import PdfReader
import os
import pathlib
os.chdir(pathlib.Path(__file__).parent.resolve())

pdf_path = "age_3_of_49.pdf"
reader = PdfReader(pdf_path)

text = ""
for page in reader.pages:
    print(' aaaa ')
    t = page.extract_text() or ""
    text += t + "\n"
    # print(t)

print(text)
# # clean up multiple blank lines
# clean_text = re.sub(r'\n{3,}', '\n\n', text).strip()

# clean_text[:2000], len(clean_text)

