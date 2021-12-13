from PIL import Image
import requests
from io import BytesIO

def printimg(pixels, size):
    curseur = 0
    for pixel in pixels:
        if curseur == size[0]:
            curseur = 0
            print("")
        curseur += 1
        print(pixel, end="")

def getimg(url, new_width = 50):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    width, height = img.size
    aspect_ratio = height/width
    
    new_height = aspect_ratio * new_width * 0.47 # 0.47 est le ration de la largeur/hauteur d'un caractère
    img = img.resize((new_width, int(new_height)))

    def colored(r, g, b, text):
        return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


    pixels = []
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            try: r, g, b = img.getpixel((x, y))
            except: r, g, b, a = img.getpixel((x, y))
            pixels.append(colored(r, g, b, "█"))
    
    return pixels, (img.size[0], img.size[1])

def allinone(url, new_width = 50):
    pixels, size = getimg(url, new_width)
    printimg(pixels, size)

if __name__ == "__main__":
    allinone("https://avatars.githubusercontent.com/u/74245537?v=4", 100)