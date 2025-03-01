# import requests 
from flask import Flask

S_App= Flask(__name__)
# url=requests.get("https://www.youtube.com/")

# if url.status_code == 200:
#     print("Opened")
# else: 
#     print("Not opened")


@S_App.route('/', methods=['GET'])
def HW():
    print("Hello World")
    
    return {}

if __name__=='__main__':
    S_App.run(debug=True)
