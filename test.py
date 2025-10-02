import requests

url = "http://127.0.0.1:8000/remove-bg"
files = {"file": open("sample.png", "rb")}  # replace with your image path

response = requests.post(url, files=files)

with open("output.png", "wb") as f:
    f.write(response.content)

print("Done! Output saved as output.png")
