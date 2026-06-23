import pytesseract
from PIL import Image
import io

def local_tesseract_ocr(file_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(file_bytes))
    text = pytesseract.image_to_string(image)
    return text.strip()