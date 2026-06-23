from .ocr_engine import local_tesseract_ocr

def read_image(file_bytes: bytes) -> str:
    text = local_tesseract_ocr(file_bytes)
    return text