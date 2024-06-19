import webhook
import requests
from time import sleep

def get_cat_image():
    try:
        response = requests.get("https://cataas.com/cat?json=true")
        img_id = response.json()["_id"]

        url = f"https://cataas.com/cat/{img_id}"
        return url
    except:
        None



def main():
    SECONDS_BETWEEN_IMAGE = 60

    i = 0
    while True:
        image = get_cat_image()

        if image == None:
            e = "error: Failed to obtain cat photo"
            print(e)
            webhook.execute_webhook(text=e)
            sleep(SECONDS_BETWEEN_IMAGE)
            continue

        image.save("image.png")

        webhook.execute_webhook(text=get_cat_image())
        i += 1

        sleep(SECONDS_BETWEEN_IMAGE)

if __name__ == "__main__":
    main()
