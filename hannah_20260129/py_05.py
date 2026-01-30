import pytesseract
from pdf2image import convert_from_path
from PIL import Image

# --- CONFIGURATION (Required for Windows users) ---
# If Tesseract and Poppler are in your PATH, you can leave these commented out.
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# POPPLER_PATH = r'C:\path\to\poppler-xx\Library\bin'

def extract_text_from_pdf(pdf_path):
    # 1. Convert PDF pages to a list of PIL images
    # We use 300 DPI for better OCR accuracy on documents like yours
    print(f"Converting {pdf_path} to images...")
    pages = convert_from_path(pdf_path, dpi=300) # add poppler_path=POPPLER_PATH if needed

    full_text = ""

    # 2. Iterate through each page image and perform OCR
    for i, page_image in enumerate(pages):
        print(f"Processing Page {i + 1}...")
        
        # Extract text from the image
        page_text = pytesseract.image_to_string(page_image)
        
        full_text += f"--- PAGE {i + 1} ---\n"
        full_text += page_text + "\n"

    return full_text

if __name__ == "__main__":
    pdf_file = 'f1.pdf'
    try:
        extracted_content = extract_text_from_pdf(pdf_file)
        
        # Save the result to a text file
        with open("extracted_output.txt", "w", encoding="utf-8") as f:
            f.write(extracted_content)
            
        print("Success! Text saved to extracted_output.txt")
        
    except Exception as e:
        print(f"An error occurred: {e}")

        