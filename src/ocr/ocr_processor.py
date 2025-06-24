from paddleocr import PaddleOCR
import os

model_ocr = PaddleOCR(use_angle_cls=True, lan='en')

def run_ocr_on_image(imagepath):

    if not os.path.exists(imagepath):
        raise FileExistsError(f"file not found on {imagepath}")
    
    result = model_ocr.ocr(imagepath, cls=True)
    resultant_list = []

    for line in result[0]:
        resultant_list.append(line[1][0])

    return resultant_list