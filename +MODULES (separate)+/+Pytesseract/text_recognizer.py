import cv2
import os
import pytesseract as pt

pt.pytesseract.tesseract_cmd = r'C:\Users\miker\AppData\Local\Programs\Tesseract-OCR\tesseract'
config = r'--oem 3 --psm 6'
dir_ = 'photos/'


# pip install pytesseract
# https://github.com/UB-Mannheim/tesseract/wiki -- install


def recognize(image=f'{dir_}p1.jpg', c=config, lang="eng"):
    """
    :param lang: language [ukr, rus, eng]
    :param image: photo source
    :param c: config for best recognition
    :return: text, that function founded
    """
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pt.image_to_string(image, config=c, lang=lang)

    cv2.imshow(f'{pht}', image)
    cv2.waitKey(0)
    return text


if __name__ == '__main__':
    for pht in os.listdir(dir_):
        print(f'{pht}:\n', recognize(image=f'{dir_}{pht}'), '\n')
