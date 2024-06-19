import io
import requests

def get_file(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()

def execute_webhook(text: str = None, username: str = None, avatar_url: str = None, files: io.BytesIO = None, image_url: str = None) -> requests.Response:
    def get_token() -> str:
        with open("KEYS/TOKEN.KEY", "r") as f:
            return f.read().strip()

    def get_id() -> str:
        with open("KEYS/ID.KEY", "r") as f:
            return f.read().strip()
    
    url = f"https://discordapp.com/api/webhooks/{get_id()}/{get_token()}"

    data = {
        "content": text,
        "username": username,
        "avatar_url": avatar_url
    }

    try:
        response = requests.post(url, data=data, files=files)

        if response.status_code == 204:
            return response
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
        
    except Exception as e:
        error_message = f"Error: {e}"
        error_message = error_message.replace(get_token(), "WEBHOOK_TOKEN")
        error_message = error_message.replace(get_id(), "WEBHOOK_ID")

        print(error_message)
        try:
            requests.post(url, data={"content": error_message})
        except:
            pass
    return None
