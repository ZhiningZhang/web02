import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os, re
import pathlib
os.chdir(pathlib.Path(__file__).parent.resolve())

pdf_path = "age_3_of_49.pdf"

# Convert first page of PDF to image
images = convert_from_path(pdf_path, dpi=300, first_page=1, last_page=1)
img = images[0]

# OCR
ocr_text = pytesseract.image_to_string(img)

print(ocr_text)

# ocr_clean = re.sub(r'\n{3,}', '\n\n', ocr_text).strip()

# ocr_clean[:2000], len(ocr_clean)

# pip install pytesseract pdf2image Pillow
