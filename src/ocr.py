from paddleocr import PaddleOCR
from paddle.fluid import is_compiled_with_cuda


class NotFound(Exception):
    pass


def get_position(img, text):
    use_gpu = is_compiled_with_cuda()
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=use_gpu)
    result = ocr.ocr(img, cls=True)
    for line in result:
        if line[1][0] == text:
            return tuple(line[0][0]), tuple(line[0][2])
    raise NotFound()
