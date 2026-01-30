import os
from PyPDF2 import PdfReader, PdfWriter
import os
import pathlib
os.chdir(pathlib.Path(__file__).parent.resolve())

input_path = "Female 49 AGLA 3m 10Pay@65160.pdf"
output_path = "age_3_of_49.pdf"

reader = PdfReader(input_path)
writer = PdfWriter()

# Page numbers are 0-based in PyPDF2; page 3 => index 2
writer.add_page(reader.pages[2])

with open(output_path, "wb") as f:
    writer.write(f)

output_path, len(reader.pages)

