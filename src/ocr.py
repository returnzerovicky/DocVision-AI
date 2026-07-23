from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import easyocr
import pytesseract
import torch
import os


class OCRProcessor:

    def __init__(self):

        print("Loading AI models...")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.processor = TrOCRProcessor.from_pretrained(
            "microsoft/trocr-base-printed"
        )

        self.model = VisionEncoderDecoderModel.from_pretrained(
            "microsoft/trocr-base-printed"
        ).to(self.device)

        self.easyocr_reader = easyocr.Reader(["en"])

        print("Models Loaded Successfully!")

    def trocr(self, image_path):

        image = Image.open(image_path).convert("RGB")

        pixel_values = self.processor(
            images=image,
            return_tensors="pt"
        ).pixel_values.to(self.device)

        generated_ids = self.model.generate(pixel_values)

        text = self.processor.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0]

        return text

    def easyocr(self, image_path):

       result = self.easyocr_reader.readtext(
           image_path,
           detail=0,
           paragraph=True
       )

       return "\n".join(result)

    def tesseract(self, image_path):

        image = Image.open(image_path)

        return pytesseract.image_to_string(image)

    def compare_models(self, image_path):

        print("=" * 60)
        print("TrOCR Output")
        print("=" * 60)

        trocr_text = self.trocr(image_path)
        print(trocr_text)

        print("\n")

        print("=" * 60)
        print("EasyOCR Output")
        print("=" * 60)

        easy_text = self.easyocr(image_path)
        print(easy_text)

        print("\n")

        print("=" * 60)
        print("Tesseract Output")
        print("=" * 60)

        tess_text = self.tesseract(image_path)
        print(tess_text)

        return {
            "trocr": trocr_text,
            "easyocr": easy_text,
            "tesseract": tess_text
        }


if __name__ == "__main__":

    sample = "data/sample_invoice.png"

    if os.path.exists(sample):

        ocr = OCRProcessor()

        ocr.compare_models(sample)

    else:

        print("Place an image named sample_invoice.png inside data/")