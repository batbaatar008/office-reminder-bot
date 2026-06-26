import requests

url = "https://dsedn-my.sharepoint.com/:x:/g/personal/batbaatar_dsedn_mn/IQDrufGpU0agS6qPGZKJ3gTiAa0ZEF-geadYdU9juHaboQU?e=5B2hrI"

response = requests.get(url, allow_redirects=True)

print("Status:", response.status_code)
print("Content-Type:", response.headers.get("content-type"))
print("First 200 chars:")
print(response.text[:200])

with open("test_download.xlsx", "wb") as f:
    f.write(response.content)

print("Downloaded size:", len(response.content))
