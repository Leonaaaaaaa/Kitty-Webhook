import PIL.Image
import webhook
import requests
import random
from time import sleep

def generate_image():
    SIZE = 500
    CELL_SIZE = 50

    image = PIL.Image.new("RGB", (SIZE, SIZE), "white")
    pixels = image.load()

    for x in range(0, SIZE, CELL_SIZE):
        for y in range(0, SIZE, CELL_SIZE):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for i in range(CELL_SIZE):
                for j in range(CELL_SIZE):
                    pixels[x+i, y+j] = color
    return image

def get_cat_image():
    response = requests.get("https://cataas.com/cat?json=true")
    img_id = response.json()["_id"]

    url = f"https://cataas.com/cat/{img_id}"
    return url



def main():
    i = 0
    while True:
        image = generate_image()
        image.save("image.png")

        webhook.execute_webhook(text=get_cat_image())
        i += 1

        sleep(60)

if __name__ == "__main__":
    main()
