import secrets

import requests

url="https://shikimori.me"
live_proxy=[]
scrs=["/system/screenshots/original/b9e4692221236fc0707c8e16f47e272e635600a8.jpg?1648915900",
      "/system/screenshots/original/e7b262e0abd3c06643f14bf864602bf6c737b588.jpg?1423557526",
      "/system/screenshots/original/036242ec534d0238f5722f6c2369582fe7f1b6e7.jpg?1651258447",
      "/system/screenshots/original/d7e90017474c96f26a20f7f8f63b4e20422d01e0.jpg?1649176783"]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

for scr in scrs:
    url = url+scr
    response = requests.get(url,headers=headers, stream=True)
    response.raise_for_status()

    # Set the file name, including the correct file extension (e.g., .jpg, .png, etc.)
    filename = f'downloaded_image_{secrets.token_hex(10)}.jpg'

    # Write the content of the request to a local file
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Image saved as {filename}")
