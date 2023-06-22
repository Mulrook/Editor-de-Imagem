from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs" # folder de imagens
pathOut = "./editImgs" # folder de imagens editadas

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # transforma em preto e branco
    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    # contraste
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)


    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')