import cv2
import numpy as np


class LayoutAnalyzer:

    def __init__(self):
        pass

    def load_image(self, image_path):

        image = cv2.imread(image_path)

        return image

    def grayscale(self, image):

        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def threshold(self, gray):

        _, thresh = cv2.threshold(
            gray,
            150,
            255,
            cv2.THRESH_BINARY_INV
        )

        return thresh

    def detect_contours(self, thresh):

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        return contours

    def detect_blocks(self, image):

        gray = self.grayscale(image)

        thresh = self.threshold(gray)

        contours = self.detect_contours(thresh)

        blocks = []

        output = image.copy()

        for contour in contours:

            x, y, w, h = cv2.boundingRect(contour)

            if w > 80 and h > 20:

                cv2.rectangle(
                    output,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                blocks.append({

                    "x": x,
                    "y": y,
                    "width": w,
                    "height": h

                })

        return output, blocks

    def analyze(self, image_path):

        image = self.load_image(image_path)

        output, blocks = self.detect_blocks(image)

        print(f"Detected {len(blocks)} document regions")

        return output, blocks


if __name__ == "__main__":

    analyzer = LayoutAnalyzer()

    output, blocks = analyzer.analyze(
        "data/sample_invoice.png"
    )

    cv2.imwrite(
        "reports/layout_detection.png",
        output
    )

    print(blocks)