import requests

url=requests.get("http://127.0.0.1:5000")

if url.status_code == 200:
    print("Opened")
else: 
    print("Not opened")