from paddleocr import PaddleOCR


class NotFound(Exception):
    pass


def get_position(img, text):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # cv2.imwrite('tmp/crop.png', img)
    result = ocr.ocr(img, cls=True)
    for line in result:
        if line[1][0] == text:
            return tuple(line[0][0]), tuple(line[0][2])
    raise NotFound()
